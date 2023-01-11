import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url="https://py4e-data.dr-chuck.net/known_by_Fikret.html"

count=int(5)
pos=int(3)-1

urllist=list()

for i in range(count):
    html=urllib.request.urlopen(url)
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    print("   tags",tags)
    print('Retrieveing:',url)
    taglist=list()
    for tag in tags:
        y=tag.get('href',None)
        print("y",y)
        taglist.append(y)

    url=taglist[pos]

    urllist.append(url)
print("lista",urllist)

print("Last Url:",urllist[-2])
print(taglist)
