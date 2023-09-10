Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Person:
    def __init__(self, name, surname, patronymic, age):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._age = age

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


if __name__ == '__main__':
    person1 = Person('Василий', 'Рыжов', 'Рыжов', 23)
    print(person1)
    print(person1.get_age())
    person1.birthday()
    print(person1.get_age())
    print(person1._age)
