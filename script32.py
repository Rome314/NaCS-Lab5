import requests, webbrowser

url = 'http://www.iu.ru/Assignment/case32.php'
r = requests.get(url, allow_redirects=False)

with open('results.html', 'w') as f:
	f.write(r.text)

new = 2
webbrowser.open('results.html', new=new)
