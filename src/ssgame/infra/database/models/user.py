from uuid import UUID, uuid4
from ssgame.infra.database.models.base import DatabaseModel
from dataclasses import dataclass
import hashlib

from ssgame.infra.database.dynamic_storage import user_data


@dataclass(slots=True)
class UserModelDTO:
    id: UUID
    username: str
    password_hash: str
    nickname: str


class UserModel(DatabaseModel):
    data: dict[UUID, UserModelDTO]

    def _add_test_user(self):
        test_password = "admin"

        password_hash = hashlib.sha256(test_password.encode()).hexdigest()

        test_user = UserModelDTO(
            id=uuid4(), username="admin", password_hash=password_hash, nickname="admin"
        )

        self.data[test_user.id] = test_user

    def __init__(self):
        self.data = user_data
        self._add_test_user()

    def _check_unique_user(self, username: str, nickname: str) -> bool:
        for _, v in self.data.items():
            if v.username == username or v.nickname == nickname:
                return False
        return True

    def add(self, user: UserModelDTO) -> None:
        if not self._check_unique_user(user.username, user.nickname):
            raise ValueError("Username or nickname has already taken")
        self.data[user.id] = user

    def validate(self, username: str, password: str) -> bool:
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        for _, v in self.data.items():
            if v.username == username and v.password_hash == password_hash:
                return True

        return False
