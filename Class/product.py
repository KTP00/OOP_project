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
PentelCaplet = pencil("CON4031717","CON4031717.png","ดินสอกด Pentel Caplet 0.5 มม.","26฿","10 อัน","ดินสอและอุปกรณ์เสริม","ดินสอ","19 Mar 2023",False,"ฟ้า","HB")
print(PentelCaplet.__dict__.items())
STAEDTLER100 = pencil("CON4033233","CON4033233.jpg","ดินสอ STAEDTLER Mars Lumograph 100","24฿","10 อัน","ดินสอและอุปกรณ์เสริม","ดินสอ","20 Mar 2023",False,"ดำ","HB")
STAEDTLER100ฺB = pencil("1011036","1011036.jpg","ดินสอ STAEDTLER Mars Lumograph black 100B เกรด 4B","24฿","10 อัน","ดินสอและอุปกรณ์เสริม","ดินสอ","20 Mar 2023",False,"ดำ","4B")
#pencil lead ไส้ดินสอกด
QUANTUM = pencil("1510610","1510610.jpg","QUANTUM ไส้ดินสอกด Q300 ขนาด 0.5 มม. 2 บี","16฿","10 อัน","ดินสอและอุปกรณ์เสริม","ไส้ดินสอ","20 Mar 2023",False,"-","2B")
#pencil box กล่องใส่ดินสอ
PencilBox = pencil("5336997","5336997.jpg","SET กล่องดินสอแม่เหล็ก พอลแฟลงค์","199฿","10 อัน","ดินสอและอุปกรณ์เสริม","กล่องดินสอ","20 Mar 2023",False,"-","-")
#pencil sharpener กบเหลาดินสอ 
ELM147 = pencil("5094965","5094965.jpg","ELM เครื่องเหลาดินสอ สามารถเหลาแท่งใหญ่ได้ ELM-147 แดง","289฿","10 อัน","ดินสอและอุปกรณ์เสริม","กบเหลาดินสอ","20 Mar 2023",False,"แดง","-")
FABER_CASTEL = pencil("1001835","1001835.jpg","กบเหลาดินสอ FABER CASTEL รุ่น 1819 สีพลาสเทล (คละแบบ)","15฿","10 อัน","ดินสอและอุปกรณ์เสริม","กบเหลาดินสอ","20 Mar 2023",False,"-","-")
# earser ยางลบ
ZEH = pencil("1521010","1521010.jpg","ยางลบดินสอ เล็ก เพนเทล Hi-Polymer ZEH-03E","14฿","10 อัน","ยางลบและน้ำยาลบคำผิด ","ยางลบ","20 Mar 2023",False,"-","-")
#liquid paper น้ำยาลบคำผิด/เทปลบคำผิด
FinePoint= pencil("1300050","1300050.jpg","ปากกาลบคำผิด 4.2 มล. เพนเทล Fine Point ZL102-WBP","54฿","10 อัน","ยางลบและน้ำยาลบคำผิด ","น้ำยาลบคำผิด/เทปลบคำผิด","20 Mar 2023",False,"-","-")
XZTT15P= pencil("1006768","1006768.jpg","เทปลบคำผิด 5มม.x12ม. น้ำเงิน เพนเทล XZTT15P-W","62฿","10 อัน","ยางลบและน้ำยาลบคำผิด ","น้ำยาลบคำผิด/เทปลบคำผิด","20 Mar 2023",False,"-","-")


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


