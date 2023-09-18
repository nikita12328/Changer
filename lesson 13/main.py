class PasswordTooShortException(Exception):
    def __init__(self, password_length):
        super().__init__(
            f"Пароль слишком короткий. Минимальная длина пароля - 6 символов. Введено символов: {password_length}")


class InvalidBirthDateException(Exception):
    def __init__(self, birth_year):
        super().__init__(
            f"Недопустимая дата рождения. Год рождения должен быть в пределах 1920-2022. Введено: {birth_year}")


class User:
    def __init__(self, login, password, name, birth_date):
        self.login = login
        self.password = password
        self.name = name
        self.birth_date = birth_date

    def change_password(self, new_password):
        if len(new_password) < 6:
            raise PasswordTooShortException(len(new_password))
        self.password = new_password
        print("Пароль успешно изменен.")

    def set_birth_date(self, new_birth_date):
        if new_birth_date < 1920 or new_birth_date > 2022:
            raise InvalidBirthDateException(new_birth_date)
        self.birth_date = new_birth_date
        print("Дата рождения успешно изменена.")


def main():
    try:
        user1 = User("user123", "password123", "John Doe", 1990)
        user1.change_password("12345")  # Вызовет исключение PasswordTooShortException
    except PasswordTooShortException as e:
        print(e)

    try:
        user2 = User("user456", "password456", "Jane Smith", 2023)
        user2.set_birth_date(1910)  # Вызовет исключение InvalidBirthDateException
    except InvalidBirthDateException as e:
        print(e)


if __name__ == '__main__':
    main()
