from delete import Delete
from fetch import fetch_all

class update_user(Delete):
    def upd(self, id, name, phone):
        query="update user set name='{}', phone='{}' where id={}".format(name,phone,id)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("updated")

helper = update_user()
# helper.upd(15,"Karmakar","88171")
# helper.fetch_user()