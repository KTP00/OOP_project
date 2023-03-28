class Admin:
    def __init__(self,name, email):
        self.__name = name
        self.__email = email
        self.keep_coupon = []

    def add_coupon(self, coupon ):
        self.keep_coupon.append(coupon)
        print(self.keep_coupon)

    @property
    def get_coupon(self):
        return self.keep_coupon
    

    def delete_coupon(self,coupon):
        self.keep_coupon.remove(coupon)
        print(self.keep_coupon)



class Coupon:
    def __init__(self,code, percentage, datetime):
        self.code = code
        self.persentage = percentage
        self.datetime = datetime
        
    # def __str__(self):
    #     return "C: {} P: {} D: {}".format(self.code, self.persentage, self.datetime)
   



adminB = Admin("Brawny","keartti@gmail.com")

c1 = Coupon("c00001", 10, "29-3-23")
c2 = Coupon("c00002", 10, "29-3-23")



adminB.add_coupon(c2)
adminB.add_coupon(c1)

adminB.delete_coupon(c1)

print(adminB.get_coupon)



