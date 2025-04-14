import json
import random

def loe(fail:str)->dict:
    f=open(fail,'r',  encoding="utf-8-sig")
    sonad=[]
    for rida in f:
        sonad.append(rida.strip())
    f.close()
    return sonad

# sonad = [
#     {'est': 'koer', 'rus': 'собака', 'eng': 'dog'},
#     {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
#     {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
#     {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
#     {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
# ]
# def kirjuta_failisse(fail:str,d:dict):
#     f=open(fail, 'w', encoding="utf-8-sig")
#     for line in d:
#         f.write(str(line)+'\n')
#     f.close()
# kirjuta_failisse("sonad.txt",sonad)


#1
def tolkija(fail:str, sona, allikas, siht)->any:
    """Sõnade tõlkimine
    Funktsioon tõlgib sõna, mille kasutaja sisestab.
    """
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad = []
        for rida in f:
            sonad.append(eval(rida.strip()))
    for kirje in sonad:
        if kirje[allikas].lower() == sona.lower():
            return kirje[siht]

#2
def lisa_sona(fail:str):
    """Lisa sõna
     Funktsioon lisab kasutaja poolt sisestatud sõnad.
    :param list fail
    """
    est_sona = input("Sõna eesti keeles: ").strip().lower()
    rus_sona = input("Sõna vene keeles: ").strip().lower()
    eng_sona = input("Sõna on inglise keeles: ").strip().lower()

    uus_sona = {'est': est_sona, 'rus': rus_sona, 'eng': eng_sona}
    with open(fail, 'a', encoding="utf-8-sig") as f :
        f.write(str(uus_sona)+'\n')
    print("Sõna on lisatud!")

#3
def muutmine_sona(fail:str):
    """Sõna muutmine
    Funktsioon muudab sõna (kasutaja valib, mida muuta).
    :param list sonad: sõnade nimekiri
    """
    while True:
        sona = input("Sisestage sõna, mida soovite muuta: ")
        if not sona.isalpha():
            print("Sõna peab sisaldama ainult tähti!")
            continue
        leitud = None
        for kirje in sonad:
            if sona.lower() in [kirje["est"].lower(), kirje["rus"].lower(), kirje["eng"].lower()]:
                leitud = kirje
                break
        if leitud:
            break
        else:
            print("Seda sõna ei leitud sõnastikust!")
    while True:
        keel = input("Mis keeles on see sõna? (eng, rus, est): ").lower()
        if keel in ["eng", "rus", "est"]:
            uus_sona = input("Sisesta uus sõna: ")
            if uus_sona.isalpha():
                leitud[keel] = uus_sona
                print("Sõna on muudetud!")
                print("Uus kirje:", leitud)
                break
            else:
                print("Uus sõna peab sisaldama ainult tähti!")
        else:
            print("Palun vali keel: 'eng', 'est' või 'rus'.")


#4
def vaata_sona(fail:str):
    """Sõnavara vaatamine ja kuulamine
    Funktsioon näitab ja häälestab kogu sõnastiku
    :param list sonad
    """
    print("Sõnastik:")
    number = 1
    with open(fail, 'a', encoding="utf-8-sig") as f :
        sonad=[json.loads(rida.strip()) for rida in f]
    for kirje in sonad:
        text = str(number) + ". Eesti: " + kirje['est'] + " Vene: " + kirje['rus'] + " Inglise: " + kirje['eng']
        print(text)
        number = number + 1
    print(" ")

#5
def test(sonad):
    """Test
    :param list sonad
    """
    print("Test")
    print("Reeglid: ma annan teile valitud keeles sõna ja te tõlgite selle teise keelde. Väljumiseks kirjutage „exit“.")
    õigesti = 0
    kõik = 0
    while True:
        random_sõnastik = random.choice(sonad)
        while True:
            language = input("Valige keel, millest tõlkida (eng, est, rus): ").strip().lower()
            if language == 'eng' or language == 'rus' or language == 'est':
                break
            else:
                print("Keel peab olema: 'eng', 'est' või 'rus'!")
        random_sone = random_sõnastik[language]
        print("Juhuslik sõna:", random_sone)
        while True:
            language1 = input("Valige keel, millesse tõlkida (eng, est, rus): ").strip().lower()
            if language1 == 'eng' or language1 == 'rus' or language1 == 'est':
                if language1 != language:
                    break
                else:
                    print("Valige keel, millesse soovite tõlkida")
            else:
                print("Keel peab olema: 'eng', 'est' või 'rus'!")
        print(f"Tõlgi sõna {random_sone} suust suhu {language} keelel {language1}")
        vastus = input("Teie vastus (või „väljumine“, et väljuda): ").strip().lower()
        if vastus == "exit":
            break
        kõik = kõik + 1
        õigest_vastus = random_sõnastik[language1]
        if vastus == õigest_vastus:
            print("Õige!")
            õigesti = õigesti + 1
        else:
            print(f"Vale! Õige vastus on: {õigest_vastus}")
    print("Test on lõppenud!")
    print(f"Õiged vastused: {õigesti} / {kõik}")
