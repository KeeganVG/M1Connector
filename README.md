# M1Connector
Python tool for connecting to M1's database ( MS-SQL )

## Installation

Install from PyPi using

`$ python3 -m pip install m1connector`

## Requirements

In addition to basic python packages this repo uses...

- pyodbc
- ODBC Driver 17 for SQL Server

## Usage

Begin by creating an M1Connector object. The object expects 4 positional arguments...

`host` - The network location of the mysql db

`db` - The target database on the host

`usr` - The User to connect as

`pswd` - Pass

The object also accepts the optional keyword arguement

`driver` - The driver used to facilitate the connection if other than "ODBC Driver 17 for SQL Server"

    from m1connector import M1Connector
    
    # Create the connection
    m1 = M1Connector(host, db, usr, pswd)

    # Execute a sql query, does NOT commit
    m1.execute(query)

    # Get one result
    m1.fetchone()

    # Get all results
    m1.fetchall()

    # Commit to the database
    m1.commit()







