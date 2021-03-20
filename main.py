import random
from os import system

# software onthoudt random getal tss 0 en 100
# variabelen
random = random.randrange(1, 101)
MaxPogingen = 5
AantalPogingen = 0
gokGetal = 0
naam = 0
nogEenKeer = ""

# START PROGRAMMA
_ = system('cls')

# Informatie tonen aan gebruiker
print("welkom, to this gokGame (powered by CorreCorneel)")
print("Je hebt 5 pogingen om een getal te raden tss de 0 en 100.")
naam = input("Wat is je naam? ")
print("hoi:" + naam)
nogEenKeer = input("Wil je een spelletje spelen (antwoord met yes of now):")
print()

# print("DEBUG: "+ str(random))
if (nogEenKeer == "yes") or (nogEenKeer == "yes"):
    while AantalPogingen < MaxPogingen:
        # BEGIN VAN DE WHILE
        # Vragen aan gebruiker voor ingave getal
        gokGetal = int(
            input("(" + str(AantalPogingen + 1) + "/" + str(MaxPogingen) + ")" +
                " Welk getal is het dat je denkt??  "))

        # Controleren of hoger, lager of juist.

        if gokGetal == random:
            print("proficiat, je hebt het juiste getal geraden!!")
            break
        else:
            print("Het is verkeerd. ", end="")
            if gokGetal < random:
                print("Je getal is te klein.")
                print()
            else:
                # Het is zeker groter
                print("Je getal is te groot.")
        AantalPogingen = AantalPogingen + 1

        if AantalPogingen == MaxPogingen:
            print("Spijtig, je pogingen zijn op.")
        # EINDE VAN DE WHILE
nogEenKeer = input("Wil je een spelletje spelen (antwoord met yes of now):")
if nogEenKeer == "now" or nogEenKeer == "Now":
    print ("oké dat de volgende keer")
#terug in programma, buiten de while
print("Programma is gedaan.")
