from sonastik import *

sonad=[
    {'est': 'koer', 'rus': 'собака', 'eng': 'dog' },
    {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
    {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
    {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
    {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
] 
print(" ----- MENU -----\n",
      "1. Sõna tõlkimine;\n",
      "2. Sõnade lisamine;\n",
      "3. Sõnade parandamine;\n",
      "4. Näita kogu sõnastikku ja häälda;\n",
      "5. Sõnade tundmise test;\n",
      "6. Välja.")
while True:
    try:
        valik=int(input("Sisesta oma valik: "))
        if valik==1:
            while True:
                sona=input("Sisesta sõna: ").lower().strip()
                if sona.isalpha():break
                else:
                    print("Sõna peab koosnema ainult tähtedest!")
            while True:
                allikas=input("Sisesta, millise keelelt (est, eng, rus): ").strip().lower()
                if allikas=="est" or allikas=="rus" or allikas=="eng": break
                else: 
                    print("Vastus peab olema ainult 'est', 'eng' või 'rus'!")
            while True:
                siht=input("Sisesta, millisele keelele (est, eng, rus): ").strip().lower()
                if siht=="rus" or siht=="eng" or siht=="est": break
                else: 
                    print("Sisesta, millise keelelt 'est' või 'eng' või 'rus'!")
            tulemus=tolkija("sonad.txt", sona, allikas, siht)
            print(tulemus)
            break
        elif valik==2:
            lisa_sona("sonad.txt")
            break
        elif valik==3:
            muutmine_sona(sonad)
            break
        elif valik==4:
           vaata_sona("sonad.txt")
           break
        elif valik==5:
            test(sonad)
            break
        elif valik==6:
            break
        else:
            print("Sisestage number vahemikus 1 kuni 6!")
    except:
        print("Vastus peab olema numbriline!")

