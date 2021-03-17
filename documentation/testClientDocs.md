# SQLite Test Client Documentation

## Table of Contents
- [SQLite Test Client Documentation](#sqlite-test-client-documentation) 
- [Directory Tree](#directory-tree)
- [Installation Instructions](#installation-instructions) 
- [```globals.py```](#globalspy)   
  - [ext](#ext)   
  - [insertOrder](#insertorder)   
  - [create](#create)   
  - [databaseName](#databasename)   
  - [queries](#queries)   
  - [databaseFilePath](#databasefilepath)   
  - [createPath](#createpath)   
  - [insertPath](#insertpath)   
  - [selectPath](#selectpath)   
  - [outputFile](#outputfile) 
- [```testClient.py```: TestClient Class](#testclientpy-testclient-class)   
  - [```TestClient.TestClient()```](#testclienttestclient)   
  - [```TestClient.close()```](#testclientclose)   
  - [```TestClient.refreshDb()```](#testclientrefreshdb)   
  - [```TestClient.freshPopulateDb()```](#testclientfreshpopulatedb)   
  - [```TestClient.dropAll()```](#testclientdropall)   
  - [```TestClient.createAll()```](#testclientcreateall)   
  - [```TestClient.insertAll()```](#testclientinsertall)   
  - [```TestClient.queryAll(printResult=0:boolean)```](#testclientqueryallprintresult0boolean)   
  - [```TestClient.testFile(filePath:string)```](#testclienttestfilefilepathstring) 
  - [```testClient.py```: Database Class](#testclientpy-database-class)   
  - [```Database.Database(filePath:string)```](#databasedatabasefilepathstring)   
  - [```Database.execute(SqlScript:string)```](#databaseexecutesqlscriptstring)   
  - [```Database.insertMany(tableName:string, listOfTuplesToAdd:list)```](#databaseinsertmanytablenamestring-listoftuplestoaddlist)   
  - [```Database.executeScript(SqlScript:string)```](#databaseexecutescriptsqlscriptstring)   
  - [```Database.close()```](#databaseclose)  
  - [```Database.getAllTables()```](#databasegetalltables)


## Directory Tree
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
[Back to Top](##table-of-contents)


## Installation Instructions
1. Run ```testClient.py``` for an example of what this program does
1. Modify ```main()``` as desired to see if the program is right for your purposes
1. Replace all the example ```.sql``` files with your own content.  
*NOTE: The feedback given by the TestClient is more clear when files have meaningful names.* 
1. Navigate to ```src/globals.py```
1. Update variable values to fit your files and queries
1. Navigate to ```src/testClient.py``` and update ```main()``` to perform the desired operations
1. Run ```testClient.py``` from the terminal
1. If there is functionality you desire or if you have any questions, [contact the author](https://www.linkedin.com/in/keziahmay/)!  

[Back to Top](##table-of-contents)


## ```globals.py``` 
This file contains the variables that control the actions of the TestClient class.  

[Back to Top](##table-of-contents)

### ext
The file extension for all files containing SQLite script to be run by this program. Most likely, the value should be '.sql'.  

[Back to Top](##table-of-contents)

### insertOrder
A list of file names (no path or extension) for insertion scripts in the order they must be executed. If you do not know what order you should populate your tables, consider starting from the table with the fewest foreign keys. If your files seem to insert in any order without errors, check to see if you have foreign key constraints turned on. To turn on FK constraints, add ```pragma foreign_keys = 1``` to the top of each file. SQLite has this constraint turned off by default.  

[Back to Top](##table-of-contents)

### create
A map of table names (key) and the file name (value, no path or extension) of the file with their create statement. This assumes that each table has its own unique create statement file.  

[Back to Top](##table-of-contents)

### databaseName
This is the name by which you refer to your database. The value us never used for computing, it is only used for printing a report.   

[Back to Top](##table-of-contents)

### queries
This one is a little complicated, bear with me. This variable is a map connecting a tuple (key) to a list of tuples (value).  
The key-tuple has two values: 
- it has a file name (no path or extension) for a select statement  
i.e. ```"selectPlaceByName"```.
- it has a use case text in plain english describing the select statement  
i.e. ```"Query: list all places sorted by name."```

Then the key by this example would be the tuple of these values:  
```("selectPlaceByName", "Query: list all places sorted by name.")```

The value-list for this map is the expected return value of the select statement. It is formatted as a list of tuples where each tuple represents a returned row. If the return has columns:  
```LocationName | Street | City | State | Zip```  
you may recieve a return value like:  
```python
[
        ('Alensberb', '4322 happy st', 'Tacoma', 'WA', '98765'), 
        ('Elk Ridge', '1234 J st', 'Bellingham', 'WA', '98765'), 
        ('Juanita Beach', '1234 Happy st', 'Tacoma', 'WA', '98765'), 
        ("Low's Point", '1234 Jerril Way', 'Tacoma', 'WA', '98765')
]
```  

[Back to Top](##table-of-contents)

### databaseFilePath
The path, file name, and extension for your database file from the location of ```testClient.py```.  
i.e. ```"database/exampleDatabaseFile.db"```  

[Back to Top](##table-of-contents)

### createPath
The path to your create statement files from the location of ```testClient.py```.  
i.e. ```"create/"```  

[Back to Top](##table-of-contents)

### insertPath
The path to your insert statement files from the location of ```testClient.py```.  
i.e. ```"insert/"```  

[Back to Top](##table-of-contents)

### selectPath
The path to your select statement files from the location of ```testClient.py```.  
i.e. ```"query/"```  

[Back to Top](##table-of-contents)

### outputFile
The path, file name, and extension for your output file from the location of ```testClient.py```.  
i.e. ```"output/output.txt"```  

[Back to Top](##table-of-contents)

## ```testClient.py```: TestClient Class
This class provides automated database creation, testing, and SQLite script error reporting.  

[Back to Top](##table-of-contents)

### ```TestClient.TestClient()```
Connects to database (in ```globals.py```) and prints statements about actions taken. 

[Back to Top](##table-of-contents)
 
### ```TestClient.close()```
Closes database and prints statementa about actions taken. 

[Back to Top](##table-of-contents)
 
### ```TestClient.refreshDb()```
Calls ```self.dropAll()``` and ```self.createAll()```. 

[Back to Top](##table-of-contents)
 
### ```TestClient.freshPopulateDb()```
Calls ```self.dropAll()```, ```self.createAll()```, and ```self.insertAll()```. 

[Back to Top](##table-of-contents)
 
### ```TestClient.dropAll()```
Gets the name of each table currently in the database and drops each one (permanent deletion of all tables). Results are printed to the terminal. Supports error reporting and pass/fail reporting. 

[Back to Top](##table-of-contents)
 
### ```TestClient.createAll()```
Traverses the create files (in ```globals.py```) and creates each table in the database. Results are printed to the terminal. Supports error reporting and pass/fail reporting. 

[Back to Top](##table-of-contents)
 
### ```TestClient.insertAll()```
Traverses the insert files in the specified order (in ```globals.py```) and executes each insertion on the database. Results are printed to the terminal. 

[Back to Top](##table-of-contents)
 
### ```TestClient.queryAll(printResult=0:boolean)```
Traverses the map of queries (in ```globals.py```), executes each select statement, grabs the returned tuples, and compares them to the list of expected tuples in the map of queries (in ```globals.py```). Results are printed to the terminal. Supports error reporting, pass/fail reporting, and warnings if the correct tuples are returned in the wrong order.  

[Back to Top](##table-of-contents)
 
### ```TestClient.testFile(filePath:string)```
Runs the SQLite script in the given ```filePath```. The file is read line-by-line. When the program reaches a ';', the line is executed. Any errors are reported with the line that the ';' was found on, the script that was attempted, and a description of the error. 

[Back to Top](##table-of-contents)
 
## ```testClient.py```: Database Class
This class provides a simple interface with the Python Sqlite3 library.  

[Back to Top](##table-of-contents)
 
### ```Database.Database(filePath:string)```
Creates a connection with the database at the ```filePath``` and gets the cursor. 

[Back to Top](##table-of-contents)
 
### ```Database.execute(SqlScript:string)```
Executes a single SQL statement, ```SqlScript```. 

[Back to Top](##table-of-contents)
 
### ```Database.insertMany(tableName:string, listOfTuplesToAdd:list)```
Given a ``listOfTuplesToAdd`` which is a list of tuples, and a ```tableName``` which is a string, this function inserts all the tuples into the table in the database. For this to execute successfully, the table must exist in the database and the tuples must have a value for each column. 

[Back to Top](##table-of-contents)
 
### ```Database.executeScript(SqlScript:string)```
Executes multiple SQL statements, ```SqlScript```. 

[Back to Top](##table-of-contents)
 
### ```Database.close()```
Closes the database. 

[Back to Top](##table-of-contents)
 
### ```Database.getAllTables()```
Returns a list of the names of all tables currently in the database. 

[Back to Top](##table-of-contents)
 
