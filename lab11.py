def zad1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"{self.cuisine_type} кухня в ресторане {self.restaurant_name}!")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    a = input("Введите название ресторана : ")
    b = input("Введите название кухни: ")
    res = Restaurant(a, b)
    res.describe_restaurant()
    res.open_restaurant()

def zad2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"{self.cuisine_type} кухня в ресторане {self.restaurant_name}!")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    res1 = Restaurant("Медальон", "Казахская")
    res2 = Restaurant("Пхали-хинкали", "Грузинская")
    res3 = Restaurant("Кафе-кебаб", "Восточная")

    res1.describe_restaurant()
    res1.open_restaurant()
    res2.describe_restaurant()
    res2.open_restaurant()
    res3.describe_restaurant()
    res3.open_restaurant()


def zad3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"{self.cuisine_type} кухня в ресторане {self.restaurant_name}! Рейтинг ресторана: {self.rating}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}")

    res1 = Restaurant("Медальон", "Казахская", 4.7)
    res2 = Restaurant("Пхали-хинкали", "Грузинская", 3.9)
    res3 = Restaurant("Кафе-кебаб", "Восточная", 2.8)

    res1.describe_restaurant()
    res2.describe_restaurant()
    res3.describe_restaurant()

    res1.update_rating(5)
    res1.describe_restaurant()
    res2.update_rating(4.5)
    res2.describe_restaurant()
    res3.update_rating(4.0)
    res3.describe_restaurant()


zad1()
input("Нажмите любую кнопку для продолжения")
zad2()
input("Нажмите любую кнопку для продолжения")
zad3()
