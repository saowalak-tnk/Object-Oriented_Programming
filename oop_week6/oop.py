class Cat:
    def __init__(self,ชื่อ,อายุ,สี,ความหิว):
        self.name = ชื่อ
        self.age = อายุ
        self.color = สี
        self.hungry = ความหิว
    def eat(self,อาหาร):
        self.hungry += อาหาร
cat1=Cat(ชื่อ="สม",อายุ=10,สี="ส้ม",ความหิว=5)
cat2=Cat("สี",10,"k",1)
print(cat1.color)
print(cat2.age)
