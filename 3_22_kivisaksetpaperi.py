piste1 = 0
piste2 = 0
print("Tyhjä syöttö lopettaa pelin.")

while True:
    pelaaja1 = input("Pelaaja 1 valinta: ")
    if pelaaja1 == "":
        print("\n***Peli loppui***")
        print("Pelaaja 1 sai", piste1, "pistettä")
        print("Pelaaja 2 sai", piste2, "pistettä")
        break

    pelaaja2 = input("Pelaaja 2 valinta: ")

    if pelaaja1 == "kivi" and pelaaja2 == "paperi":
        print("-->Pelaaja 2 voitti\n")
        piste2 = piste2 + 1

    if pelaaja1 == "paperi" and pelaaja2 == "kivi":
        print("-->Pelaaja 1 voitti\n")
        piste1 = piste1 + 1

    if pelaaja1 == "kivi" and pelaaja2 == "sakset":
        print("-->Pelaaja 1 voitti\n") 
        piste1 = piste1 + 1

    if pelaaja1 == "sakset" and pelaaja2 == "kivi":
        print("-->Pelaaja 2 voitti\n") 
        piste2 = piste2 + 1

    if pelaaja1 == "sakset" and pelaaja2 == "paperi":
        print("-->Pelaaja 1 voitti\n")
        piste1 = piste1 + 1

    if pelaaja1 == "paperi" and pelaaja2 == "sakset":
        print("-->Pelaaja 2 voitti\n") 
        piste2 = piste2 + 1

    if pelaaja1 == pelaaja2:
        print("-->Tasapeli, ei pistettä kummallekaan.\n")
