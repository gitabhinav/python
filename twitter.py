import urllib
import twurl
import json
import dbconn

twitter_url = 'https://api.twitter.com/1.1/friends/list.json'
conn = dbconn.open('root','root','twitter')
cur = conn.cursor()
url = twurl.augment(twitter_url,{'screen_name':'abhinavsaxena','count':'20'})
print("Retrieving data...")
connection = urllib.urlopen(url)
data = connection.read()
headers = connection.info().dict
js = json.loads(data)

cur.execute('insert into spider_data (spider_data) values (?)', (js))

cur.close()
dbconn.close(conn)
