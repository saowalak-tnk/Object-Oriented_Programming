resume = {}
no = int(input("จำนวนคนที่ป้อน : "))
for i in range(1,no+1):
    resume['name'] = str(input('กรอกชื่อ :'))
    resume['nickname'] = str(input('กรอกชื่อเล่น :'))
    resume['stdid'] = str(input('กรอกรหัสนักศึกษา : '))
    resume['hobb'] = str(input('กรอกงานอดิเรก : '))
    resume['color'] = str(input('กรอกสีที่ชอบ : '))
    print(f'ข้อมูลคนที่{i}')
    print(resume)
    