
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
def tolkija(fail:str, sona:str )->any:
    """Sõnade tõlkimine
    Funktsioon tõlgib sõna, mille kasutaja sisestab.
    :param fail str
    :param sona str: Sisesta kasutaja
    """
    h=("Seda sõna ei ole sõnaraamatus!")
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad = []
        for rida in f:
            sonad.append(eval(rida.strip()))
    for kirje in sonad:
        if kirje['est'].lower() == sona.lower():
            h=(f"{sona} - rus: {kirje['rus']}, eng: {kirje['eng']}")
            break
        elif kirje['rus'].lower()==sona.lower():
            h=(f"{sona} - est: {kirje['est']}, eng: {kirje['eng']}")
            break
        elif kirje['eng'].lower()==sona.lower():
            h=(f"{sona} -  est: {kirje['est']}, rus: {kirje['rus']}")
            break
    return h

#2
def lisa_sona(fail:str):
    """Lisa sõna
     Funktsioon lisab kasutaja poolt sisestatud sõnad.
    :param str fail
    """
    while True:
        est_sona=str(input("Sisesta sona eesti keeles:")).lower().strip()
        if est_sona.isalpha(): break
        else: 
            print("Sõna peab koosnema ainult tähtedest!")
    while True:
        rus_sona=str(input("Sisesta sona vene keeles:")).lower().strip()
        if rus_sona.isalpha(): break
        else:
             print("Sõna peab koosnema ainult tähtedest!")
    while True:
        eng_sona=str(input("Sisesta sona inslise keeles:")).lower().strip()
        if eng_sona.isalpha(): break
        else: 
             print("Sõna peab koosnema ainult tähtedest!")

    uus_sona = {'est': est_sona, 'rus': rus_sona, 'eng': eng_sona}
    with open(fail, 'a', encoding="utf-8-sig") as f :
        f.write(str(uus_sona)+'\n')
    print("Sõna on lisatud!")

#3
def muutmine_sona(fail:str):
    """Sõna muutmine
    Funktsioon muudab sõna (kasutaja valib, mida muuta).
    :param str fail
    """
    h=("Seda sõna ei ole sõnaraamatus!")
    while True:
        sona = input("Sisestage sõna, mida soovite muuta: ")
        if sona.isalpha(): break
        else:
            print("Sõna peab sisaldama ainult tähti!")
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad = []
        for rida in f:
            sonad.append(eval(rida.strip()))
        indeks=-1
        i=0
        while i< len(sonad):
            kirje=sonad[i]
            if sona.lower() in [kirje["est"].lower(), kirje["rus"].lower(), kirje["eng"].lower()]:
                h=(f"est: {kirje['est']}, rus: {kirje['rus']}, eng: {kirje['eng']}")
                indeks=i
                break
            i+=1
        print(h)
    while True:
        uus_sona_ee=str(input("Sisesta sona eesti keeles:")).lower().strip()
        if uus_sona_ee.isalpha(): break
        else: 
            print("Sõna peab koosnema ainult tähtedest!")
    while True:
        uus_sona_ru=str(input("Sisesta sona vene keeles:")).lower().strip()
        if uus_sona_ru.isalpha(): break
        else:
             print("Sõna peab koosnema ainult tähtedest!")
    while True:
        uus_sona_eng=str(input("Sisesta sona inslise keeles:")).lower().strip()
        if uus_sona_eng.isalpha(): break
        else: 
             print("Sõna peab koosnema ainult tähtedest!")
    sonad[i] = {'est': uus_sona_ee, 'rus': uus_sona_ru, 'eng': uus_sona_eng}
    with open(fail, 'w', encoding="utf-8-sig") as f :
        for kirje in sonad:
            f.write(str(kirje)+'\n')
    print("Sõna on muudatud!")



#4
def vaata_sona(fail:str):
    """Sõnavara vaatamine ja kuulamine
    Funktsioon näitab ja häälestab kogu sõnastiku
    :param str fail
    """
    print("Sõnastik:")
    number = 1
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad = []
        for rida in f:
            sonad.append(eval(rida.strip()))
    for kirje in sonad:
        text = str(number) + ". Eesti: " + kirje['est'] + " Vene: " + kirje['rus'] + " Inglise: " + kirje['eng']
        print(text)
        number = number + 1
    print(" ")

#5
def test(fail:str):
    """Test
    :param str fail
    """
    with open(fail, 'r', encoding='utf-8-sig') as f:
        sonad = []
        for rida in f:
            sonad.append(eval(rida.strip()))
    print("Test")
    print("Reeglid: ma annan teile valitud keeles sõna ja te tõlgite selle teise keelde. Väljumiseks kirjutage „exit“.")
    õigesti = 0
    kõik = 0
    while True:
        random_sõnastik = random.choice(sonad)
        while True:
            language = str(input("Valige keel, millest tõlkida (eng, est, rus): ")).strip().lower()
            if language == 'eng' or language == 'rus' or language == 'est':
                break
            else:
                print("Keel peab olema: 'eng', 'est' või 'rus'!")
        random_sone = random_sõnastik[language]
        while True:
            language1 = str(input("Valige keel, millesse tõlkida (eng, est, rus): ")).strip().lower()
            if language1 == 'eng' or language1 == 'rus' or language1 == 'est':
                if language1 != language:
                    break
                else:
                    print("Valige keel, millesse soovite tõlkida")
            else:
                print("Keel peab olema: 'eng', 'est' või 'rus'!")
        print(f"Tõlgi sõna '{random_sone}' suust suhu '{language}' keelel '{language1}'")
        vastus = input("Teie vastus (või „exit“, et väljuda): ").strip().lower()
        if vastus == "exit":
           print(f"Õiged vastused: {õigesti} / {kõik}")
           print("Test on lõppenud!")
           break
        kõik = kõik + 1
        õigest_vastus = random_sõnastik[language1]
        if vastus == õigest_vastus:
            print("Õige!")
            õigesti = õigesti + 1
        else:
            print(f"Vale! Õige vastus on: {õigest_vastus}")

