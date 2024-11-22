import random 

class Student :
    def __init__(self,ชื่อนามสกุล,ชื่อเล่น,):
        self.name = ชื่อนามสกุล
        self.nickname = ชื่อเล่น
        self.score = random.randint(1,10)
    def Scores(self):
        if self.score >= 5:
            print(f"{self.name} {self.nickname} {self.score} : คุณสอบผ่าน")
        else :
            print(f"{self.name} {self.nickname} {self.score} : คุณสอบตก")
student1 =Student("Chaiyanan yimsawat","Queue",)
student2 =Student("Chutima Siritham","Sen",)
student3 =Student("Gamolsak Chirangphan","Aof",)
student4 =Student("nanticha wongyong","Ice",)
student5 =Student("Thanchanok Chaichana","Ked",)
 
student1.Scores()
student2.Scores()
student3.Scores()
student4.Scores()
student5.Scores()


