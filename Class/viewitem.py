class Product:
    def __init__(self, id , name , instock):
        self.id = id
        self.name = name
        self.instock = instock



class Catalog(Product):

    def __init__(self):
        self.catalog = []

    @property
    def get_catalog(self):
        return self.catalog
    
    def add_catalog(self,product):
        self.catalog.append(product)
        print(self.catalog) 

   

   

p1 = Product("a1001", "Oil", 7)
p2 = Product("a1s1", "Book", 3)
p3 = Product("a1sa1", "Pen", 3)

c1 = Catalog()
c1.add_catalog(p1)
c1.add_catalog(p2)
c1.add_catalog(p3)




