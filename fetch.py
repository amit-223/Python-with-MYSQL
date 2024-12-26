from insert_fun import Insert_func
class fetch_all(Insert_func):
    def fetch_user(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("id: ",row[0])
            print("name: ",row[1])
            print("phone: ",row[2])
            print()

helper = fetch_all()
# helper.fetch_user()
