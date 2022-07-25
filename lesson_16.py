import calendar
# Task_1


class Person:
    def __init__(self, name, age, place, hours_of_stay):
        self.name: str = name
        self.age: int = age
        self.place: str = place
        self.hours_of_stay: int = hours_of_stay
        self.marks = None
        self.salary = None

    def info(self):
        print('Name:', self.name,
               '\nAge:', self.age,
               '\nPlace:', self.place,
               '\nHours of stay:', self.hours_of_stay)


class Student(Person):
    def __init__(self, marks, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.marks = marks

    def total(self):
        print('You mark for today is:', self.marks)


class Teacher(Person):
    def __init__(self, salary, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.salary = salary

    def sum(self):
        print('The salary of this teacher is:', self.salary)


# Task_2

class Mathematician:

    def square_nums(self, lst1):
        squared = [x**2 for x in lst1]
        return squared

    def remove_positives(self, lst2):
        empty_array = []
        for num in lst2:
            if num < 0:
                empty_array.append(num)
        return empty_array

    def filter_leaps(self, lst3):
        new = []
        for i in lst3:
            if calendar.isleap(int(i)):
                new.append(i)
        return new


m = Mathematician()


# task_3


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:

    def __init__(self):
        self.product = None
        self.all = []
        self.income = 0

    def add(self, product: Product, amount):
        self.product = product
        item = {self.product.type,
                self.product.name,
                self.product.price * 0.3,
                amount
                }
        self.all.append(item)
    # def set_discount(self):
    #     ...
    #
    # def sell_product(self):
    #     ...
    #
    # def get_income(self):
    #     ...
    # def get_all_products(self):
    #     ...
    # def get_product_info(self, product_name):


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()


def main():

    # task 2
    print(m.square_nums([7, 11, 5, 4]))
    print(m.remove_positives([26, -11, -8, 13, -90]))
    print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
    # task3
    print(s.add(p, 10))
    print(s.add(p2, 300))


if __name__ == '__main__':
    main()
