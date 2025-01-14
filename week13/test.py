class Animal:
    def __init__(self, name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f'ชื่อ: {self.name} อายุ: {self.age} ปี สี: {self.color}'
class Dog(Animal):
    def __init__(self, name, age, color, race):
        super().__init__(name, age, color)
        self.race =race
    def showinfo(self):
        return f"หมาพันธ์ {self.race} มี {super().showinfo()}"
animal1 = Animal('dog', 2, 'black')
dog1 = Dog('dog', 2, 'black', 'poodle')
print(animal1.showinfo())
