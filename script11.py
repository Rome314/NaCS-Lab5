import urllib, urllib2, webbrowser

url = 'http://www.iu.ru/Assignment/case11.php'
values = {'qty': 1, 'Price':0}
data = urllib.urlencode(values)

req = urllib2.Request(url, data)
rsp = urllib2.urlopen(req)

with open('results.html', 'w') as f:
	f.write(rsp.read())

new = 2
webbrowser.open('results.html', new=new)
