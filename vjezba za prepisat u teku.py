#stvaramo dict u kojeg cemo kasnije stavljat rijeci i broj njihovih ponavljanja
ura={}
with open("mbox-short.txt") as f:
    for loop in f:
        if loop.startswith("From "): #uzimamo samo one rijeci kojima linija pocinje sa From: jer se u njima trazi informacija koju mi trazimo
            ura[loop.split()[5][0:2]]=ura.get(loop.split()[5][0:2],0)+1 #dict[key]=sada ova funkcija get trazi taj key te ako ga ne nadje daje mu default
                                                                        # vrijednost 0, te svaki iduci put kad ga nadje dodaje mu po jednu vrijednost
ura_list=[] #obrnit cemo key i value jer zelimo kasnije sortat po broju ponavljanja a ne po alfabetickom orderu
for k,v in ura.items():
    ura_list.append((k,v))

sortitano= sorted(ura_list)

for x in sortitano:
    print(x[0],x[1])


