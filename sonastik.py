
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

# est=['koer', 'kass', 'maja', 'auto', 'päike']
# rus=['собака', 'кошка', 'дом', 'машина', 'солнце']
# eng=['dog', 'cat', 'house', 'car', 'sun']
sonad=[
    {'est': 'koer', 'rus': 'собака', 'eng': 'dog' },
    {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
    {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
    {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
    {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
]

def tolkija(sonad, allikas, siht, sona):
    for kirje in sonad:
        if kirje[allikas] == sona.lower():
            return kirje[siht]
    return "Слово не найдено!"

def lisa_sona(sonad):
    print("Добавляем новое слово в словарь!")
    uus_est = input("Введите слово на эстонском: ").strip().lower()
    uus_rus = input("Введите слово на русском: ").strip().lower()
    uus_eng = input("Введите слово на английском: ").strip().lower()
    
    sonad.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})
    print("Новое слово добавлено!")