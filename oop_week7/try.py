while True:
    try :
        print("โปรแกรมหาพื้นที่ 3 เหลี่ยม")
        u = int(input('ใส่ค่าฐาน \n'))
        if u == 0:
            raise ZeroDivisionError
        elif u < 0:
            raise Exception
        u = int(input('ใส่ค่าความสูง\n'))
        if u == 0:
            raise ZeroDivisionError
        elif u < 0:
            raise Exception
        q = 0.5 * u * u
        print(f'พื้นที่ของ 3 เหลี่ยม = {q}')

        print("โปรแกรมหาพื้นที่ 4 เหลี่ยมผืนผ้า")
        u = int(input('ใส่ค่าความกว้าง\n'))
        if u == 0:
            raise ZeroDivisionError
        elif u < 0:
            raise Exception
        u = int(input('ใส่ค่าความยาว\n'))
        if u == 0:
            raise ZeroDivisionError
        elif u < 0:
            raise Exception
        t = u * u
        print(f'พื้นที่ของ 4 เหลี่ยมผืนผ้า = {t}')
        print("โปรแกรมหาพื้นที่ วงกลม")
        u = int(input('ใส่ค่ารัศมี\n'))
        if u == 0:
            raise ZeroDivisionError
        elif u < 0:
            raise Exception
        o = 3.14 * u ** 2
        print(f'พื้นที่ของวงกลม = {o}')
    except ValueError:
        print("ใส่เฉพาะตัวเลขเต็ม")
    except ZeroDivisionError:
        print("ห้ามใส่ศูนย์")
    except:
        print("ห้ามติดลบ")