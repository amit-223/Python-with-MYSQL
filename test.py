import mysql.connector as connector

con = connector.connect(host='localhost',port='3306',user='root',
                        password='root', database='student')
print(con)

# import mysql.connectorcls


# cnx = mysql.connector.connect(user='root', password='root',
#                               host='localhost',
#                               database='student')
# print(cnx)