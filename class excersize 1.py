class House:

    def __init__(self, area = 0, price = 0):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)

    def info(self):
        print(f'Площадь: {self._area}')
        print(f'Цена: {self._price}')
        print()

    @classmethod
    def SmallHouse(cls, price = 0):
        SmallHouse = cls(40, price)
        return SmallHouse

class Human:
    default_name = 'Venya'
    default_age = '29'

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = House()

    def info(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Деньги: {self.__money}')
        print(f'Дом: {self.__house}')
        print()

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}')
        print(f'Default age: {Human.default_age}')
        print()

    def earn_money(self):
        self.__money += 1000

    def __make_deal(self, home, price):
        self.__money -= price
        self.__house = home

    def buy_house(self, home, discount=0):
        if self.__money > home._price * (1 - discount / 100):
            self.__make_deal(home, home._price * (1 - discount / 100))
            print('Сделка завершена')
            print()
        else:
            print('Не хватает денег на покупку этого дома')
            print()

def main():
    Human.default_info()
    Alex = Human('Alexey', 33)
    Alex.info()
    little_house = House.SmallHouse(200)
    little_house.info()
    Alex.buy_house(little_house, 0)
    Alex.earn_money()
    Alex.buy_house(little_house, 10)
    Alex.info()

if __name__ == '__main__':
    main()