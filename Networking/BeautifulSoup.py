from bs4 import BeautifulSoup
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

juva= BeautifulSoup(html_doc, "html.parser")

            #nested data structure
#print(juva.prettify())      #printa nam se lipo rasporedeno a ne onako ruzno



                #ako zelimo naci poveznice
for bonus in juva.find_all("a"): #nadje svaki red gdje ima poveznica <a
    print("ovo su imena:",bonus.get_text("href"), "a ovo su linkovi",bonus.get("href"))
"get_tex daje nan podatak koji ide kod linka dok nan obicni get daje poveznicu s linkom"
## [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


#ako zelimo da nam isprinta samo text iz svega bez html oznaka
#print(juva.text)