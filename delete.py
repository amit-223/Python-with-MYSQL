# from test import DBHelper
from fetch import fetch_all

class Delete(fetch_all):
    def delete_user(self, id):
        query="delete from user where id={}".format(id)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

h= Delete()
# h.delete_user(16)
# h.fetch_user()