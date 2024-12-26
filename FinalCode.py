#Phele we are creating database on mysql using cmd/powershell/workbench commands.
# ab hum python ke through database bana rhe hai.
#aur se sare database save rahenge backend mai.

#Project name-> creating Database application using python

from insert_fun import Insert_func
from fetch import fetch_all
from delete import Delete
from update import update_user

class DatabaseApp():
    def mainMethod(self):
        insObj = Insert_func()
        fetObj=fetch_all()
        delObj=Delete()
        upObj=update_user()

        while True:
            print("****Welcome****")
            print("P1 insert user")
            print("P2 fetch user")
            print("P3 delete user")
            print("P4 update user")
            print("P5 exit user")
            print()

            try:
                choice=int(input("Enter value.."))
                if choice==1:
                    id= int(input("id: "))
                    name=input("name: ")
                    phone=input("phone: ")
                    insObj.inser_user(id,name,phone)

                elif choice==2:
                    fetObj.fetch_user()

                elif choice==3:
                    id =int(input("which id do yo want to delete? "))
                    delObj.delete_user(id)

                elif choice==4:
                    id =int(input("updating id: "))
                    name=input("updating name: ")
                    phone=input("updating phone: ")
                    upObj.upd(id,name,phone)
                    
                elif choice==5:
                    break
                    
                else:
                    print("Invalid user..")
                    
            except Exception as e:
                print(e)
                print("Invaid details..")

obj = DatabaseApp()
obj.mainMethod()
