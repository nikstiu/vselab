import re
import random
from collections import UserDict

dict = UserDict()

filename = "Z:\Тюрин\doplab1\synonyms.txt"


def Save(key, value):                               #Определяется функция Save, которая добавляет новый синоним в файл.
    with open(filename, 'a') as file:
        file.write("\n")
        file.write("{} - {}".format(key, value))


with open(filename, 'r') as file:
    lines = file.read().splitlines()
    for item in lines:                                  #Для каждой строки из файла определяется ключ (слово) и значение (синонимы).

        key = item.split(" - ")[0].lower()

        values = item.split(" - ")[1:]

        if (len(values) > 0):                           #Если значение содержит несколько синонимов, они разделяются по символу ";" и сохраняются в виде списка.
            values = values[0].strip()
            if (values.split(";") is None):
                value = values
            else:
                value = list(values.split(";"))

            value = [x.strip(' ') for x in value]   #Список синонимов очищается от пробелов.

            if (dict.get(key) is None):     #Если ключ уже есть в словаре, то список синонимов добавляется к уже имеющимся, иначе создается новая запись в словаре.
                dict[key] = value
            else:
                dict[key] += value

while True:                             #В бесконечном цикле запрашивается у пользователя слово.
    s = input("Введите слово: ")
    if s:                           #Если слово не пустое, оно приводится к нижнему регистру и проверяется на наличие в словаре.
        s = s.strip().lower()

        if (dict.get(s) is None):
            print('Нет синонимов для слова {} '.format(s))      #Если для данного слова нет синонимов, выводится соответствующее сообщение.
        else:

            syn = dict[s]

            print('Синоним: {}'.format(random.choice(syn)))                #Если для слова есть синонимы, выбирается случайный синоним из списка.

        res = input('Добавить новый синоним {} [Y] - да ? '.format(s)).strip()          #Запрашивается у пользователя желание добавить новый синоним.
        if res.lower() == 'y':
            wsyn = input('Введите синоним: ').strip().lower()             ##Если пользователь соглашается добавить новый синоним, запрашивается его ввод и происходит добавление в словарь и файл синонимов.
            if wsyn:
                if (dict.get(s) is None):
                    dict[s] = wsyn
                    Save(s, wsyn)
                else:
                    if (wsyn not in syn):
                        syn.append(wsyn)
                        dict[s] = list(set(syn))
                        Save(s, wsyn)
