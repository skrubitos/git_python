'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
 Once 'done' is entered, print out the largest and smallest of the numbers.
  If the user enters anything other than a valid number catch it with a try/except and
   put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.
'''
pitanje = True
lista_upisa = []
najveci_broj = None
najmanji_brij = None
while pitanje is True:
    unesi_tekst = input("upisi broj: ")
    try:
        if unesi_tekst == "done":
            break
        lista_upisa.append(int(unesi_tekst))

        for i in lista_upisa:
            if najveci_broj is None:
                najveci_broj = i
            if i > najveci_broj:
                najveci_broj = i
        for x in lista_upisa:
            if najmanji_brij is None:
                najmanji_brij = x
            if x < najmanji_brij:
                najmanji_brij = x

    except ValueError:
        print("Invalid input")
print(f"Maximum is {najveci_broj}")
print(f"Minimum is {najmanji_brij}")
