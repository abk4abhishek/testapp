import sqlite3
import os
import os.path
import ctypes
from flask import g

def db_connect(app):
    databaseFile = app.config['DATABASE_URL']
    sqlFile = app.config['DATABASE_SCHEMA']
    conn = sqlite3.connect(databaseFile)
    return conn

def db_close(conn):
    conn.close()
    return 0

def db_init(app):
    databaseFile = app.config['DATABASE_URL']
    sqlFile = app.config['DATABASE_SCHEMA']

    # Delete the old table
    if os.path.isfile(databaseFile):
        os.remove(databaseFile)

    # Create the tables
    qry = open(sqlFile, 'r').read()
    sqlite3.complete_statement(qry)
    conn = db_connect(app)
    cursor = conn.cursor()
    try:
        cursor.executescript(qry)
        conn.commit()
        print ("DB initialize successfully")
    except Exception as e:
        MessageBoxW = ctypes.windll.user32.MessageBoxW
        errorMessage = databaseFile + ': ' + str(e)
        MessageBoxW(None, errorMessage, 'Error', 0)
        cursor.close()
        conn.rollback()
        raise
    finally:
        db_close(conn)

def db_add_data(app,values):
    conn=db_connect(app)
    print ("Opened database successfully")
    q="INSERT INTO TESTSTEPS (URL,METHOD,DETAIL) VALUES (?,?,?)"
    conn.execute(q,(values))
    conn.commit()
    print ("Records created successfully")
    db_close(conn)