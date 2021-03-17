# SQLiteTestClient

## License
MIT License

Copyright (c) 2021 Keziah May

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## How To Use 
This program provides an easy to use testing interface for SQLite3 scripts using Python 3.8.3.

### File Organization
```
SQLiteTestClient/
    documentation/
        testClientDocs.md
    src/
        analyze/
            oneLongFile.sql
        create/
            create1.sql
            create2.sql
            create3.sql
        database/
            exampleDatabaseFile.db
        insert/
            insert1.sql
            insert2.sql
            insert3.sql
        output/
            output.txt
        query/
            selectUC1.sql
            selectUC2.sql
            selectUC3.sql
        globals.py
        testClient.py
    .gitignore
    LICENSE
    README.md
```

### Installation
Open the globals.py file and change all the global variables to match your database's file organization. Update textClient.py main() function to complete the desired operations. Then, run testClient.py. To learn about the operations performed by this program, read the "Functionality" section. 

### Functionality
Using this program, you can drop all the tables in a SQLite database, create tables from a directory of create files, populate the database from a directory of insert files, test a series of queries from a directory of queries, and find the location of a bug in a SQLite script. 

#### Run Standard Tests with Output
To drop, create, populate, and test queries on your table, follow the installation instructions and paste this into main:
```python
  testDb = TestClient()    # open the database
  testDb.freshPopulateDb() # drops all tables, recreates all tables, populates all tables
  testDb.queryAll()        # run all select statements, compare results to expected results
  testDb.close()           # close the database
```
The terminal will display a report describing actions attemped by the TestClient and the success ratio.  
![image](https://user-images.githubusercontent.com/45299665/111353491-9888d580-8642-11eb-9258-1ed14c436b26.png)

Any errors along the way will be reported to the terminal as they happen.  
![image](https://user-images.githubusercontent.com/45299665/111358181-4d24f600-8647-11eb-859c-056d250a1c31.png)

Similarly, any queries that return a result that is different than what was listed as expected in globals.py will be reported to the terminal.  
![image](https://user-images.githubusercontent.com/45299665/111354164-3e3c4480-8643-11eb-8eb1-f0733e0c3741.png)

If any returned results have all the right tuples but in the wrong order, they will be listed as a passed test, but a warning will print to the terminal.   
![image](https://user-images.githubusercontent.com/45299665/111354416-88252a80-8643-11eb-9435-bff30cc3fd85.png)

For nicely formated query results, locate output.txt. It will be populated with Use-Case text followed by the results of the query.  
![image](https://user-images.githubusercontent.com/45299665/111354728-d89c8800-8643-11eb-84d2-31b315a2c1e0.png)

These can also be printed to the terminal if in main, you pass the boolean value 'True' as an argument to queryAll().  
![image](https://user-images.githubusercontent.com/45299665/111355076-3f21a600-8644-11eb-8a2b-d50b1e55998e.png)

#### Execute and Evaluate a SQLite File for Debugging Purposes
To run a file full of sqlite3 script with line-by-line parsing and error reporting that points out the errors' location to the specific command and approximate line number, follow the installation instructions and add the following to main:
```python
  tFile =                  # <insert the filepath to your sql file here as a string>
  testDb = TestClient()    # open the database
  testDb.testFile(tFile)   # run the script in tFile with error reporting
  testDb.close()           # close the database
```
NOTE: If your tFile expects an existing database, follow these instructions:
- if you need all tables dropped, call   
```testDb.dropAll()```
- if you need all tables created, call  
```testDb.createAll()```
- if you need all tables dropped AND created, call  
```testDb.refreshDb()``` instead of dropAll and createAll
- if you need all tables populated, call  
```testDb.insertAll()```
- if you need all tables dropped AND created AND populated, call  
```testDb.freshPopulatedDb()``` instead of dropAll, createALL, and insertALL

The output of this program will print to the terminal as follows:
![image](https://user-images.githubusercontent.com/45299665/111374494-6aaf8b00-865a-11eb-88c1-8b5725fcf1f8.png)
