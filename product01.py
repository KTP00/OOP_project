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
My_Engineer = book("D099956", "My_Engineer.png", "My Engineer", 599, 5,
                   "ตุ๊กตากระเบื้องเคลือบ", " Lavender",
                   "หนังสือนิยาย / วรรณกรรม", "นิยายวาย นิยายยูริ", "18_3_23",
                   False)
Alumni_page = book("DA01870", "Alumni_page.jpg", "Alumni_page", 319, 6,
                   "Shuhai Cangsheng", "หอมหมื่นลี้",
                   "หนังสือนิยาย / วรรณกรรม", "นิยายจีน", "18_3_23", False)
Hello_World = book("DA00069", "Hello_World.jpeg",
                   "Hello World เธอ.ฉัน.โลก.เรา (ปกอ่อน)", 256, 10,
                   "Mado Nozaki (มาโดะ โนซากิ)", "Ume Publishing",
                   "หนังสือนิยาย / วรรณกรรม", "นิยายแฟนตาซี", "18_3_23", False)
Fire_lover = book("D094164", "Fire_lover.jpg",
                  "หนังสือนิยาย Fire lover ไฟละลายรัก", 287, 7, "ทิรารัน",
                  "Lavender", "หนังสือนิยาย / วรรณกรรม", "นิยายโรแมนติก",
                  "18_3_23", False)
ON_TARGET = book("DA03432", "ON_TARGET.jpg", "หนังสือ พิกัดนรก ON TARGET", 315,
                 6, "MARK GREANEY", "น้ำพุสำนักพิมพ์",
                 "หนังสือนิยาย / วรรณกรรม", "นิยายสืบสวนสอบสวน", "18_3_23",
                 False)
THE_SHINING = book("D098790", "THE_SHINING.jpeg",
                   "หนังสือ THE SHINING โรงแรมนรก", 495, 9, "สตีเวน คิง",
                   "BEAT", "หนังสือนิยาย / วรรณกรรม", "นิยายสยองขวัญ",
                   "18_3_23", False)

#การ์ตูน/มังงะ
haikyuu = book("5302044", "haikyuu.jpg",
               "ไฮคิว!! คู่ตบฟ้าประทาน เล่ม 36 - ฉันชนะ", 60, 14,
               "HARUICHI FURUDATE", "siam inter comic", "การ์ตูน/มังงะ",
               "หนังสือการ์ตูน", "19_3_23", False)
Dragon_Maid = book("DA02851", "Dragon_Maid.jpeg",
                   "หนังสือการ์ตูน น้องเมดมังกรของคุณโคบายาชิ เล่ม 4", 97, 10,
                   "Coolkyousinjya", "เซนชู พับลิชชิ่ง จำกัด", "การ์ตูน/มังงะ",
                   "หนังสือการ์ตูน", "19_3_23", False)
One_Piece = book("D093454", "One_Piece.jpeg", "วัน พีซ - One Piece เล่ม 36",
                 40, 9, "EIICHIRO ODA", "siam inter comic", "การ์ตูน/มังงะ",
                 "หนังสือการ์ตูน", "19_3_23", False)
The_Wolf = book("DA02822", "The_Wolf.jpeg",
                "หนังสือ The Wolf Who Picked Up หมาป่าผู้เก็บบางสิ่งมา ", 449,
                9, "หมาเหว่ย", "FIN PUBLISHING", "การ์ตูน/มังงะ",
                "หนังสือการ์ตูน", "19_3_23", False)
Solo_Leveling = book("5332743", "Solo_Leveling.jpeg",
                     "หนังสือSolo Leveling 1 Mg (ปกอ่อน)", 275, 9, "ชู่กง",
                     "PHOENIX", "การ์ตูน/มังงะ", "หนังสือการ์ตูน", "19_3_23",
                     False)
Morimiya = book("5337463", "Morimiya.jpeg",
                "หนังสือโฮริมิยะ สาวมั่นกับนายมืดมน เล่ม 16 (เล่มพิเศษจบ)",
                240, 7, "DAISUKE HAGIWARA", "สยามอินเตอร์ คอมิคส์ บ.จ.ก.",
                "การ์ตูน/มังงะ", "หนังสือการ์ตูน", "19_3_23", False)

#  หนังสือเด็ก
# นิทาน
kide_dragon = book("DA02626", "DA02626.jpeg", "หนังสือ มังกรน้อยหวงสมบัติ",
                   242, 7, "Nicola Kinnear", "Dandelion Publishing",
                   "หนังสือเด็ก", "หนังสือนิทาน", "19_3_23", False)
