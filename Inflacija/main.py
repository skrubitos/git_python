#10 km traku u 42minute i 42sekunde

def sec_to_min(sec):
    min= int(sec)/60
    return min

def full_min(minute,sec):
    full = sec_to_min(sec)+ minute
    return full
def km_po_min():
    avarage=  10/full_min(42, 42)
    km_h= 10/(full_min(42, 42)/60)
    print("Vasa prosjecna brzina je {:.2f} km/h".format(km_h))
    print("{:.2f} kilometra po minuti ".format(avarage))

km_po_min()