import pymysql
conn=pymysql.connect(host="localhost",database='login',user="root",password="lahari97")
cursor=conn.cursor()
str="insert into webpagelog values('madh@gmail','saikrishna')"
try:
    cursor.execute(str)
    conn.commit()
    print("1 row inserted...")
except:
    conn.rollback()

cursor.close()
conn.close()
