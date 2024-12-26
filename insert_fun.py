from connectionCode import DBHelper
 
class Insert_func(DBHelper):
    def inser_user(self,id,name,phone):
        query="insert into user(id,name,phone) values ({},'{}','{}')".format(id,name,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved")

helper = Insert_func()
# helper.inser_user(15,"amit","8770")
# helper.inser_user(16,"pratham","7799")
# helper.inser_user(17,"subal","5671")