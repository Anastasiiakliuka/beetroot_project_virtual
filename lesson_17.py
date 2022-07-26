# task_1
class Animal:

    def __init__(self, name):
        self.name = name

    def talk(self):
        return

    def lay_down(self):
        return


class Dog(Animal):
    def talk(self):
        print('Woof Woof!')

    def lay_down(self):
        print('The pet lays down')

    def stick(self):
        print('Here is the stick!')


class Cat (Animal):
    def talk(self):
        print('Meow!')


animals = [Dog('Spike'), Cat('Mia')]
for animal in animals:
    animal.talk()


def dog_command():
    temp_var = Dog('Peter')
    user_input = input('Say "talk" if you want me to talk!\n')
    if user_input == 'talk':
        temp_var.talk()
    user_input_2 = input('Say "lay down" if you want me to lay down\n')
    if user_input_2 == 'lay down':
        temp_var.lay_down()
    user_input_3 = input('Say "apport" if you want me to bring the stick!\n')
    if user_input_3 == 'apport':
        temp_var.stick()


def cat_command():
    temp_var = Cat('Mia')
    user_input_cat = input('Say "talk" if you want me to talk\n')
    if user_input_cat == 'talk':
        temp_var.talk()

# task_3


class Fraction (int):

    def __add__(self, other):
        return self + other, self + other

    def __sub__(self, other):
        return self - other, self - other

    def __mul__(self, other):
        return self * other, self * other

    def __div__(self, other):
        return self // other, self // other


def main():

    # task_1
    dog_command()
    cat_command()

    # task_3
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    c = x + y
    print(c)


if __name__ == '__main__':
    main()
