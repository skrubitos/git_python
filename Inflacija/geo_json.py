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


print(len(citanje))
try:
    js = json.loads(citanje)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(citanje)


print(json.dumps(js, indent=4))

lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)