class LoginView:
    def set_data(self, successful: bool) -> None:
        if successful:
            print("Вы успешно вошли")
        else:
            print("Авторизация не удалась")
