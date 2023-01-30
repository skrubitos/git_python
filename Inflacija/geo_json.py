import urllib.request, urllib.parse
import json

url= "https://py4e-data.dr-chuck.net/json?"
ivanko=dict()
adresa = input("what is your adress? ")
ivanko["adress"]=adresa
skupni_url= url + urllib.parse.urlencode(ivanko)

print(f"Retrieving url: {skupni_url}")

spajanje= urllib.request.urlopen(skupni_url)
citanje=spajanje.read().decode()


