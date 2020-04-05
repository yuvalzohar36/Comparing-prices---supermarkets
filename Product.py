# this file make new objects call Product 

class Product():
    def __init__(self, store_name, product_name, price,manufacturer_name, item_code ):
        self.store_name = str(store_name)
        self.product_name = str(product_name)
        self.price = str(price)
        self.manufacturer_name = str(manufacturer_name)
        self.item_code = str(item_code)

    def printValues(self):
        print("Store name : " + self.store_name)
        print("Product name : " + self.product_name)
        print("Price : " + self.price)
        print("Manufacturer Name : " + self.manufacturer_name)
        print("Item Code : " + self.item_code)
