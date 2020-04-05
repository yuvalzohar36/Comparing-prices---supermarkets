# this file also contains 2 function that belongs to other project ( the writing to txt files )
import xml.etree.ElementTree as ET
from Product import Product

class MakeData():
    def __init__(self):
        self.data_shufersal = []
        self.data_market = []
        self.data_ramilevi = []
        self.file = open('C:\\Users\\yuval\\Desktop\\items.txt','w') # rami levi
        self.filecode = open('C:\\Users\\yuval\\Desktop\\itemscode.txt', 'w') # rami levi
        self.fileS = open('C:\\Users\\yuval\\Desktop\\itemss.txt','w')  #shufersal
        self.filecodeS = open('C:\\Users\\yuval\\Desktop\\itemscodes.txt', 'w') #shufersal

        self.tree_shufersal = ET.parse('C:\\Users\\yuval\\Desktop\\stores\\shufersalNesher.txt')
        self.root_shufersal = self.tree_shufersal.getroot()
        self.tree_market = ET.parse('C:\\Users\\yuval\\Desktop\\stores\\market.xml')
        self.root_market = self.tree_market.getroot()
        self.tree_ramilevi = ET.parse('C:\\Users\\yuval\\Desktop\\stores\\ramilevi.xml')
        self.root_ramilevi = self.tree_ramilevi.getroot()

    def makeAll(self):
        for i in self.root_shufersal[5]:
            product = Product("shufersal", i[3].text, str(i[12].text), str(i[4].text), i[1].text)
            self.data_shufersal.append(product)
        for i in self.root_market[4]:
            product = Product("market Store", i[3].text, i[12].text, str(i[4].text),i[1].text)
            self.data_market.append(product)
        for i in self.root_ramilevi[6]:
            product = Product("rami levi Store", i[3].text, i[12].text, i[4].text, i[1].text)
            self.data_ramilevi.append(product)

    def writeToTxt(self): # rami levi
        for i in range(len(self.data_ramilevi)):
            pro_name = self.data_ramilevi[i].product_name
            pro_code = self.data_ramilevi[i].item_code
            self.file.write(pro_name +"\n")
            self.filecode.write(pro_code + "\n")
        self.filecode.close()
        self.file.close()

    def writeToTxtSufersal(self): # Shufersal
        for i in range(len(self.data_shufersal)):
            pro_name = self.data_shufersal[i].product_name
            pro_code = self.data_shufersal[i].item_code
            self.fileS.write(pro_name +"\n")
            self.filecodeS.write(pro_code + "\n")
        self.filecodeS.close()
        self.fileS.close()

m = MakeData()
m.makeAll()
m.writeToTxtSufersal()
