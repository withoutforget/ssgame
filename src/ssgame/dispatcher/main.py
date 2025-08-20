from ssgame.dispatcher.auth import AuthDispatcher


class MainDispatcher(AuthDispatcher):
    def run(self) -> None:
        auth_dispatcher = AuthDispatcher()

        auth_result = auth_dispatcher.run()

        if not auth_result:
            return
