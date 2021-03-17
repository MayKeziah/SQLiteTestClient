# globals.py
'''
LICENSE:
MIT License

Copyright (c) 2021 Keziah May

Permission is hereby granted, free of charge, to any person obtaining a copy of this 
software and associated documentation files (the "Software"), to deal in the Software 
without restriction, including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in all copies 
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# ABOUT
'''
A list of variables relating to a SQLite3 database. 

This file is designed to be accompanied by a testing program (testClient.py) 
that uses the variables contained in this file (globals.py) to run a series 
of tests on SQLite files. 

This program is written in python 3.8.3 and is written to accompany an interface 
(testClient.py) for sqlite3.

INSTALLATION: Change all the global variables to match your database's file organization. 
Place testClient.py and globals.py in the locations of your choosing and update the 
import statement for globals.py in testClient.py to match. 
Then, run testClient.py. To control what testClient.py does on run, consult the README.md
in this repository (github.com/MayKeziah/SQLiteTestClient).

AUTHOR: Keziah May (linkedin.com/in/keziahmay/)

'''

# File extention of all files to be executed (usually .sql)
ext = ".sql"

# Insert-file names (no path or extensions)
insertOrder = ["insert1", "insert2", "insert3"]

# Table name to create-file name mapping (no path or extensions)
create = {
  "PLACE": "create1",
  "PROJECT": "create2",
  "PERSON": "create3"
}

# Name of database to display to user on testing screen
databaseName = "<Database Name>"

# Select-File names (no path or extensions) and use case text tuples mapped to expected selection results
# Format: 
#     {
#       ("filename", "UseCase Text"): 
#         [
#           ("expectedTuple1Col1", "expectedTuple1Col2"),
#           ("expectedTuple2Col1", "expectedTuple2Col2")
#         ]
#     }
queries = {
      ("selectUC1", 
      "Query: list all places, sort by name")
      : 
       [('Alensberb', '4322 happy st', 'Tacoma', 'WA', '98765'), 
        ('Elk Ridge', '1234 J st', 'Bellingham', 'WA', '98765'), 
        ('Juanita Beach', '1234 Happy st', 'Tacoma', 'WA', '98765'), 
        ("Low's Point", '1234 Jerril Way', 'Tacoma', 'WA', '98765')
       ],
      ("selectUC2", 
      "Query: list all projects, sort by location")
      : 
       [('Elk Ridge', 'Wedding', 'James', 'May', '2021-03-16'), 
        ('Elk Ridge', 'Race', 'Kathy', 'Dugolna', '2021-03-16'), 
        ('Juanita Beach', 'Race', 'James', 'May', '2021-03-13'), 
        ("Low's Point", 'Wedding', 'James', 'May', '2021-03-14')
       ],
      ("selectUC3", 
      "Query: list all places that projects are taking place at.")
      : 
       [('Juanita Beach',), 
        ('Elk Ridge',), 
        ("Low's Point",)
       ],       
       }

# PATH VARIABLES: 
#   The paths from your testClient.py to your sql files
#   Expects each table to have its own create path and 
#   that sql code is in a .<ext> file
databaseFilePath = "database/exampleDatabaseFile.db"
dropPath = "drop/"
createPath = "create/"
insertPath = "insert/"
selectPath = "query/"
outputFile = "output/output.txt"
