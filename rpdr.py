# rpdr.py

'''
*****************************************************
Example use:

# instantiate SQLite Factory
import rpdr
F = rpdr.SqliteFactory()

# import all RPDR tables in a directory
F.build_database( "/Users/nathanielreynolds/Documents/Career/'12 Mass General Hosptial/Atrial Fibrillation Project/rpdr_data/Detailed_data_request_2012-present" )

# import a single RPDR table
F.build_table( "path/to/rpdrfile.txt" )


# instantiate Patient
import rpdr
dbpath = "/Users/nathanielreynolds/Documents/Career/'12 Mass General Hosptial/Atrial Fibrillation Project/rpdr_data/Detailed_data_request_2012-present/JNR0_20130508_103057_MGH_DB.sqlite"
P = rpdr.Patient(dbpath, empi='100090828', mrn='54321')

# view patient timeline
P.timeline(['Rdt','Rad'])

# view specific event
P.event('Rad', 1)

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
        rpdrFileEndings = [ '%s.%s' % (table.name, table.fileExt) for table in rpdrtables.Tables]

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
            if tablePath.endswith( '%s.%s' % (t.name, t.fileExt) ):
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
        dbPath = '%sDB.sqlite' % tablePath.strip( '%s.%s' % (rpdrTable.name, rpdrTable.fileExt) )
        dbCon = sqlite3.connect(dbPath)
        dbCon.row_factory = sqlite3.Row
        print " Connected to SQLite database: %s" % os.path.basename(dbPath)


        # check if the RPDR table already exists
        #rpdrTable.name = rpdrTable.name
        qResult = None
        with dbCon:
            dbCur = dbCon.cursor()
            dbCur.execute( "SELECT name FROM sqlite_master WHERE type='table' AND name='%s'" % rpdrTable.name )
            qResult = dbCur.fetchone()

        if qResult is not None:
            print " Error! The RPDR table '%s' already exists." % rpdrTable.name
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
        print " Creating '%s' database table..." % rpdrTable.name
        qCreate = "CREATE TABLE `%s` ( %s )" % ( rpdrTable.name, ','.join(colDecs) )
        with dbCon:
            dbCur = dbCon.cursor()
            dbCur.execute(qCreate)

        # add column indices
        for col in rpdrTable.columns:
            if col.index:
                with dbCon:
                    dbCur = dbCon.cursor()
                    qIndex = "CREATE INDEX `%s_%s_idx` ON `%s` (`%s`)" % (rpdrTable.name, col.name, rpdrTable.name, col.name)
                    dbCur.execute(qIndex)


        # prepare insert query - will ignore duplicates for tables with primary keys and uniqueness
        qInsert = "INSERT OR IGNORE INTO %s ( `%s` ) VALUES ( %s )" % (rpdrTable.name, '`, `'.join(rpdrTableColumnNames), ', '.join([ '?' for col in rpdrTableColumnNames]) )

        # fill table
        print " Filling '%s' database table..." % rpdrTable.name
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





class Patient:

    #--------------------------------------------------------------------------------------------
    def __init__( self, dbPath=None, empi=None, mrn=None ):
    
        # validate args
        if dbPath is None:
            print " Error: must provide database path."
            return
        if empi is None and mrn is None:
            print " Error: must provide EMPI or MRN."
            return
        
        # define class variables
        self.dbPath = dbPath
        self.empi = empi
        self.mrn = mrn
        self.possibleRpdrTableNames = [ t.name for t in rpdrtables.Tables ]
        self.possibleTimelineTableNames = [ t.name for t in rpdrtables.Tables if t.useInTimeline ]
        self.dbTableNames = None
        self.dbRpdrTableNames = None
        self.dbRpdrTables = None
        self.dbTimelineTableNames = None
        self.dbTimelineTables = None
        self.demographics = None
        self.timelineTableNames = None

        # connect to SQLite database and enable dictionary access of rows
        self.dbCon = sqlite3.connect(self.dbPath)
        self.dbCon.row_factory = sqlite3.Row
    
        # get list of tables in database
        with self.dbCon:
            dbCur = self.dbCon.cursor()
            dbCur.execute( "SELECT name FROM sqlite_master WHERE type='table'" )
            qResult = dbCur.fetchall()
            if qResult is None:
                print " Error: No tables in database."
                return
            else:
                self.dbTableNames = [str(row[0]) for row in qResult]
    
        # get list of RPDR tables in given database
        self.dbRpdrTableNames = [ n for n in self.dbTableNames if n in self.possibleRpdrTableNames ]
        self.dbRpdrTables = [ t for t in rpdrtables.Tables if t.name in self.dbRpdrTableNames ]
        
        # check that there are rpdr tables in given database
        if len(self.dbRpdrTableNames) < 1:
            print " Error: No RPDR tables found in database."
            
        # get list of RPDR tables in database to use in self.timeline()
        self.dbTimelineTableNames = [ n for n in self.dbTableNames if n in self.possibleTimelineTableNames ]
        self.dbTimelineTables = [ t for t in rpdrtables.Tables if t.name in self.dbTimelineTableNames ]

        # search for basic patient demographics
        with self.dbCon:
            dbCur = self.dbCon.cursor()
            dbCur.execute( "SELECT * FROM Dem WHERE EMPI=? LIMIT 1", (empi,) )
            qResult = dbCur.fetchone()
            if qResult is None:
                print " Error: Couldn't find patient in Dem with EMPI = %s." % empi
                return
            self.demographics = qResult
        
        ## find number of events belonging to this patient in each table accept the Mrn table
        #with self.dbCon:
        #    dbCur = self.dbCon.cursor()
        #    for tableName in [ n for n in self.dbRpdrTableNames if n != 'Mrn' ]:
        #        dbCur.execute( "SELECT count(*) FROM %s WHERE EMPI=?" % tableName, (empi,) )
        #        qResult = dbCur.fetchone()
        #        if qResult is None:
        #            print " No events found in '%s'" % tableName
        #        else:
        #            print " Found %d events in '%s' table" % (qResult[0],tableName)




    #--------------------------------------------------------------------------------------------
    def timeline( self, tables='' ):

        # determine tables to search
        if tables:
            timelineTables = [ t for t in self.dbTimelineTables if t.name in tables ]
            if not timelineTables:
                print "Error: Provided timeline tables are invalid ( %s )" % tables
                return
        else:
            timelineTables = self.dbTimelineTables
        
        # create SQL search query
        tablesSearchQueries = []
        for table in timelineTables:
            dateColName = None
            blurbColName = None
            for col in table.columns:
                if col.timelineDate:
                    dateColName = col.name
                if col.timelineBlurb:
                    blurbColName = col.name
            q = "SELECT '%s' AS 'Table', rowid AS EventId, %s AS Date, round( ( ( julianday(%s) - julianday('%s') ) / 365 ), 2 ) AS Age, %s AS Blurb FROM %s WHERE EMPI = %s" \
                % (table.name, dateColName, dateColName, self.demographics['Date_of_Birth'], blurbColName, table.name, self.empi )
            tablesSearchQueries.append(q)
        qSearch = "Select * From ( %s ) ORDER BY Date" % " UNION ".join(tablesSearchQueries)

        # query database
        events = None
        with self.dbCon:
            dbCur = self.dbCon.cursor()
            dbCur.execute( qSearch )
            qResult = dbCur.fetchall()
            if qResult is None:
                print " Error: Search query failed."
                return
            events = qResult

        # print events
        print " _______________________________________________________________________________________________\n |"
        print " | Timeline: %s" % str(tables)
        print " |----------------------------------------------------------------------------------------------"
        print " |Table\t|Event \t|Date \t\t|Age \t|Blurb"
        print " |----------------------------------------------------------------------------------------------"
        print " |Dem \t|1 \t|%s \t|0.00 \t|Birth Date" % self.demographics['Date_of_Birth']
        for event in events:
            if len(event['Blurb']) > 50:
                blurb = "%s..." % event['Blurb'][:50]
            else:
                blurb = event['Blurb']
            print " |%s \t|%s \t|%s \t|%s \t|%s" % (event['Table'], str(event['EventId']), event['Date'], str(event['Age']), blurb )
        if self.demographics['Date_of_Death']:
            print " |Dem \t|1 \t|%s \t|    \t|Birth Date" % self.demographics['Date_of_Birth']
        print " |______________________________________________________________________________________________\n"




    #--------------------------------------------------------------------------------------------
    def event( self, table, event ):

        # validate args
        if table:
            table = [ t for t in self.dbRpdrTables if t.name in table ][0]
        else:
            print "Error: Can't find '%s' table!"
            return
        if not event:
            print "Error: Must provide event id!"
            return

        # search for event
        qResult = None
        with self.dbCon:
            dbCur = self.dbCon.cursor()
            dbCur.execute( "SELECT * FROM %s WHERE EMPI = ? AND rowid = ? LIMIT 1" % table.name, (self.empi,event) )
            qResult = dbCur.fetchone()
            if qResult is None:
                print " Error: Search query failed."
                return
        eventCols = [c for c in qResult]

        # determine spacing after name
        colLength = 0
        for col in table.columns:
            if len(col.name) > colLength:
                colLength = len(col.name)
        
        print " _______________________________________________________________________________________________\n |"

        # print table name
        spacing = ''.join([ ' ' for i in xrange(colLength - len("Table")) ])
        print " |Table:%s %s" % (spacing, table.name)

        # account for last column containing a free-text report
        spacing = "|%s" % ''.join([ ' ' for i in xrange(colLength+1) ])
        eventCols[len(eventCols)-1] = eventCols[len(eventCols)-1].replace('\n', '\n %s ' % spacing)

        # print columns
        for cIdx, col in enumerate(table.columns):
            spacing = ''.join([ ' ' for i in xrange(colLength - len(col.name)) ])
            print " |%s:%s %s" % (col.name, spacing, eventCols[cIdx])

        print " |______________________________________________________________________________________________\n"









