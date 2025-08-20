from ssgame.dispatcher.base import BaseDispathcer
from dataclasses import dataclass

from ssgame.infra.database.models.user import UserModel
from ssgame.controller.auth.login import LoginController
from ssgame.view.auth.login import LoginView


@dataclass
class AuthDispatcher(BaseDispathcer):
    def run(self) -> bool:
        controller = LoginController()
        view = LoginView()

        data = controller.get_data()

        result = UserModel().validate(
            username=data["username"], password=data["password"]
        )

        view.set_data(result)

        return result
