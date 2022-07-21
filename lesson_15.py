# # Task_1
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is", self.firstname, self.lastname, "and I’m",
              self.age, "years old")


person1 = Person('Karl', 'Johnson', 26)
# Task_2


class Dog:

    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age_factor * self.age

# Task_3


class TVController:
    CHANNELS = ["BBC", "Discovery", "TV1000"]
    current_channel = CHANNELS[0]
    # turns on the first channel

    def first_channel(self):
        self.current_channel = self.CHANNELS[0]
        print(self.current_channel)
    # turns on the last channel

    def last_channel(self):
        self.current_channel = self.CHANNELS[-1]
        print(self.current_channel)
    # turns on the channel based on the number in argument

    def turn_channel(self, args):
        if args == 1:
            self.current_channel = self.CHANNELS[0]
            print(self.current_channel)
        elif args == 2:
            self.current_channel = self.CHANNELS[1]
            print(self.current_channel)
        elif args == 3:
            self.current_channel = self.CHANNELS[2]
            print(self.current_channel)
    # prints out current channel

    def print_current_channel(self):
        if self.current_channel is not None:
            print(self.current_channel)


TVController1 = TVController()


# task_4


class Student:

    SCHOOL = 'California public school'
    MIN_AGE = 6
    MAX_AGE = 18

    def __init__(self, name, age, grade, teacher, pages_read, iq=80,
                 max_pages_read=20):
        self.name = name
        self.age = age
        self.grade = grade
        self.teacher = teacher
        self.pages_read = pages_read
        self.iq = iq
        self.max_pages_read = max_pages_read
    # shows info about the student

    def show_info(self):
        print(f'Name:', self.name, '\nAge:', self.age, '\nGrade',
              self.grade, '\nTeacher:', self.teacher, '\nPages read per day:',
              self.pages_read)

    def study(self):
        print('Student is studying')

    def bored(self):
        print('Student is bored, he needs to rest')
    # calculates the reading process based on the pages read and prints out the
    # amount of pages read or if student has to stop if the amount exceeds the
    # limit

    def reading_progress(self):
        self.pages_read += 10
        if self.pages_read > self.max_pages_read:
            print('You have read too many for today')
        else:
            print(f'Wow, you have read', self.pages_read, 'pages today!')
    # increases the IQ everytime once called

    def getting_smarter(self):
        self.iq += 1
        print(f'You are getting smarter - your IQ is', self.iq, 'now!')


class MiddleSchool(Student):
    MAX_PAGES_READ = 50

    # calculates the reading process based on the pages read and prints out the
    # amount of pages read or if student has to stop if the amount exceeds the
    # limit
    def reading_progress(self):
        self.pages_read += 10
        if self.pages_read > self.MAX_PAGES_READ:
            print('You have read too many for today')
        else:
            print(f'Wow, you have read', self.pages_read, 'pages today!')


class HighSchool(Student):
    MAX_PAGES_READ = 100

    # calculates the reading process based on the pages read and prints out the
    # amount of pages read or if student has to stop if the amount exceeds the
    # limit
    def reading_progress(self):
        self.pages_read += 20
        if self.pages_read > self.MAX_PAGES_READ:
            print('You have read too many for today')
        else:
            print(f'Wow, you have read', self.pages_read, 'pages today!')


student_1 = MiddleSchool('Peter', 10, 4, 'Ms.Mary', 20)
student_2 = HighSchool('Ben', 15, 9, 'Mr.Johnson', 40)


def main():
    # task_1
    person1.talk()
    # task_2
    pet = Dog(13)
    print(f'Your dog is', pet.human_age(), 'in human age!')
    # task_3
    TVController1.first_channel()
    TVController1.last_channel()
    TVController1.turn_channel(2)
    TVController1.print_current_channel()
    # task_4
    ...


if __name__ == '__main__':
    main()










