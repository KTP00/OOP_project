class Acount:
    def __init__(self, id , password, phonnumber, rank):
        self.id = id
        self.password = password
        self.phonnumber = phonnumber
        self.rank = rank
       
    def set_rank(self, rank):
        self.rank = rank


    def checklogin(self,id , password):
        if self.id != id or self.password != password:
            return False
        return True
        

       

class Admin(Acount):
    def __init__(self,id , password, phonnumber,  admin_name, email, rank="Admin"):
        super().__init__(id , password, phonnumber, rank)
        self.admin_name = admin_name
        self.email = email


class Member(Acount):
    def __init__(self,id , password, phonnumber,  admin_name, email, rank="Normal"):
        super().__init__(id , password, phonnumber, rank)
        self.admin_name = admin_name
        self.email = email





adminb = Admin("001","brawny","0805590976", "brawny", "kearttiyot@gmail.com")
adminp = Admin("002","phonnapa","0805590976",  "phonnapa", "phonnapa@gmail.com")


memdeef = Member("009f", "deef", "0805590976", "deef", "deffnapa@gmail.com" )


x = memdeef.checklogin("009f","deef")

print(x)
# print(adminp.rank)
