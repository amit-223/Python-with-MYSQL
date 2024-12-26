#this is a main code for connection which we write in classes.

import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='root',
                                     database='student')
        query = 'create table if not exists user(id int primary key, name varchar(200),phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        # print("created")

DBHelper() 