# rpdr.py

'''
*****************************************************
Example use:

# instantiate
import rpdr
F = rpdr.SqliteFactory()

# import all RPDR tables in a directory
F.build_database( "/Users/nathanielreynolds/Documents/Career/'12 Mass General Hosptial/Atrial Fibrillation Project/rpdr_data/Detailed_data_request_2012-present" )

# import a single RPDR table
F.build_table( "path/to/rpdrfile.txt" )


*****************************************************
'''




# add working directory to search path
import os
import sys
sys.path.insert(0, os.path.realpath(__file__))

# get RPDR Table info
import rpdrtables

# get file management tools
import shutil
import fnmatch
import re

# get SQLite tools
import sqlite3

# get csv tools
import csv

# get time tools
import time





class SqliteFactory:

    #--------------------------------------------------------------------------------------------
    # build SQLite database from RPDR tables in the given directory
    def build_database( self, buildDir ):

        # check that the given import directory exists
        if not os.path.isdir(buildDir):
            print "Error! Import directory doesn't exist: %s" % buildDir
            return

        # list the import directory files
        buildDirFiles = [ f for f in os.listdir(buildDir) if os.path.isfile( os.path.join(buildDir,f) ) ]

        # check that there are files in this directory
        if len(buildDirFiles) < 1:
            print "Error! No files found in import directory: %s" % buildDir
            return

        # get list of vaild RPDR file endings
        rpdrFileEndings = [ '%s.%s' % (table.fileSuffix, table.fileExt) for table in rpdrtables.Tables]

        # check if each file is an RPDR file
        rpdrFiles = []
        rpdrFilePrefixes = []
        for file in buildDirFiles:
            for fileEnding in rpdrFileEndings:
                if file.endswith( fileEnding ):
                    rpdrFiles.append(file)
                    rpdrFilePrefixes.append( file.rstrip(fileEnding) )
                    break

        # check that RPDR files were found
        if len(rpdrFiles) < 1:
            print "Error! No RPDR files were found in import directory: %s" % buildDir
            return

        # check that all RPDR files have the same prefix
        rpdrFilePrefixes = list(set( rpdrFilePrefixes ))
        if len(rpdrFilePrefixes) > 1:
            print "Error! Not all the RPDR files have the same prefix: %s" % str(rpdrFilePrefixes)
            return

        # info
        print "Will build SQLite database from the following RPDR files:"
        for file in rpdrFiles:
            print " - %s" % file

        # build each table
        for file in rpdrFiles:
            self.build_table( os.path.join(buildDir,file) )




    #--------------------------------------------------------------------------------------------
    # build a single RPDR table
    def build_table( self, tablePath ):

        print "Building table from %s..." % os.path.basename(tablePath)
        # check that file exists
        if not os.path.exists( tablePath ):
            print " Error! RPDR table file doesn't exist: %s" % tablePath
            return

        # check that file is an RPDR file
        rpdrTable = None
        for t in rpdrtables.Tables:
            if tablePath.endswith( '%s.%s' % (t.fileSuffix, t.fileExt) ):
                rpdrTable = t

        if rpdrTable == None:
            print " Error! File provided is not a recognized RPDR file: %s" % tablePath
            return

        # open file as csv file with approriate dialect
        csvFile = open(tablePath,"rb")
        csvReader = csv.reader(
            csvFile,
            delimiter = rpdrTable.csvDialect.delimiter,
            doublequote = rpdrTable.csvDialect.doublequote,
            escapechar = rpdrTable.csvDialect.escapechar,
            lineterminator = rpdrTable.csvDialect.lineterminator,
            quotechar = rpdrTable.csvDialect.quotechar,
            quoting = rpdrTable.csvDialect.quoting,
            skipinitialspace = rpdrTable.csvDialect.skipinitialspace,
            strict = rpdrTable.csvDialect.strict
        )


        # get headers from file
        headers = csvReader.next()[0].split(rpdrTable.csvDialect.delimiter)

        # check headers against table templates
        rpdrTableColumnNames = [ col.name for col in rpdrTable.columns ]
        unexpectedCols = []
        for header in headers:
            if header not in rpdrTableColumnNames:
                unexpectedCols.append( header )

        if len(unexpectedCols) > 0:
            print " Error! Unexpected columns found: %s" % str(unexpectedCols)
            return

        # connect to SQLite database and enable dictionary access of rows
        dbPath = '%sDB.sqlite' % tablePath.strip( '%s.%s' % (rpdrTable.fileSuffix, rpdrTable.fileExt) )
        dbCon = sqlite3.connect(dbPath)
        dbCon.row_factory = sqlite3.Row
        print " Connected to SQLite database: %s" % os.path.basename(dbPath)


        # check if the RPDR table already exists
        dbTableName = rpdrTable.fileSuffix
        qResult = None
        with dbCon:
            dbCur = dbCon.cursor()
            dbCur.execute( "SELECT name FROM sqlite_master WHERE type='table' AND name='%s'" % dbTableName )
            qResult = dbCur.fetchone()

        if qResult is not None:
            print " Error! The RPDR table '%s' already exists." % dbTableName
            return

        # create column declarations
        colDecs = []
        for col in rpdrTable.columns:
            newDec = " `%s` %s " % (col.name, col.type)
            if col.notNull:
                newDec = " %s NOT NULL " % newDec
            if col.primaryKey:
                newDec = " %s PRIMARY KEY " % newDec

            colDecs.append( newDec )

            # shouldn't use unique with "INSERT OR IGNORE" below to avoid unexpected ignoring of data
            # not including foreign keys, because not worth the work.
            #if col.unique:
            #    newDec = " %s UNIQUE " % newDec


        # create database table
        print " Creating '%s' database table..." % dbTableName
        qCreate = "CREATE TABLE `%s` ( %s )" % ( dbTableName, ','.join(colDecs) )
        with dbCon:
            dbCur = dbCon.cursor()
            dbCur.execute(qCreate)

        # add column indices
        for col in rpdrTable.columns:
            if col.index:
                with dbCon:
                    dbCur = dbCon.cursor()
                    qIndex = "CREATE INDEX `%s_%s_idx` ON `%s` (`%s`)" % (dbTableName, col.name, dbTableName, col.name)
                    dbCur.execute(qIndex)


        # prepare insert query - will ignore duplicates for tables with primary keys and uniqueness
        qInsert = "INSERT OR IGNORE INTO %s ( `%s` ) VALUES ( %s )" % (dbTableName, '`, `'.join(rpdrTableColumnNames), ', '.join([ '?' for col in rpdrTableColumnNames]) )

        # fill table
        print " Filling '%s' database table..." % dbTableName
        with dbCon:
            dbCur = dbCon.cursor()
            numCols = len(rpdrTableColumnNames)
            for rIdx, row in enumerate(csvReader):
                
                # check for too few columns
                if len(row) < numCols:
                    print " Error (row %d)! Less than %d columns found! %s" % (rIdx+1, numCols, row)
                    return
                
                # handle extra columns: combine end columns
                if len(row) > numCols:
                    row = row[:numCols-1] + ['|'.join(row[numCols-1:])]
                
                # handle date reformat
                for cIdx, col in enumerate(rpdrTable.columns):
                    if col.dateReformat and row[cIdx]:
                        row[cIdx] = time.strftime( col.dateReformat.reformat, time.strptime(row[cIdx], col.dateReformat.format) )
                
                # handle free-text report in last column
                if rpdrTable.freeTextReportInLastColumn:
                    reportRows = [ row[-1] ]
                    while 1:
                        nextRow = csvReader.next()
                        if not nextRow:
                            reportRows.append('')
                        else:
                            if '[report_end]' not in nextRow[0]:
                                reportRows.append( '|'.join(nextRow) )
                            else:
                                break
                    row[-1] = '\n'.join(reportRows)
                    
                # insert row into database
                dbCur.execute(qInsert, row)

        # close file
        csvFile.close()

        # info
        print " Done!"






















