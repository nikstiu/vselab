def p1():
    pass
word = []
while(words := str(input('Введите слово: '))) !="stop":
    word.append(words)
print (" ".join(word))



def p2():
    pass
w1 = []
while(w1 := str(input('Введите слово: '))) !="stop":
    if "ф" in w1 or "Ф" in w1:
        print("Ого, это редкое слово")
    else:
        print("Эх, это не очень редкое слово")

def p3():
    pass
z = 0
n = 0
from random import randint
while True:
        a = randint(1, 11)
        b = randint(1, 11)
        print(f'{a} + {b} =', end='')
        res = input()
        while not res.isdigit() and res != "stop":
            res = input()
            if res == "stop":
                break
        res = int(res)
        if a + b == res:
            z+= 1
            print("Правильно!")
        else:
            print("Ответ неправильный ")
            n += 1
        if n == 3:
            print("Игра закончена. Правильных ответов: ", z)
            break
p2(), p3()








