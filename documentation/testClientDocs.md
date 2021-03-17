# SQLite Test Client Documentation

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

## ```globals.py``` 

### ext
The file extension for all files containing SQLite script to be run by this program. Most likely, the value should be '.sql'.

### insertOrder
A list of file names (no path or extension) for insertion scripts in the order they must be executed. If you do not know what order you should populate your tables, consider starting from the table with the fewest foreign keys. If your files seem to insert in any order without errors, check to see if you have foreign key constraints turned on. To turn on FK constraints, add ```pragma foreign_keys = 1``` to the top of each file. SQLite has this constraint turned off by default.

### create
A map of table names (key) and the file name (value, no path or extension) of the file with their create statement. This assumes that each table has its own unique create statement file.

### databaseName
This is the name by which you refer to your database. The value us never used for computing, it is only used for printing a report. 

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
### databaseFilePath
The path, file name, and extension for your database file from the location of ```testClient.py```.  
i.e. ```"database/exampleDatabaseFile.db"```

### createPath
The path to your create statement files from the location of ```testClient.py```.  
i.e. ```"create/"```

### insertPath
The path to your insert statement files from the location of ```testClient.py```.  
i.e. ```"insert/"```

### selectPath
The path to your select statement files from the location of ```testClient.py```.  
i.e. ```"query/"```

### outputFile
The path, file name, and extension for your output file from the location of ```testClient.py```.  
i.e. ```"output/output.txt"```

## ```testClient.py```: TestClient Class
This class provides automated database creation, testing, and SQLite script error reporting.
### ```TestClient.TestClient()```
Connects to database (in ```globals.py```) and prints statements about actions taken.
### ```TestClient.close()```
Closes database and prints statementa about actions taken.
### ```TestClient.refreshDb()```
Calls ```self.dropAll()``` and ```self.createAll()```.
### ```TestClient.freshPopulateDb()```
Calls ```self.dropAll()```, ```self.createAll()```, and ```self.insertAll()```.
### ```TestClient.dropAll()```
Gets the name of each table currently in the database and drops each one (permanent deletion of all tables). Results are printed to the terminal. Supports error reporting and pass/fail reporting.
### ```TestClient.createAll()```
Traverses the create files (in ```globals.py```) and creates each table in the database. Results are printed to the terminal. Supports error reporting and pass/fail reporting.
### ```TestClient.insertAll()```
Traverses the insert files in the specified order (in ```globals.py```) and executes each insertion on the database. Results are printed to the terminal.
### ```TestClient.queryAll(printResult=0:boolean)```
Traverses the map of queries (in ```globals.py```), executes each select statement, grabs the returned tuples, and compares them to the list of expected tuples in the map of queries (in ```globals.py```). Results are printed to the terminal. Supports error reporting, pass/fail reporting, and warnings if the correct tuples are returned in the wrong order. 
### ```TestClient.testFile(filePath:string)```
Runs the SQLite script in the given ```filePath```. The file is read line-by-line. When the program reaches a ';', the line is executed. Any errors are reported with the line that the ';' was found on, the script that was attempted, and a description of the error.
## ```testClient.py```: Database Class
This class provides a simple interface with the Python Sqlite3 library. 
### ```Database.Database(filePath:string)```
Creates a connection with the database at the ```filePath``` and gets the cursor.
### ```Database.execute(SqlScript:string)```
Executes a single SQL statement, ```SqlScript```.
### ```Database.insertMany(tableName:string, listOfTuplesToAdd:list)```
Given a ``listOfTuplesToAdd`` which is a list of tuples, and a ```tableName``` which is a string, this function inserts all the tuples into the table in the database. For this to execute successfully, the table must exist in the database and the tuples must have a value for each column.
### ```Database.executeScript(SqlScript:string)```
Executes multiple SQL statements, ```SqlScript```.
### ```Database.close()```
Closes the database.
### ```Database.getAllTables()```
Returns a list of the names of all tables currently in the database.
