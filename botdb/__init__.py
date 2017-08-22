import os
import sqlite3
from shared import *

dbfile = 'botdb/members.db'
schemafile = 'botdb/members_schema.sql'
initialdata = 'botdb/initial_data_schema.sql'

dbisnew = not os.path.exists(dbfile)
conn = sqlite3.connect(dbfile)

def exec_schemafile(connection, file):
    with open(file, 'rt') as f:
        schema = f.read()
        conn.executescript(schema)

def _getmember(member):
    member = str(member)
    with sqlite3.connect(dbfile) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        select * from member
        where name=:member
        """, {"member": member})
        result = cursor.fetchone()
        if result is not None:
            name, rela, nick = result
            return memberdata(name, rela, nick)
        else:
            return None

def _addmember(member, relationship = 'neutral', nickname = None):
    member = str(member)
    with sqlite3.connect(dbfile) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        insert into member (name, relationship, nickname)
        values (:name, :rela, :nick)
        """, {"name": member, "rela": relationship,"nick": nickname})

def _updatemember(member, relationship = None, nickname = None):
    member = str(member)
    with sqlite3.connect(dbfile) as conn:
        if relationship is not None:
            cursor = conn.cursor()
            cursor.execute("""
            update member set relationship = :rela where name=:name
            """, {"name": member, "rela": relationship})

        if nickname is not None:
            cursor = conn.cursor()
            cursor.execute("""
            update member set nickname = :nick where name=:name
            """, {"name": member,"nick": nickname})
    return

def findmember(member):
    return _getmember(member)

def editmember(member, relationship = 'neutral', nickname = None):
    memdata = _getmember(member)
    if memdata is not None:
        _updatemember(member, relationship, nickname)
    else:
        _addmember(member, relationship, nickname)

def editmemberval(member, key, value):
    pass

def getmemberval(member, key):
    pass

#Main
with sqlite3.connect(dbfile) as conn:
    if dbisnew:
        print('Creating schema')
        exec_schemafile(conn, schemafile)

        print('Inserting initial data')
        exec_schemafile(conn, initialdata)
    else:
        print('Database exists, assume schema does too')