kide_ABC = book("D097214", "D097214.jpeg",
                "หนังสือ คนเก่งหัดคัดเขียน ABC (พร้อมระบายสี) (ปกอ่อน)", 31, 7,
                "กองบรรณาธิการ", "No author ", "หนังสือเด็ก",
                "หนังสือเสริมทักษะ", "19_3_23", False)
kide_Plants_Zombies = book("DA03576", "DA03576.jpeg",
                           "หนังสือ Plants vs Zombies ท่องโลกดาราศาสตร์และกะเทาะโจทย์คณิต", 80, 7, 
                           "หนังสือเด็ก", "หนังสือการ์ตุนความรู้", "19_3_23", False)
kide_Word_Book = book("D093680", "D093680.jpeg",
                      "หนังสือ Picture Word Book ศัพท์ภาษาอังกฤษ 5000 คำ", 169,
                      7, "มัญชรี สุรอภินันทน์", "อักษรา ฟอร์ คิดส์, บจก.",
                      "หนังสือเด็ก", "ความรู้ทั่วไปสำหรับเด็ก/สารานุกรม",
                      "19_3_23", False)
Board_color = book("DA03778", "DA03778.jpeg",
                   "Board Book : Colors (ใช้ร่วมกับ MIS Talking Pen)", 95, 7,
                   "", "", "หนังสือเด็ก",
                   "หนังสือสื่อการเรียนรู้", "19_3_23", False)

# หนังสือหนังสือจิตวิทยาทั่วไป
# หนังสือหนังสือจิตวิทยาทั่วไป(General Psychology)
GP1 = book("D096180", "D096180.jpeg",
                   "หนังสือ ทำไงได้ ก็งานต้องเสร็จวันนี้นี่นา", 295, 7,
                   "SEOLLEDA",
                   "SPRINGBOOKS", "หนังสือหนังสือจิตวิทยาทั่วไป",
                   "หนังสือหนังสือจิตวิทยาทั่วไป", "21_3_23", False)
GP2 = book("D091255", "D091255.jpeg",
                   "หนังสือ เหนื่อยไหม กอดหัวใจตัวเองหรือยัง", 295, 7,
                   "ยุนแดฮย็อน",
                   "Bloom publishing", "หนังสือหนังสือจิตวิทยาทั่วไป",
                   "หนังสือให้กำลังใจ", "21_3_23", False)
GP3 = book("D092006", "D092006.jpeg",
                   "หนังสือ บวก ลบ คุณ ฉัน ความน่าจะรักระหว่างเรา", 239, 5,
                   "Hannah Fry",
                   "Being", "หนังสือหนังสือจิตวิทยาทั่วไป",
                   "หนังสือพัฒนาความสัมพันธ์ ความรัก ครอบครัว", "21_3_23", False)
GP4 = book("D094629", "D094629.jpeg",
                   "หนังสือ THE ART OF REST พักผ่อนศาสตร์ ศาสตร์แห่งการพักให้ได้พัก (อย่างแท้จริง)", 231, 5,
                   "CLAUDIA HAMMOND",
                   "Cactus Publishing", "หนังสือหนังสือจิตวิทยาทั่วไป",
                   "หนังสือพัฒนาตนเอง", "21_3_23", False)

#หนังสือธุรกิจ
#หุ้นและการลงทุน
Bs1 = book("D092862","D092862.jpeg",
                   "หนังสือ MONEY SUMMARY สรุปเรื่องเงินให้เข้าใจง่ายใน 1 เล่ม", 259, 5,
                   "จักรพงษ์ เมษ์พันธุ์",
                   " I AM THE BEST", "ธุรกิจ",
                   "หุ้นและการลงทุน", "21_3_23", False)
Bs2 = book("D098142","D098142.jpeg",
                   "หนังสือ เทรดหุ้นด้วยกราฟ ฉบับมือใหม่", 220, 5,
                   "พัชราภรณ์ เคนชมภู",
                   "พราว", "ธุรกิจ",
                   "หุ้นและการลงทุน", "21_3_23", False)
#หนังสือการตลาด
Bs3 = book("D097848","D097848.jpeg",
                   "หนังสือ อินฟลูเอนเซอร์ : พลังการขายให้เหมือนไม่ได้ขาย", 265, 5,
                   "ซาร่า แมคคอร์ควอเดล",
                   "อมรินทร์ How To, สนพ.", "ธุรกิจ",
                   "การตลาด", "21_3_23", False)
Bs4 = book("DA00886","DA00886.jpeg",
                   "หนังสือ ดันเว็บไซต์ให้เป็นที่ 1 ในใจลูกค้าด้วย SEO 3rd Edition", 365, 5,
                   "ศุภณัฐ สุขโข",
                   "INFO PRESS", "ธุรกิจ",
                   "การตลาด", "21_3_23", False)
