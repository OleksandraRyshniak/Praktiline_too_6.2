from sonastik import *
# 📖 Практическая работа: Словарь
# Трёхъязычный словарь ✅
# Эстонский 🇪🇪
# Русский 🇷🇺
# Английский 🇬🇧
# Программа должна позволять:
# Перевод с любого языка на другой
# Добавление слов, если слова нет
# Исправление, если слово указано неверно
# Проверка знаний (тест) — выбор направления (например, эстонский → русский, русский → английский и т.д.)
# Бонус: Text-to-Speech (с использованием модуля pyttsx3)

# План программы:
# *С использованием списков:
# est = ['koer', 'kass', 'maja', 'auto', 'päike']
# rus = ['собака', 'кошка', 'дом', 'машина', 'солнце']
# eng = ['dog', 'cat', 'house', 'car', 'sun']

# Формируем словарь на основе списков:

# sonastik = []
# for e, r, g in zip(est, rus, eng):
#     sonastik.append({'est': e, 'rus': r, 'eng': g})

# * Или используем список списков:

# # Начальные данные для трёх языков
# sonad = [
#     {'est': 'koer', 'rus': 'собака', 'eng': 'dog'},
#     {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
#     {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
#     {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
#     {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
# ]

# def tolkija(sonad, allikas, siht, sona):
#     for kirje in sonad:
#         if kirje[allikas] == sona.lower():
#             return kirje[siht]
#     return "Слово не найдено!"
# def lisa_sona(sonad):
#     print("Добавляем новое слово в словарь!")
#     uus_est = input("Введите слово на эстонском: ").strip().lower()
#     uus_rus = input("Введите слово на русском: ").strip().lower()
#     uus_eng = input("Введите слово на английском: ").strip().lower()
    
#     sonad.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})
#     print("Новое слово добавлено!")

# Идеи для функций (всего не менее 12!):

#     loo_sonastik() — создаёт словарь для трёх языков

#     otsi_sona() — ищет слово на любом языке и отображает переводы на другие

#     lisa_sona() — добавляет новое слово на трёх языках

#     paranda_sona() — исправляет существующее слово

#     kuva_sonad() — отображает весь словарь

#     vali_keelte_suund() — запрашивает у пользователя, с какого языка на какой он хочет перевести

#     testi_teadmisi() — проверка знаний с использованием случайных слов

#     kuva_tulemus() — отображает итоговый результат теста

#     kysi_kasutajalt_sisestus() — запрашивает ввод и проверяет на пустоту

#     text_to_speech() — произносит слово вслух

#     kuva_menuu() — отображает меню и инструктирует пользователя

#     valjasta_tervitus() — программа приветствует пользователя в начале

# Структура программы:

#     sonastik.py — все функции и данные

#     main.py — основная логика и меню

# Дополнительная возможность:

# Можно сделать так, чтобы при добавлении нового слова оно сразу добавлялось в список sonastik, после чего его можно было бы немедленно использовать для перевода или тестирования!
sonad=[
    {'est': 'koer', 'rus': 'собака', 'eng': 'dog' },
    {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
    {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
    {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
    {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
] 
# Программа должна позволять:
# Перевод с любого языка на другой
# Добавление слов, если слова нет
# Исправление, если слово указано неверно
# Проверка знаний (тест) — выбор направления (например, эстонский → русский, русский → английский и т.д.)
# Бонус: Text-to-Speech (с использованием модуля pyttsx3)
 
print(" ----- MENU -----\n",
      "1. Перевод слова;\n",
      "2. Добавление слов;\n",
      "3. Исправление слов;\n",
      "4. Показать весь словарь;\n",
      "5. Тест на знание слов;\n",
      "6. Озвучить весь словарь;\n",
      "7. Выйти.")
while True:
    try:
        valik=int(input("Sisesta oma valik: "))
        if valik==1:
            while True:
                sona=input("Введите слово: ").lower().strip()
                if sona.isalpha():break
                else:
                    print("Слово должно состоять только из букв!")
            while True:
                allikas=input("введите с какого языка (est, eng, rus): ").strip()
                if allikas=="est" or allikas=="rus" or allikas=="eng": break
                else: 
                    print("Ответ должен быть только 'est' või 'eng' või 'rus'!")
            while True:
                siht=input("введите на какой язык (est, eng, rus): ").strip()
                if siht=="rus" or siht=="eng" or siht=="est": break
                else: 
                    print("Ответ должен быть только 'est' või 'eng' või 'rus'!")
            tulemus=tolkija(sonad, allikas, siht, sona)
            print(tulemus)
        elif valik==2:
            lisa_sona(sonad)
        elif valik==3:
            print()
        elif valik==4:
            print(vaata_sona(sonad))
        elif valik==5:
            print()
        elif valik==6:
            print()
        elif valik==7:
            break
        else:
            print("Sisestage number vahemikus 1 kuni 6!")
    except:
        print("Vastus peab olema numbriline!")

