# rpdrtables.py

'''
*****************************************************
Example use:


*****************************************************
'''




# get csv tools
from csv import QUOTE_NONE

# get namedtuple
from collections import namedtuple


#--------------------------------------------------------------------------------------------
# define RPDR table column foreign key reference
ForeignKeyRef = namedtuple('ForeignKeyRef','table column')

# define RPDR table column date/time reformat map
DateReformat = namedtuple('DateReformat','format reformat')
SQLITE_DATE_FORMAT = '%Y-%m-%d'

# define RPDR table column
TableColumn = namedtuple('TableColumn','name type primaryKey index unique notNull foreignKeyRef dateReformat timelineDate timelineBlurb')

# define RPDR csv dialect and some standards
CsvDialect = namedtuple('CsvDialect','delimiter doublequote escapechar lineterminator quotechar quoting skipinitialspace strict')

StandardCsvDialect = CsvDialect(
    delimiter = '|',
    doublequote = True,
    escapechar = None,
    lineterminator = '\r\n',
    quotechar = '',
    quoting = QUOTE_NONE,
    skipinitialspace = True,
    strict = False
)

# define RPDR table
Table = namedtuple('Table', 'name fileExt columns csvDialect freeTextReportInLastColumn useInTimeline')



#--------------------------------------------------------------------------------------------
# define Car RPDR table
Car = Table(
    name = 'Car',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = True,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %I:%M:%S %p', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Report_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Con RPDR table
Con = Table(
    name = 'Con',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = False,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    True,
            index =         False,
            unique =        True,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Last_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "First_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Middle_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Address1",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Address2",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "City",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "State",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Zip",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Country",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Home_Phone",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Day_Phone",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "SSN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "VIP",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Previous_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Patient_ID_List",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Insurance_1",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Insurance_2",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Insurance_3",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Primary_Care_Physician",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Resident_Primary_Care_Physician",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Dem RPDR table
Dem = Table(
    name = 'Dem',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = False,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    True,
            index =         False,
            unique =        True,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Gender",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Date_of_Birth",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Age",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Language",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Race",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Marital_status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Religion",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Is_a_veteran",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Zip_code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Country",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Vital_status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Date_Of_Death",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Dia RPDR table
Dia = Table(
    name = 'Dia',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Date",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Diagnosis_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Code_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_Flag",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Provider",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Clinic",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Hospital",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Inpatient_Outpatient",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Encounter_number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Dis RPDR table
Dis = Table(
    name = 'Dis',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = True,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %I:%M:%S %p', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Report_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Dpt RPDR table
Dpt = Table(
    name = 'Dpt',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = True,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %I:%M:%S %p', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Report_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Enc RPDR table
Enc = Table(
    name = 'Enc',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Encounter_number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Encounter_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Hospital",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Inpatient_Outpatient",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Service_Line",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Attending_MD",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Admit_Date",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Discharge_Date",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Clinic_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Admit_Source",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Discharge_Disposition",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Payor",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Admitting_Diagnosis",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Principle_Diagnosis",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_1",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_2",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_3",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_4",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_5",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_6",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_7",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_8",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_9",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Diagnosis_10",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "DRG",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Patient_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Referrer_Discipline",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define End RPDR table
End = Table(
    name = 'End',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = True,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %I:%M:%S %p', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Report_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Lab RPDR table
Lab = Table(
    name = 'Lab',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Seq_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %H:%M', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Group_Id",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Loinc_Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Test_Id",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Test_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Result",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Result_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Abnormal_Flag",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Reference_Units",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Reference_Range",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Toxic_Range",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Specimen_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Specimen_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Correction_Flag",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Test_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Ordering_Doc_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Accession",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Source",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Lhm RPDR table
Lhm = Table(
    name = 'Lhm',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "System",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "LMR_Health_Maintenance_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %H:%M', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "LMR_Text_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "LMR_Code_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Result",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Result_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Comments",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Lme RPDR table
Lme = Table(
    name = 'Lme',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "LMR_Medication_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %H:%M', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "LMR_Text_Med_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Generic_ID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Rollup_ID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "LMR_Code_Med_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Med_ID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Med_Freq",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Med_Route",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Dose",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Units",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Take_Dose",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Take_Units",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Dispense",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Dispense_Units",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Duration",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Duration_Units",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Refills",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "PRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Rx",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "No_Substitutions",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Directions",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Comments",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Lno RPDR table
Lno = Table(
    name = 'Lno',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = True,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "LMRNote_Date",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %H:%M', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Record_Id",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Author",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "COD",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Institution",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Author_MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Subject",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Comments",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Lpr RPDR table
Lpr = Table(
    name = 'Lpr',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "LMR_Problem_Date",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "LMR_Text_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Concept_ID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "LMR_Code_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Comments",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Onset_Date",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Resolution_Date",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Procedure_Date",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Modifiers",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Acuity",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Severity",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Condition",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Sensitivity_Flag",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Location",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Lvs RPDR table
Lvs = Table(
    name = 'Lvs',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "LMR_Vital_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %H:%M', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "LMR_Text_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "LMR_Code_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Result",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Units",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Site",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Position",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Rythm",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Med RPDR table
Med = Table(
    name = 'Med',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Medication_Date",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Medication",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Code_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Quantity",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Provider",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Clinic",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Hospital",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Inpatient_Outpatient",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Encounter_number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Mic RPDR table
Mic = Table(
    name = 'Mic',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = True,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Microbiology_Number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Microbiology_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %H:%M:%S', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Specimen_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Specimen_Comments",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Test_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Test_Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Test_Comments",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Test_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Organism_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Organism_Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Organism_Comment",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Organism_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Mrn RPDR table
Mrn = Table(
    name = 'Mrn',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = False,
    columns=[
        TableColumn(
            name =          "IncomingId",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "IncomingSite",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Enterprise_Master_Patient_Index",
            type =          "TEXT",
            primaryKey =    True,
            index =         False,
            unique =        True,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MGH_MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "BWH_MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "FH_MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "SRH_MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "NWH_MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "NSMC_MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MCL_MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Opn RPDR table
Opn = Table(
    name = 'Opn',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = True,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %I:%M:%S %p', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Report_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Pal RPDR table
Pal = Table(
    name = 'Pal',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "System",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "PEARAllergy_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %H:%M:%S', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Allergen",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Allergen_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Allergen_Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Reaction",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Comments",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Pat RPDR table
Pat = Table(
    name = 'Pat',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = True,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %I:%M:%S %p', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Report_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Phy RPDR table
Phy = Table(
    name = 'Phy',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Date",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Concept_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Code_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Result",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Units",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Provider",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Clinic",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Hospital",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Inpatient_Outpatient",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Encounter_number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Prc RPDR table
Prc = Table(
    name = 'Prc',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Date",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Procedure_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Code_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Procedure_Flag",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Quantity",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Provider",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Clinic",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Hospital",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Inpatient_Outpatient",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Encounter_number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Prv RPDR table
Prv = Table(
    name = 'Prv',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Provider_Rank",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Is_PCP",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Last_Seen_Date",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Provider_Name",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Provider_ID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Address_1",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Address_2",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "City",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "State",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Zip",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Phone_Ext",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Fax",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "EMail",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Specialties",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Enterprise_service",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "CPM_Id",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Pul RPDR table
Pul = Table(
    name = 'Pul',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = True,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %I:%M:%S %p', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Report_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Rad RPDR table
Rad = Table(
    name = 'Rad',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = True,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MID",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Date_Time",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y %I:%M:%S %p', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Report_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Status",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Report_Text",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Rdt RPDR table
Rdt = Table(
    name = 'Rdt',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = True,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Date",
            type =          "DATETIME",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  True,
            timelineBlurb = False,
            dateReformat =  DateReformat( format='%m/%d/%Y', reformat=SQLITE_DATE_FORMAT )
        ),
        TableColumn(
            name =          "Mode",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Group",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Test_Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Test_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = True,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Accession_Number",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Provider",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Clinic",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Hospital",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Inpatient_Outpatient",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)



#--------------------------------------------------------------------------------------------
# define Rnd RPDR table
Rnd = Table(
    name = 'Rnd',
    fileExt = 'txt',
    csvDialect = StandardCsvDialect,
    freeTextReportInLastColumn = False,
    useInTimeline = False,
    columns=[
        TableColumn(
            name =          "EMPI",
            type =          "TEXT",
            primaryKey =    False,
            index =         True,
            unique =        False,
            notNull =       True,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN_Type",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "MRN",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Accession",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Deptartment",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Exam_Code",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "History1",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "History2",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "History3",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Long_Description",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Rad1",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Rad2",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Rad3",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Req",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Division",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Region",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Specialty",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "Body_Part",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        ),
        TableColumn(
            name =          "FileName",
            type =          "TEXT",
            primaryKey =    False,
            index =         False,
            unique =        False,
            notNull =       False,
            foreignKeyRef = None,
            timelineDate =  False,
            timelineBlurb = False,
            dateReformat =  None
        )
    ]
)




#--------------------------------------------------------------------------------------------
# list of RPDR tables to consider

Tables = [
    Car,
    Con,
    Dem,
    Dia,
    Dis,
    Dpt,
    Enc,
    End,
    Lab,
    Lhm,
    Lme,
    Lno,
    Lpr,
    Lvs,
    Med,
    Mic,
    Mrn,
    Opn,
    Pal,
    Pal,
    Pat,
    Phy,
    Prc,
    Prv,
    Pul,
    Rad,
    Rdt,
    Rnd
]

