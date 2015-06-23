import urllib.request

fhand = urllib.request.urlopen('http://timesofindia.indiatimes.com/home/education/news/Its-springtime-for-MBAs-again-Study/articleshow/47363732.cms')
for line in fhand:
    print (line.strip())
