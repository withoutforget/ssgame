from typing import Any, Protocol


class BaseDispathcer(Protocol):
    def run(self, *args, **kwargs) -> Any:
        pass
