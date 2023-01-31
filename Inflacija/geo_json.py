import urllib.request, urllib.parse
import json
api_key = 42
url= 'http://py4e-data.dr-chuck.net/json?'
#adresa = input("what is your adress? ")
while True:
    adresa=input("Upisite svoju ulicu: ")
    ivanko=dict()
    ivanko["address"]=adresa
    ivanko['key']=api_key
    skupni_url= url + urllib.parse.urlencode(ivanko)

    print(f"Retrieving url: {skupni_url} \n \n")

    spajanje= urllib.request.urlopen(skupni_url)
    citanje=spajanje.read().decode()

    js=json.loads(citanje)
    #print(json.dumps(js,indent=4))
    
    try:
        grad=js['results'][0]['address_components'][2]['long_name']
        opcina=js['results'][0]['address_components'][3]['long_name']
        zupanija=js['results'][0]['address_components'][4]['long_name']
        drzava=js['results'][0]['address_components'][5]['long_name']

        lat=js['results'][0]["geometry"]['location']['lat']
        lng=js['results'][0]["geometry"]['location']['lng']

        print(f'Ovo su vasi podatci \n Drzava: {drzava} \n Zupanija:{zupanija} \n Opcina: {opcina} \n Grad: {grad} \n Lat: {lat} \n Lng: {lng}')
        break
    except :
        print("Nesto je poslo po krivu, ili ne mozemo naci adresu ili niste upisali dobre podatke \n")
