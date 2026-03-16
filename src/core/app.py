import pygame as pg
import sys

from settings import *
from scenes import *
from .scene_manager import GameSceneManager
from typing import Dict

class App:
    def __init__(self) -> None:
        pg.init()
        self.display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("IceTrap")
        self.is_running: bool = True
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0

        self.game_scene_manager = GameSceneManager("title_screen")

        self.title_screen = TitleScreen(self.display, self.game_scene_manager)

        self.states: Dict[str, object] = {"title_screen": self.title_screen}

    def run(self) -> None:
        while self.is_running and not self.game_scene_manager.exit_game:
            self._handle_events()
            self._update()
            self._run_state()
        pg.quit()
        sys.exit()

    def _update(self) -> None:
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001

    def _handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
                self.game_scene_manager.exit_game = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False
                    self.game_scene_manager.exit_game = True
    
    def _run_state(self) -> None:
        current_scene = self.states[self.game_scene_manager.get_scene()]
        current_scene.run()        
