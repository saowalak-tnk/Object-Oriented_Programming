class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__price = []
        self.__stock = stock
    def add(self):
        self.__stock += instock
    def dele(self):
        self.__stock -= instock
    def edit(self):
        inprice = int(input('กรอกราคาสินค้า '))
        self.__price.append(inprice)
    def detail(self):
        return (f'(มีราคา {self.__price} บาท จำนวน {self.__stock} ชิ้น)')

pro1 = Product('book', 0)
while True:
    a = input('กรุณาเลือก: ต้องการ เพิ่มจำนวนสินค้า(add)  ลดจำนวนสินค้า(dele) ตรวจสอบสินค้า(check)  แก้ไขราคาสินค้า(edit) ออก(exit) : ')
    if a == 'add':
        instock = int(input('จำนวนที่ต้องการเพิ่ม: '))
        pro1.add()
    elif a == 'dele':
        instock = int(input('จำนวนที่ต้องการลด: '))
        pro1.dele()
    elif a == 'check':
        print(f'รายการสินค้า {pro1.name} มีรายละเอียดดังนี้ {pro1.detail()}')
    elif a == 'edit':
        pro1.edit()
    elif a == 'exit':
        break
print(f'รายการสินค้า {pro1.name} มีรายละเอียดดังนี้ {pro1.detail()}')
