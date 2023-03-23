# class Chelovek:
#     pi = 3.14  # public статический
#     __city = "Новосибирск"  # private статический
#     def __init__(self, height):
#         self.high = height  # public динамический
#         self.__vozrast = 23  # private динамический
#
# obj = Chelovek(175)
# print(obj.high)
# # print(Chelovek.pi)

# class Chelovek:
#     def __init__(self, height=175):
#         self.hi = height
#
# obj = Chelovek()
# print(obj.hi)
#
# obj2 = Chelovek(150)
# print(obj2.hi)

class Human:
    default_name = "Кира"
    default_age = 23
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 2500000
        self.__house = None

    def info(self):
        return (self.name, self.age, self.__money, self.__house)

    def earn_money(self):
        self.__money += 1000000

    def default_info(self):
        return Human.default_name, Human.default_age

    def __make_deal(self, dom):
        dom.final_price()
        if self.__money > dom.finall_price:
            self.__money -= dom.finall_price
            print("денег хватает")
            return True
        else:
            print("денег нема")
            return False

    def buy_house(self, dom):
        if self.__make_deal(dom):  # make_deal -> ценовой вопрос
            dom.owner = self.name  # владелец дома
            self.__house = dom  # владение домом
            print("хата приобретена")
        else:
            print(f"{'у тебя:'} {self.__money}, {'поработай ещё чуть-чуть!'}")


class House:
    def __init__(self, area="Pushkina", price=3510000):
        self.__area = area
        self.__price = price

    def final_price(self):
        from random import randint
        skidka = randint(5, 25)
        self.finall_price = self.__price - skidka / 100 * self.__price

violetta = Human()
dom1 = House()
violetta.buy_house(dom1)





