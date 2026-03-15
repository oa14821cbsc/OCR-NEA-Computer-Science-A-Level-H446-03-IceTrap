import pygame as pg
from typing import Dict

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

FPS = 60

BACKGROUND_COLOUR = (137, 207, 240)

class App:
    def __init__(self) -> None:
        pg.init()
        self.is_running: bool = True
        self.clock = pg.time.Clock()
        self.states: Dict[str, object]

    def run(self) -> None:
        self.time = pg.clock.tick(FPS)

app = App()