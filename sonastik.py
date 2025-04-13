import pyttsx3
import random

# Мой список словарей (определяю только один раз)
sonad = [
    {'est': 'koer', 'rus': 'собака', 'eng': 'dog'},
    {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
    {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
    {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
    {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
]
#1
def tolkija(sonad, allikas, siht, sona):
    """Sõnade tõlkimine
    Funktsioon tõlgib sõna, mille kasutaja sisestab.
    """
    for kirje in sonad:
        if kirje[allikas] == sona.lower():
            print("Tõlkimine:", kirje[siht])
            return kirje[siht]
    return "Sõna ei leitud!"

#2
def lisa_sona(sonad):
    """Lisa sõna
     Funktsioon lisab kasutaja poolt sisestatud sõnad.
    :param list sonad
    """
    est_sona = input("Sõna eesti keeles: ").strip().lower()
    rus_sona = input("Sõna vene keeles: ").strip().lower()
    eng_sona = input("Sõna on inglise keeles: ").strip().lower()

    uus_sona = {'est': est_sona, 'rus': rus_sona, 'eng': eng_sona}
    sonad.append(uus_sona)
    print("Sõna on lisatud!")

#3
def muutmine_sona(sonad):
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
def vaata_sona(sonad):
    """Sõnavara vaatamine ja kuulamine
    Funktsioon näitab ja häälestab kogu sõnastiku
    :param list sonad
    """
    print("Sõnastik:")
    number = 1
    mootor = pyttsx3.init()
    for kirje in sonad:
        text = str(number) + ". Eesti: " + kirje['est'] + " Vene: " + kirje['rus'] + " Inglise: " + kirje['eng']
        print(text)
        mootor.say(text)
        number = number + 1
    mootor.runAndWait()
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
