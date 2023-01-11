import re

tekst_neki='''
ovo je test di pise ko ima koliko godina
Josip ima 23 godine
Petar ima 58 godina
Mater ima 55 godina
'''

years= re.findall(r'\d{1,3}',tekst_neki)
names=re.findall(r'[A-Z][a-z]*',tekst_neki)
print(names)
print(years)

popis_svega_toga  = {}
for eachname in names:
    print(eachname)
    index_caller= names.index(eachname)
    index_commuter= years[index_caller]
    popis_svega_toga[eachname]=index_commuter

print(popis_svega_toga)




