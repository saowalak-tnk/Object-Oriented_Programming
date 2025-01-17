import database
mycursor = database.mydb.cursor()
def selectdb(table):
    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)
    show = mycursor.fetchall()
    return show

def deletedb(table, id_name, id):
    sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
    mycursor.execute(sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False


def editdb(table, column, id_name, id,val):
    sql = f"UPDATE {table} SET {column} = %s WHERE {id_name} = %s"
    val_sql = (val, id)
    mycursor.execute(sql, val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False   
#print(editdb('products','stock','product_id',1,100)) 
def insert_products(name,des, price, stock):
    sql = "INSERT INTO products  VALUES (%s, %s, %s, %s, %s)"
    val_sql = (None, name,des, price, stock)
    mycursor.execute(sql, val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
#print(insert_products('SHUTLINE','หนังสือวาย', 1299, 50))
def insert_categories(name):
    sql = "INSERT INTO categories  VALUES (%s, %s)"
    val_sql = (None, name)
    mycursor.execute(sql, val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
#print(insert_categories('โลกสวย'))   
def insert_user(name,password,email,role):
    sql = "INSERT INTO user  VALUES (%s, %s, %s, %s, %s)"
    val_sql = (None, name,password,email,role)
    mycursor.execute(sql, val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
#print(insert_user('ue',1993,'saowalak.yuri@gmail.com','admin'))
def insert_oders(date,amount,status):
    sql = "INSERT INTO orders  VALUES (%s, %s, %s, %s)"
    val_sql = (None, date,amount,status)
    mycursor.execute(sql, val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
print(insert_oders('28/10/2548',1299,'กำลังจัดส่ง'))   
