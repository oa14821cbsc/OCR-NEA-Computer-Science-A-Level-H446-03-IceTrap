"""
This module is the entrypoint to the program!
"""
import pygame as pg


class App:
    """
    This class represents the game window.
    """

    def __init__(self) -> None:
        pg.init()
        pass

    def run() -> None:
        pass

    def update() -> None:
        pass

    def _handle_events() -> None:
        pass


def main() -> None:
    """
    Entrypoint of the program. This is where the app object is created and ran.
    """
    app = App()
    app.run()


if __name__ == "__main__":
    main()
