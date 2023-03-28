class Cart:
    def __init__(self):
        self.__item_list = []
        # print (self.__item_list) 
        
    def add_to_cart(self,item):
        self.__item_list.append(item)
        print (self.__item_list) 
        

class AuthenticateUser:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.shopping_cart = []


    def get_shopping_cart(self):
        self.shopping_cart = Cart()
        

    def add_to_cart(self,product, number):
        item = Item(product,number)
        self.shopping_cart.append(item)
        # Cart.add_to_cart(item)

       

class Product:
    def __init__(self,name) :
        self.__name = name

class Item(Product):
    def __init__(self, name, number):
        super().__init__(name)
        self.__number = number


john = AuthenticateUser("john","mail")
john.get_shopping_cart

p1 = Product("oil")
p2 = Item("as",3)


john.add_to_cart(p1,2)
john.add_to_cart(p2,2)

cart = Cart()
cart.add_to_cart(p1,3)
# print (cart) 


