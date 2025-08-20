from typing import Any, Protocol


class BaseController(Protocol):
    def get_data(self, *args, **kwargs) -> Any:
        pass
