a = input("โปรดกรอกชื่อ \n")
b = input("โปรดกรอกอายุ \n")
c = input("โปรดกรอกรหัสประจำตัวนักศึกษา \n")
d = input("โปรดกรอกชั้นปี \n")
e = input("โปรดกรอกชื่อเล่น \n")
f = float(input("โปรดกรอกส่วนสูง \n"))
g = float(input("โปรดกรอกน้ำหนัก \n"))
t = f + g
print(f'ชื่อ: {a} อายุ: {b} ปี')
print(f'รหัสประจำตัวนักเรียน: {c} ระดับชั้น: {d}')
print(f'ชื่อเล่น: {e}')
print(f'ส่วนสูง: {f} เซนติเมตร น้ำหนัก: {g} กิโลกรัม')
print(f'ส่วนสูง + น้ำหนัก = {t}')