import urllib, urllib2, webbrowser

url = 'http://www.iu.ru/Assignment/case01.php'
values = {'age': 100}
data = urllib.urlencode(values)

req = urllib2.Request(url, data)
rsp = urllib2.urlopen(req)

with open('results.html', 'w') as f:
        f.write(rsp.read())

new = 2
webbrowser.open('results.html', new=new)
