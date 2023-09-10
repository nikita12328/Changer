# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from task1.my_classes.Person import Person


class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, name, surname, patronymic, age, id):
        super().__init__(name, surname, patronymic, age)
        self.id = id

    def get_level(self):
        return sum(int(num) for num in str(self.id)) % self.MAX_LEVEL


if __name__ == '__main__':
    employee1 = Employee("Константин", "Ситников", "Ситников", 23, 12345)
    print(employee1.get_level())
