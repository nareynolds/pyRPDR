# examples.py


# import pyRPDR
import rpdr


# instantiate RPDR dataset
rpdrDir = "/path/to/directory/containing/RPDR/text/files"
ds = rpdr.Dataset()


# instantiate a patient
empi = '1234567'
p = rpdr.Patient( ds, empi )


# print patient's timeline
p.timeline()


# print patient's timeline for limited tables
tableNames = "Rdt Rad"
p.timeline( tableNames )


# look at particular event in patient's timeline
tableName = "Rad"
eventId = 1
p.event( tableName, eventId )


# record a note about patient
author = "Your Name"
note = "something noteable about this patient"
p.writeNote( author=author, note=note)


# print patient notes
p.printNotes()


# delete patient notes
noteIds = [1,2,3,4,5]
p.deleteNotes( noteIds )


