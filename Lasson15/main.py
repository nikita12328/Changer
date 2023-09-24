import logging
import argparse

# Настроим логирование
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] - %(message)s')

class PasswordTooShortException(Exception):
    def __init__(self, password_length):
        super().__init__(
            f"Пароль слишком короткий. Минимальная длина пароля - 6 символов. Введено символов: {password_length}")
        logging.error("PasswordTooShortException: " + self.args[0])

class InvalidBirthDateException(Exception):
    def __init__(self, birth_year):
        super().__init__(
            f"Недопустимая дата рождения. Год рождения должен быть в пределах 1920-2022. Введено: {birth_year}")
        logging.error("InvalidBirthDateException: " + self.args[0])

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
        logging.info(f"Пользователь {self.login} изменил пароль.")

    def set_birth_date(self, new_birth_date):
        if new_birth_date < 1920 or new_birth_date > 2022:
            raise InvalidBirthDateException(new_birth_date)
        self.birth_date = new_birth_date
        print("Дата рождения успешно изменена.")
        logging.info(f"Пользователь {self.login} изменил дату рождения на {new_birth_date}.")

def main():
    """
    можно запускать программу с аргументами из командной строки,
    указав --login, --password и/или --birth_date,
    чтобы изменить пароль или дату рождения пользователя
    python your_script.py --login user123 --password new_password
    python your_script.py --login user123 --birth_date 1995
    """
    parser = argparse.ArgumentParser(description='Управление пользователями.')
    parser.add_argument('--login', required=True, help='Логин пользователя')
    parser.add_argument('--password', help='Новый пароль пользователя')
    parser.add_argument('--birth_date', type=int, help='Новая дата рождения пользователя')

    args = parser.parse_args()

    try:
        user = User(args.login, "password123", "John Doe", 1990)
        if args.password:
            user.change_password(args.password)
        if args.birth_date:
            user.set_birth_date(args.birth_date)
    except PasswordTooShortException as e:
        print(e)
    except InvalidBirthDateException as e:
        print(e)

if __name__ == '__main__':
    main()
