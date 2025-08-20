from ssgame.controller.base import BaseController


class LoginController(BaseController):
    def get_data(self) -> dict[str, str]:
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")

        return {
            "username": username,
            "password": password,
        }
