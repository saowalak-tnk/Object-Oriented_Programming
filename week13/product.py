class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__price = []
        self.__stock = stock
    def add(self ,instock):
        if instock > 0:
            self.__stock += instock
            print(f"เพิ่มสินค้า {self.name} จำนวน {instock} ชิ้นเรียบร้อยแล้ว")
        else:
            print("จำนวนสินค้าที่เพิ่มต้องมากกว่า 0")
    def dele(self ,instock):
        if 0 < instock <= self.__stock:
            self.__stock -= instock
            print(f"ลดสินค้า {self.name} จำนวน {instock} ชิ้นเรียบร้อยแล้ว")
        else:
            print("จำนวนสินค้าที่ลดไม่ถูกต้อง หรือมีสินค้าในสต็อกไม่เพียงพอ")
    def edit(self):
        inprice = int(input('กรอกราคาสินค้า '))
        self.__price.append(inprice)
        print(f"ราคาสินค้า {self.name} ถูกตั้งไว้ที่ {inprice} บาท")
    def detail(self):
        return (f'(ชื่อ {self.name} จำนวน {self.__stock} ชิ้น)')
    
class Phone(Product):
    def __init__(self, name, stock, brand):
        super().__init__(name, stock)
        self.brand = brand
    def detail(self):
        return f"แบรนด์ {self.brand} {super().detail()}"
    
class Notebook(Product):
    def __init__(self, name, stock, system):
        super().__init__(name, stock)
        self.system = system
    def detail(self):
        return f'ระบบปฏิบัติการ {self.system} {super().detail()}'
    
class Clothes(Product):
    def __init__(self, name, stock, size):
        super().__init__(name, stock)
        self.size = size
    def detail(self):
        return f'size {self.size} {super().detail()}'

pro1 = Product('book', 0)
phone1 = Phone("IPhone16", 50, 'apple')
notebook1 = Notebook('acer', 20, 'Windows')
clothes1 = Clothes('nile', 100, 'M')
phone1.edit()
print(phone1.detail())
