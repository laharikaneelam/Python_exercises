import pymysql
conn=pymysql.connect(host="localhost",database='login',user="root",password="lahari97")
cursor=conn.cursor()
cursor.execute("select *from webpagelog")
row=cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fetchone()
cursor.close()
conn.close()
