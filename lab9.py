import os

from PIL import Image, ImageFilter


def zad1():
    os.chdir("/Users/maslina/Downloads/PycharmProjects 2/lab7")
    with Image.open("img1_1.jpg") as img:
        img.load()
        a = "changed"
        img = img.filter(ImageFilter.SHARPEN)
        img.save(f"/Users/maslina/Downloads/PycharmProjects 2/Лаба 9/img1{a}.jpg")
    with Image.open("img2_2.jpg") as img:
        img.load()
        a = "changed"
        img2 = img.filter(ImageFilter.SHARPEN)
        img2.save(f"/Users/maslina/Downloads/PycharmProjects 2/Лаба 9/img2{a}.jpg")
    with Image.open("img3_3.jpg") as img:
        img.load()
        a = "changed"
        img3 = img.filter(ImageFilter.SHARPEN)
        img3.save(f"/Users/maslina/Downloads/PycharmProjects 2/Лаба 9/img3{a}.jpg")
    with Image.open("img4_4.jpg") as img:
        img.load()
        a = "changed"
        img4 = img.filter(ImageFilter.SHARPEN)
        img4.save(f"/Users/maslina/Downloads/PycharmProjects 2/Лаба 9/img4{a}.jpg")
    with Image.open("img5_5.jpg") as img:
        img.load()
        a = "changed"
        img5 = img.filter(ImageFilter.SHARPEN)
        img5.save(f"/Users/maslina/Downloads/PycharmProjects 2/Лаба 9/img5{a}.jpg")

def zad2():
    a = 0
    os.chdir("/Users/maslina/Downloads/PycharmProjects 2/lab7")
    with Image.open("img1_1.jpg") as img:
        split_tup = os.path.splitext('img1_1.jpg')
        imgform = split_tup[1]
        if imgform := (".jpg"):
            a += 1
            img.load()
            img1 = img.filter(ImageFilter.SHARPEN)
            img1.save(f"/Users/maslina/Downloads/PycharmProjects 2/Лаба 9/img1-{a}.jpg")
    with Image.open("img2_2.jpg") as img:
        split_tup = os.path.splitext('img2_2.jpg')
        imgform = split_tup[1]
        if imgform := (".jpg"):
            a += 1
            img.load()
            img2 = img.filter(ImageFilter.SHARPEN)
            img2.save(f"/Users/maslina/Downloads/PycharmProjects 2/Лаба 9/img2-{a}.jpg")
    with Image.open("img3_3.jpg") as img:
        split_tup = os.path.splitext('img3_3.jpg')
        imgform = split_tup[1]
        if imgform := (".jpg"):
            a += 1
            img.load()
            img3 = img.filter(ImageFilter.SHARPEN)
            img3.save(f"/Users/maslina/Downloads/PycharmProjects 2/Лаба 9/img3-{a}.jpg")
    with Image.open("img4_4.jpg") as img:
        split_tup = os.path.splitext('img4_4.jpg')
        imgform = split_tup[1]
        if imgform := (".jpg"):
            a += 1
        img.load()
        img4 = img.filter(ImageFilter.SHARPEN)
        img4.save(f"/Users/maslina/Downloads/PycharmProjects 2/Лаба 9/img4-{a}.jpg")
    with Image.open("img5_5.jpg") as img:
        split_tup = os.path.splitext('img5_5.jpg')
        imgform = split_tup[1]
        if imgform := (".jpg"):
            a += 1
        img.load()
        img5 = img.filter(ImageFilter.SHARPEN)
        img5.save(f"/Users/maslina/Downloads/PycharmProjects 2/Лаба 9/img5-{a}.jpg")


def zad3():
    os.chdir("/Users/maslina/Downloads/PycharmProjects 2/Лаба 9")
    with open("buy.csv", encoding="utf=8") as c:
        lines = c.readlines()
        s = 0
        print("Нужно купить: ")
        for line in lines[1:]:
            pr, kolvo, price = line.strip().split(',')
            s += int(kolvo) * int(price)
            print(f"{pr} - {kolvo} шт. за {price} руб.")
        print(f"Итоговая сумма: {s} руб.")

zad2()