import pytest
from main import User, PasswordTooShortException, InvalidBirthDateException


def test_change_password_exception():
    user = User("user123", "password123", "John Doe", 1990)
    with pytest.raises(PasswordTooShortException,
                       match="Пароль слишком короткий. Минимальная длина пароля - 6 символов. Введено символов: 5"):
        user.change_password("12345")


def test_set_birth_date_exception():
    user = User("user456", "password456", "Jane Smith", 2023)
    with pytest.raises(InvalidBirthDateException,
                       match="Недопустимая дата рождения. Год рождения должен быть в пределах 1920-2022. Введено: 1910"):
        user.set_birth_date(1910)
