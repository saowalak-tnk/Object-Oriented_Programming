a = 0
while True :
    q = input('ใส่ค่า : ')
    if q == 'หยุด' :
        print(f'ผลรวมตอนนี้ {a}')
        print(f'ผลรวมทั้งหมด {a}')
        break
    try :
        i = int(q)
        if i > 0 :
            a += i
            print(f'ผลรวมตอนนี้ {a}')
        elif i < 0:
            raise Exception
        elif i == 0:
            raise ZeroDivisionError
        else:
            raise ValueError
        
    except ValueError:
        print("ห้ามใส่ตัวหนังสือ")
    except ZeroDivisionError:
        print("ห้ามใส่0 ถ้าต้องการหยุด พิมคำว่า <หยุด>")
    except:
        print("ห้ามติดลบ")   