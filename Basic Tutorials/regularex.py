import re
listaa=[]
with open("suma.txt") as f:
    for x in f:
        y= re.findall("[0-9]+",x)
        if len(y)<1:
            continue
        try:
            listaa.append(y[0])
        except IndexError:
            pass
        try:
            listaa.append(y[1])
        except IndexError:
            pass
        try:
            listaa.append(y[2])
        except IndexError:
            pass
        try:
            listaa.append(y[3])
        except IndexError:
            pass
        try:
            listaa.append(y[4])
        except IndexError:
            pass
        try:
            listaa.append(y[5])
        except IndexError:
            pass

suma_svega= 0
for x in listaa:
    suma_svega+= int(x)
print(suma_svega)

