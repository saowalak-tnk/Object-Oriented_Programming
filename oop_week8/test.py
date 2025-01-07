class Test :
    def __init__(self,name,job,salary):
        self.Name = name
        self.Job = job
        self.salary = salary
        
    def salaryyear(self):
        q = self.salary * 12      
        return q
    
job1 = Test('คาราเกะ','ครู',12000)
job2 = Test('ทงคัตสึ','หมอ',45000)
job3 = Test('มิโซะ','โปรแกรมเมอร์',40000)
print(f'{job1.Name} ประกอบอาชีพ {job1.Job} มีเงินเดือนทั้งปี {job1.salaryyear()}') 
print(f'{job2.Name} ประกอบอาชีพ {job2.Job} มีเงินเดือนทั้งปี {job2.salaryyear()}') 
print(f'{job3.Name} ประกอบอาชีพ {job3.Job} มีเงินเดือนทั้งปี {job3.salaryyear()}') 


        