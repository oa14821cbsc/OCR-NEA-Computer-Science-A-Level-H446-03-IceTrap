"""
This module is the entrypoint to the program!
"""
import pygame as pg
from src.config.config_file import SCREEN_WIDTH, SCREEN_HEIGHT

class App:
    """
    This class represents the game window.
    """

    def __init__(self) -> None:
        pg.init()
        pg.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)

    def run(self) -> None:
        pass

    def update(self) -> None:
        pass

    def _handle_events(self) -> None:
        pass


def main() -> None:
    """
    Entrypoint of the program. This is where the app object is created and ran.
    """
    app = App()
    app.run()


if __name__ == "__main__":
    main()
