import logging
from ssgame.dispatcher.main import MainDispatcher


def main():
    dp = MainDispatcher()

    dp.run()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
