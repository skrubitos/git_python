unesi_tekst=input('Unesite tekst: ')
lista_imena=unesi_tekst.split()
dit={}
najvecibroj = None
for broj in lista_imena:
    dit[broj]=dit.get(broj,0)+1
for broj in iter(dit.items()):
    if najvecibroj== None:
        najvecibroj=broj
    if najvecibroj<broj:
        najvecibroj=broj

print(f'\n Rijec koja se najvise puta pojavila je  {najvecibroj[0]}, pokazala se tocno {najvecibroj[1]} puta')

