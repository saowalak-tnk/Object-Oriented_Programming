nums = []
no = int(input("No. : "))
for i in range(no):
    num = int(input('ใส่ตัวเลข : '))
    nums.append(num)
a = sum(nums) / len(nums)
print(nums)
print(f'ค่าเฉลี่ย{a}')