#การจัดการ/ธุรกิจ
Bs5 = book("D097384","D097384.jpeg",
                   "หนังสือ งานประจำสอนทำธุรกิจ (ปกอ่อน)", 245, 5,
                   "นาฟิส อิสลาม",
                   "อะไรเอ่ย, สนพ.", "ธุรกิจ",
                   "การจัดการ/ธุรกิจ", "21_3_23", False)
Bs6 = book("DA00058","DA00058.jpeg",
                   "หนังสือ คู่มือทดสอบไอเดียธุรกิจ",595, 5,
                   "DAVID J. BLAND, ALEX OSTERWALDER",
                   "วีเลิร์น", "ธุรกิจ",
                   "การจัดการ/ธุรกิจ", "21_3_23", False)
#การเงินและการลงทุน
Bs7 = book("D094536","D094536.jpeg",
                   "หนังสือ อ่านงบการเงินด้วยปากกา 3 สี", 255,5 ,
                   "โยชิตะ คันจิ",
                   "วีเลิร์น", "ธุรกิจ",
                   "การเงินและการลงทุน", "21_3_23", False)
Bs8 = book("D096636","D096636.jpeg",
                   "หนังสือ จิตวิทยาว่าด้วยเงิน", 290,5,
                   "MORGAN HOUSEL",
                   "ลีฟ ริช ฟอร์เอฟเวอร์", "ธุรกิจ",
                   "การเงินและการลงทุน", "21_3_23", False)
#เศรษฐศาสตร์
Bs9 = book("D097711","D097711.jpeg",
                   "หนังสือ เศรษฐกิจโลก 1,000 ปี", 30,5,
                   "ลงทุนแมน",
                   "แอลทีแมน", "ธุรกิจ",
                   "เศรษฐศาสตร์", "21_3_23", False)
Bs10 = book("D099043","D099043.jpeg",
                   "หนังสือ ECONOMIX เศรษฐกิจ สะกิดสมอง", 30,5,
                   " Michael Goodwin (ไมเคิล กูดวิน)",
                   "ลีฟ ริช ฟอร์เอฟเวอร์", "ธุรกิจ",
                   "เศรษฐศาสตร์", "21_3_23", False)





# Pen






# pencil
PentelCaplet = pencil("CON4031717","CON4031717.png","ดินสอกด Pentel Caplet 0.5 มม.",26,10,"ดินสอและอุปกรณ์เสริม","ดินสอ","19 Mar 2023",False,"ฟ้า","HB")
print(PentelCaplet.__dict__.items())
STAEDTLER100 = pencil("CON4033233","CON4033233.jpg","ดินสอ STAEDTLER Mars Lumograph 100",24,10,"ดินสอและอุปกรณ์เสริม","ดินสอ","20 Mar 2023",False,"ดำ","HB")
STAEDTLER100ฺB = pencil("1011036","1011036.jpg","ดินสอ STAEDTLER Mars Lumograph black 100B เกรด 4B",24,10,"ดินสอและอุปกรณ์เสริม","ดินสอ","20 Mar 2023",False,"ดำ","4B")
#pencil lead ไส้ดินสอกด
QUANTUM = pencil("1510610","1510610.jpg","QUANTUM ไส้ดินสอกด Q300 ขนาด 0.5 มม. 2 บี",16,10,"ดินสอและอุปกรณ์เสริม","ไส้ดินสอ","20 Mar 2023",False,"-","2B")
#pencil box กล่องใส่ดินสอ
PencilBox = pencil("5336997","5336997.jpg","SET กล่องดินสอแม่เหล็ก พอลแฟลงค์",199,10,"ดินสอและอุปกรณ์เสริม","กล่องดินสอ","20 Mar 2023",False,"-","-")
#pencil sharpener กบเหลาดินสอ 
ELM147 = pencil("5094965","5094965.jpg","ELM เครื่องเหลาดินสอ สามารถเหลาแท่งใหญ่ได้ ELM-147 แดง", 289, 10,"ดินสอและอุปกรณ์เสริม","กบเหลาดินสอ","20 Mar 2023",False,"แดง","-")
FABER_CASTEL = pencil("1001835","1001835.jpg","กบเหลาดินสอ FABER CASTEL รุ่น 1819 สีพลาสเทล (คละแบบ)",15 , 10,"ดินสอและอุปกรณ์เสริม","กบเหลาดินสอ","20 Mar 2023",False,"-","-")
# earser ยางลบ
ZEH = pencil("1521010","1521010.jpg","ยางลบดินสอ เล็ก เพนเทล Hi-Polymer ZEH-03E",14,10,"ยางลบและน้ำยาลบคำผิด ","ยางลบ","20 Mar 2023",False,"-","-")
#liquid paper น้ำยาลบคำผิด/เทปลบคำผิด
FinePoint= pencil("1300050","1300050.jpg","ปากกาลบคำผิด 4.2 มล. เพนเทล Fine Point ZL102-WBP", 54, 10,"ยางลบและน้ำยาลบคำผิด ","น้ำยาลบคำผิด/เทปลบคำผิด","20 Mar 2023",False,"-","-")
XZTT15P= pencil("1006768","1006768.jpg","เทปลบคำผิด 5มม.x12ม. น้ำเงิน เพนเทล XZTT15P-W", 62, 10,"ยางลบและน้ำยาลบคำผิด ","น้ำยาลบคำผิด/เทปลบคำผิด","20 Mar 2023",False,"-","-")


