class product : 
  def __init__(self, id, picture, name, price, in_stock, category, type, date, recommend):
    self.id = id
    self.picture = picture
    self.name = name
    self.price = price
    self.in_stock = in_stock
    self.category = category
    self.type = type
    self.date = date
    self.recommend = recommend


class book(product) :
  def __init__(self, id, picture, name, price, in_stock, category, type,date,recommend, author_name, publisher):
    product.__init__(self, id, picture, name, price, in_stock, category, type,date,recommend) 
    self.author_name = author_name
    self.publisher = publisher
    
class Pen(product) :
  def __init__(self, id, picture, name, price, in_stock, category, type,date,recommend, color):
    product.__init__(self, id, picture, name, price, in_stock, category, type,date,recommend)
    self.color = color
    
class pencil(product) :
  def __init__(self, id, picture, name, price,  in_stock, category, type,date,recommend, color, intensity):
    product.__init__(self, id, picture, name, price, in_stock,  category, type,date,recommend)
    self.color = color
    self.intensity = intensity

class earser(product) :
  def __init__(self, id, picture, name, price, in_stock,  category, type,date,recommend, color):
    product.__init__(self, id, picture, name, price, in_stock, category, type,date,recommend)
    self.color = color

class measurementTool(product) :
  def __init__(self, id, picture, name, price, in_stock,   category, type,date,recommend, size):
    product.__init__(self, id, picture, name, price, in_stock,  category, type,date,recommend)
    self.size = size
  
class paper(product) :
  def __init__(self, id, picture, name, price,  in_stock, category, type,date,recommend,  color, size ):
    product.__init__(self, id, picture, name, price, in_stock, category, type,date,recommend)
    self.color = color
    self.size = size


# Book 
# นิยาย    






# Pen






# pencil
PentelCaplet = pencil("CON4031717","CON4031717.png","ดินสอกด Pentel Caplet 0.5 มม.","26฿","10 อัน","ดินสอและอุปกรณ์เสริม","ดินสอ","19 Mar 2023",False,"ฟ้า","0.5 มม.")
print(PentelCaplet.__dict__.items())


# earser





# measurementTool







# paper












    
######################################################
class item(product) :
  def __init__(self, id, picture, name, price, in_stock, details, category, type,date,recommend, quantity,promotion):
    product.__init__(self, id, picture, name, price, in_stock, details, category, type,date,recommend) 
    self.quantity = quantity
    self.promotion = promotion
    
class catalog(product) :
  def __init__(self, name, price, picture):
    product.__init__(self, name, price, picture)
    
    
class newProductCatalog(catalog) :
  def __init__(self, name, price, picture):
    catalog.__init__(self, name, price, picture)
    
    
class bookRecommendCatalog(catalog) :
  def __init__(self, name, price, picture):
    catalog.__init__(self, name, price, picture)
    
class paperRecommendCatalog(catalog) :
  def __init__(self, name, price, picture):
    catalog.__init__(self, name, price, picture)

class stationeryRecommendCatalog :
  def __init__(self, name, price, picture):
    catalog.__init__(self, name, price, picture)


