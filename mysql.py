import pymysql

db = pymysql.connect(host='192.168.225.130', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
user = 'Bob'
sql = 'INSERT INTO inori(name) values(%s)'
try:
    cursor.execute(sql, (user))
    db.commit()
except:
    db.rollback()
db.close()
