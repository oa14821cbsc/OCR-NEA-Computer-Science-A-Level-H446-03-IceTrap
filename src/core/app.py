import pygame as pg

from settings import *
from typing import Dict

class App:
    def __init__(self) -> None:
        pg.init()
        self.display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.is_running: bool = True
        self.clock = pg.time.Clock()
        self.states: Dict[str, object] = {}

    def run(self) -> None:
        while self.is_running:
            self._handle_events()
            self._update()
            self._render()

    def _update(self) -> None:
        self.delta_time = self.clock.tick(FPS)
        self.time = pg.time.get_ticks() * 0.001
    
    def _render(self) -> None:
        self.display.fill(BACKGROUND_COLOUR)
        pg.display.flip()

    def _handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False