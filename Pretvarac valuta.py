#dobrodošlica
import time
def mjenjacnica():
    print ("Dobrodošli u pretvarač valuta ")
    time.sleep(0.25)
    print ("odaberite  prvu valutu valutu")
    time.sleep(0.5)
    print ("1. (E)UR")
    time.sleep(0.25)
    print ("2. (U)SD")
    time.sleep(0.25)
    print ("3. (H)RK")
    broj =input("Unesite slovo prve valute: ")

    # ako pokusamo unijeti broj, program ponovo trazi input slova
    while  broj.isdigit() :
        print("Trebate unijeti slovo a ne broj ")
        print("Molimo ponovite")
        broj= input("Unesite ponovno broj: ")

    # ako ne upisemo neki od ova 3 broja program nece nastaviti
    while broj.upper() != "E" and broj.upper() != "U" and broj.upper() != "H":
        print ("Pogrešan odabir")
        print ("Odaberite jednu od 3 ponuđene valute")
        broj= input("Valuta: ")

    # ako odaberemo euro
    if broj.upper() == "E":
        print ("Odabrali ste Euro")
        time.sleep(0.25)
        broj_d = input ("odaberite drugu valutu: ")

        while broj_d.isdigit():
            print("Trebate unijeti slovo a ne broj ")
            print("Molimo ponovite")
            broj_d = input("Unesite ponovno broj: ")

        # ako ne upisemo neki od ova 3 broja program nece nastaviti
        while broj_d.upper() != "E" and broj_d.upper() != "U" and broj_d.upper() != "H":
            print("Pogrešan odabir")
            print("Odaberite jednu od 3 ponuđene valute")
            broj_d = input("Valuta: ")

        #ako odaberemo E
        if broj_d.upper() == "E":
            print("Ako imate jednu čokoladu i želite je podijeliti s prijateljima ")
            time.sleep(1.5)
            print ("koliko će prijatelji dobiti čokolade")
            time.sleep(3)
            print ("0, jer vi ste pojeli čokoladu, a i nemate prijatelja")
            time.sleep(3)
            print("stvarno ne znate koliko X Eura vrijedi X Eura")
            mjenjacnica()
        #ako odaberemo U
        elif broj_d.upper() == "U":
            print("Odabrali ste USD:")
            EUR = input("Odaberite količinu eura: ")
            USD = float(EUR) * 1.0559
            print(USD, "USD")
            mjenjacnica()
        #ako odaberemo H
        elif broj_d.upper() == "H":
            print("Odabrali ste HRK:")
            EUR = input("Odaberite količinu eura: ")
            HRK = float(EUR) * 7.543
            print(HRK, "kuna")
            mjenjacnica()


    #ako odaberemo dolar
    if broj.upper() == "U":
        print ("Odabrali ste USD")
        time.sleep(0.25)
        broj_d = input ("odaberite drugu valutu: ")

        while broj_d.isdigit():
            print("Trebate unijeti slovo a ne broj ")
            print("Molimo ponovite")
            broj_d = input("Unesite ponovno broj: ")

        # ako ne upisemo neki od ova 3 broja program nece nastaviti
        while broj_d.upper() != "E" and broj_d.upper() != "U" and broj_d.upper() != "H":
            print("Pogrešan odabir")
            print("Odaberite jednu od 3 ponuđene valute")
            broj_d = input("Valuta: ")

        #ako odaberemo U
        if broj_d.upper() == "U":
            print("Ako imate jednu čokoladu i želite je podijeliti s prijateljima ")
            time.sleep(1.5)
            print ("koliko će prijatelji dobiti čokolade")
            time.sleep(3)
            print ("0, jer vi ste pojeli čokoladu, a i nemate prijatelja")
            time.sleep(3)
            print("stvarno ne znate koliko X Dolara vrijedi X Dolara")
            mjenjacnica()
        #ako odaberemo E
        elif broj_d.upper() == "E":
            print("Odabrali ste EUR:")
            USD = input("Odaberite količinu dolara: ")
            EUR = float(USD) * 0.950278
            print(USD, "EUR")
            mjenjacnica()
        # ako odaberemo H
        elif broj_d(upper) == "H":
            print("Odabrali ste HRK:")
            USD = input("Odaberite količinu dolara: ")
            HRK = float(USD) *   7.16399
            print(HRK, "kuna")
            mjenjacnica()


    #ako odaberemo kunu
    if broj.upper() == "H":
        print ("Odabrali ste Kunu")
        time.sleep(0.25)
        broj_d = input ("odaberite drugu valutu: ")

        while broj_d.isdigit():
            print("Trebate unijeti slovo a ne broj ")
            print("Molimo ponovite")
            broj_d = input("Unesite ponovno broj: ")

        # ako ne upisemo neki od ova 3 broja program nece nastaviti
        while broj_d.upper() != "E" and broj_d.upper() != "U" and broj_d.upper() != "H":
            print("Pogrešan odabir")
            print("Odaberite jednu od 3 ponuđene valute")
            broj_d = input("Valuta: ")

    # ako odaberemo E"
        if broj_d.upper() == "E":
            print("Ako imate jednu čokoladu i želite je podijeliti s prijateljima ")
            time.sleep(1.5)
            print ("koliko će prijatelji dobiti čokolade")
            time.sleep(3)
            print ("0, jer vi ste pojeli čokoladu, a i nemate prijatelja")
            time.sleep(3)
            print("stvarno ne znate koliko X Kuna vrijedi X Kuna")
            mjenjacnica()
    # ako odaberemo U
        elif broj_d.upper() == "U":
            print("Odabrali ste USD:")
            HRK = input("Odaberite količinu kuna: ")
            USD = float(HRK) * 0.139587
            print(USD, "USD")
            mjenjacnica()
    # ako odaberemo E
        elif broj_d.upper() == "E":
            print("Odabrali ste EUR:")
            EUR = input("Odaberite količinu kuna: ")
            HRK = float(EUR) * 0.132431
            print(HRK, "EUR")
            mjenjacnica()
mjenjacnica()
