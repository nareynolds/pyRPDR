rpdr.py
=======

Intended audience:
These modules were written to help in the exploration, organization, and management of a RPDR data.

Intended use:
This reads known RPDR data text files, and records it into an SQLite database.
This shows the timeline of RPDR events from a specific patient.
This allows you to record notes about each patient into the same database.

Details:
This was written for Python 2.7.X
This relies on sqlite3 ( https://docs.python.org/2/library/sqlite3.html ) extensively.
The default location of the SQLite database is the directory of the RPDR data.
The format of known RPDR tables are defined in the file "rpdrdefs.py"
Warning: the format of the text files returned by the RPDR are frequently changed.
All common use cases are presented in the file "examples.py"

Have fun!