# measurementTool
Twist_Maped_TC279210 = measurementTool("1005905", "Twist_Maped_TC279210.png",
                                       "Twist_Maped_TC279210", 38, 5,
                                       "อุปกรณ์วัด", "ไม้บรรทัด", "19_3_23",
                                       "20cm", False)
ARL960H9 = measurementTool("1011388", "ARL960H9.png", "ARL960H9", 10, 5,
                           "อุปกรณ์วัด", "ไม้บรรทัด", "19_3_23", "15cm", False)
# วงเวียน

MAPED_GRAPHIC = measurementTool("K090974", "MAPED_GRAPHIC.png",
                                "MAPED_GRAPHIC", 49, 5, "อุปกรณ์วัด",
                                "วงเวียน", "19_3_23", "3.5x12cm", False)
MAPED_STUDY = measurementTool("K090971", "MAPED_STUDY.png", "MAPED_STUDY", 62,
                              5, "อุปกรณ์วัด", "วงเวียน", "19_3_23",
                              "3.5x12cm", False)

# ชุดเรขาคณิต

snoopy_MG_SRL96087 = measurementTool("5338029", "snoopy_MG_SRL96087.png",
                                     "snoopy_MG_SRL96087", 45, 5, "อุปกรณ์วัด",
                                     "ชุดเรขาคณิต", "19_3_23", "7.5x0.4x19cm",
                                     "False")
snoopy_SRL960Q8 = measurementTool("5338028", "snoopy_SRL960Q8.png",
                                  "snoopy_SRL960Q8", 50, 5, "อุปกรณ์วัด",
                                  "ชุดเรขาคณิต", "19_3_23", "8x0.5x19.5cm",
                                  "False")
MG_FRL96011 = measurementTool("5380302", "MG_FRL96011.png", "MG_FRL96011", 37,
                              5, "อุปกรณ์วัด", "ชุดเรขาคณิต", "19_3_23",
                              "8.5x0.7x18cm", False)



# paper
A4_DOUBLE_A = paper("CON5196170", "A4_DOUBLE_A.png", "A4_DOUBLE_A", 43, 10,
                    "white", "กระดาษ", "กระดาษโน้ต", "19_3_23",
                    "21x29.7cm(A4)", False)
KAKAO = paper("5293360", "KAKAO.png", "KAKAO", 78, 10, "white", "กระดาษ",
              "กระดาษโน้ต", "19_3_23", "9X9cm", False)

# กระดาษถ่ายเอกสาร
A4_SHIH_TZU = paper("5002166", "A4_SHIH_TZU.png", "A4_SHIH_TZU", 108, 5,
                    "white", "กระดาษ", "กระดาษถ่ายเอกสาร", "20_3_23",
                    "210x297cm(A4)", False)
Quality = paper("5005764", "Quality.png", "Quality", 110, 5, "white", "กระดาษ",
                "กระดาษถ่ายเอกสาร", "20_3_23", "210x297cm(A4)", False)

#  กระดาษสติ๊กเกอร์
SC003_PASTEL_A6 = paper("5309381", "SC003_PASTEL_A6.png", "SC003_PASTEL_A6",
                        108, 5, "assorted", "กระดาษ", "กระดาษสติ๊กเกอร์",
                        "20_3_23", "(Aุ6)", False)

# กระดาษรายงาน
Double_A_Professional = paper("5001320", "Double_A_Professional.png",
                              "Double_A_Professional", 17, 5, "purple",
                              "กระดาษ", "กระดาษรายงาน", "20_3_23",
                              "15.8x25.3cm", False)

# กระดาษความร้อน
CASIO_808 = paper("5004736", "CASIO_808.png", "CASIO_808", 175, 5, "black",
                  "กระดาษ", "กระดาษความร้อน ", "20_3_23", "80x80cm", False)











    
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


