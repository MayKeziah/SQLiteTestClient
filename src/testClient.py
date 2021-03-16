# testClient.py
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
A simple class for automated testing and reporting on a sqlite database. 

This file is designed to be accompanied by a list of global variables (globals.py) 
that tell this file where to find the database and its files for 
creation, insertion, selection, etc. 

This program is written in python 3.8.3 and is written to interface with sqlite3.

INSTALLATION: Find the associated globals.py file and change all the global variables 
to match your database's file organization. Place testMaster.py globals.py 
in the locations of your choosing and update the import statement for globals.py in this file. 
Then, run this file (testMaster.py).

AUTHOR: Keziah May (linkedin.com/in/keziahmay/)

'''

import sqlite3 as sql
from globals import *

def main():
  testDb = TestClient()
  testDb.freshPopulateDb()

  testDb.queryAll()
  # To see nicely formatted queries and results, uncomment the following:
  # testDb.queryAll(1)

  # To see line-by line file parsing with error reporting, 
  # enter an error-ridden file for tFile and uncomment the following:
  # tFile = "analyze/oneLongFile.sql"
  # testDb.dropAll()
  # testDb.testFile(tFile)
  testDb.close()

  


# A class designed to assist in database testing by 
# dropping, creating, populating, and executing queries on the tables of a database. 
# All passed scripts are reported. Fails and errors are described. 
# Warnings pass but also report to the terminal.
class TestClient():
  def __init__(self):
    global databaseFilePath
    self.database = Database(databaseFilePath)
    print(">>> ", "STARTING TEST CLIENT")
    print(">>> ", databaseName, "opened")

  # Close the database
  def close(self):
    global databaseName
    self.database.close()
    print(">>> ", databaseName, "closed")
    print(">>> ", "END TEST CLIENT")

  # Drop and create the database tables
  def refreshDb(self):
    self.dropAll()
    self.createAll()

  # drop, create, and populate the database tables
  def freshPopulateDb(self):
    self.refreshDb()
    self.insertAll()

  # For each table in the database, drop it. Report errors and pass/fail count
  def dropAll(self):
    tables = self.database.getAllTables()
    count = 0
    dropText = "DROP TABLE "
    for table in tables:
      command = dropText + table
      try:
        self.database.execute(command)
        count += 1
      except sql.OperationalError as e:
        print(">>> ", "ERROR: in", command)
        print(">>> ", "DESCRIPTION: ", e)
  
    print(">>> ", count, "/", len(tables), " tables dropped")

  # Executes all create statements in the createPath files listed in globals.py
  def createAll(self):
    tables = self.database.getAllTables()
    global create
    global ext
    global createPath
    count = 0

    # For each create file in the create path, read the sql scripts and execute them. 
    # Report errors and pass/fail count
    for table in create:
      file = createPath + create[table] + ext
      if (not tables.count(table)):
        sqlFile = open(file, 'r')
        sqlScript = sqlFile.read()
        try:
          self.database.executeScript(sqlScript)
          count += 1
        except sql.OperationalError as e:
          print(">>> ", "ERROR: in", file)
          print(">>> ", "DESCRIPTION: ", e)    

    print(">>> ", count, "/", len(create), " tables created")

  # Executes all insert statements in insertPath files in the insertOrder specified in globals.py
  def insertAll(self):
    global insertPath
    global insertOrder
    global ext
    count = 0

    # For each file, read it and execute it. 
    # Report errors and pass/fail count
    for filename in insertOrder:
      file = insertPath + filename + ext
      sqlFile = open(file, 'r')
      sqlScript = sqlFile.read()
      try:
        self.database.executeScript(sqlScript)
        count+=1
      except sql.OperationalError as e:
        print(">>> ", "ERROR: in", file)
        print(">>> ", "DESCRIPTION: ", e)
        # break
    print(">>> ", count, "/", len(insertOrder), " tables populated")

  # Executes all queries located in the selectPath variable of globals.py
  def queryAll(self, printResult = 0):
    global outputFile
    global selectPath
    global queries
    global ext

    # Clear output file
    open(outputFile, 'w').close()

    # Open output file for appending
    formattedOutput = open(outputFile, 'a')
    count = 0
    for fileName, query in queries:
      # print(query)
      file = selectPath + fileName + ext
      matchingOrder = 1
      expected = queries[(fileName, query)]
      sqlFile = open(file, 'r')
      sqlScript = sqlFile.read()
      sqlFile.close()
      try:
        result = self.database.execute(sqlScript)
        # result = ""
        # self.testFile(file)
        string = query + "\n"
        
        # Generate formatted output, send to output file
        for row in result:
          string += "  " + str(row) + "\n"
        formattedOutput.write(string + "\n")

        # If user wants formatted results, print them. 
        if (printResult):
          print(string)

        # compare result of query to expected output
        if(not(result == expected)):
          matchingOrder = 0

        # print(">>> ", "EXPECTED: ")
        # print(expected)
        # print(">>> ", "RESULT: ")
        # print(result)
        # Compare to expected output when sorted (same tuples diff order?)
        origResult = result.copy()
        origExpected = expected.copy()        
        origResult.sort()
        origExpected.sort()
        if(origResult == origExpected):
          count+=1

          # Warining Message
          if(not matchingOrder):
            print(">>> ", "WARNING: ", file, "correct tuples, wrong order.")
        else:
          # Failed test message
          print(">>> ", "FAIL: ", file, "result != expected")
          print(">>> ", "RESULT: ")
          print(result)
          print(">>> ", "EXPECTED: ")
          print(expected)
      except sql.OperationalError as e:
        # SQL error message
        print(">>> ", "ERROR: in", file)
        print(">>> ", "DESCRIPTION: ", e)
        # break
    print(">>> ", count, "/", len(queries), " queries passed")

  # Use to test a file full of sql scripts. 
  # Each command from beginning to ';' must be in a single line.
  def testFile(self, file):
    print(">>> ", "Starting Analysis of", file)
    sqlFile = open(file, 'r')
    queries = sqlFile.readlines()
    ret = "RESULTS:\n"
    successful = 0
    # command = 0
    line = 0
    partialCommand = ""
    attempted = 0
    temp = ""

    # For each line of sql code
    while line < len(queries) - 1:     
      # This is a new line
      line += 1

      # does it end with ';'?
      if (self.eOfStatement(queries[line])):
        # This is the end of a command
        # command += 1
        partialCommand += queries[line]
      else:
        # This is part of a multi-line command, append until eof command
        partialCommand += queries[line]
        continue
      try:
        # If there is a line to execute, execute and print result
        if(len(partialCommand) > 1):
          temp = partialCommand
          partialCommand = ""
          attempted += 1
          result = self.database.execute(temp)
          if (len(result)):
            print(result)
          successful += 1
      except sql.OperationalError as e:
        # Print an error message
        ret = "---\n"
        ret += "ERROR: (" + str(e) + ") in " + file + " at or before line " + str(line) + ".\n"
        ret += "ATTEMPTED: \n" + temp 
        print(ret)
    print(str(successful) + "/" + str(attempted) + " queries executed successfully.")
    print()
    print(">>> ", file, "analysis complete")
    sqlFile.close()
    return ret
    
  # Is this the end of a statement? (does it end with ';*' where * = 0 or more ' ')
  def eOfStatement(self, string):
    if (not len(string)):
      return False
    i = len(string) - 1
    while(i >= 0 and (string[i] == ' ' or string[i] == '\n')):
      i -= 1
    return False if (i < 0) else string[i] == ';'

# A class designed to simplify interfacing with a sqlite3 database. 
class Database():
  def __init__(self, databasePath):
    self.db = sql.connect(databasePath)
    self.query = self.db.cursor()
  
  # Execute sql code
  def execute(self, string):
    # Execute script
    self.query.execute(string)

    # Fetch results (if any)
    result = self.query.fetchall()

    # Save (commit) the changes
    self.db.commit()

    # return results or []
    return result

  # given a table name and a list of tuples, insert all tuples. 
  # Expects all table values to be present in input tuples.
  def insertMany(self, table, list):
    string = "INSERT INTO " + table + " VALUES ("
    if len(list):
      for i in range(len(list[0]) - 1):
        string = string + "?,"
      string = string + "?)"
    self.query.executemany(string, list)
    self.db.commit()

  # Like execute but for multiple statements
  def executeScript(self, string):
    self.query.executescript(string)
    self.db.commit()
    return self.query.fetchall()

  # Close the database
  def close(self):
    self.db.close()

  # Get a list of the names of all tables in the database
  def getAllTables(self):
    self.query.execute("SELECT name FROM sqlite_master WHERE type='table';")
    result = self.query.fetchall()
    results_list = [item[0] for item in result]
    return results_list

main()