from flask import g

import sqlite3


def connect_database():
    sql = sqlite3.connect('C:/Users/Asus/Desktop/Projects/student_flask/students.db')   
    sql.row_factory = sqlite3.Row
    return sql


def get_database():
    if not hasattr(g, 'crudapplication_db'):
        g.crudapplication_db = connect_database() 

    return g.crudapplication_db
