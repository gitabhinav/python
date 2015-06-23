import dbconn
conn = dbconn.open('root','root','world')
cursor = conn.cursor()
table = 'city'
cursor.execute("select * from city")
for rows in cursor:
    print("fetching data...",'/n',cursor.fetchone())
dbconn.close(conn)

