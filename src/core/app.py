import pygame as pg
import sys

from settings import *
from scenes import *
from .scene_manager import GameSceneManager
from typing import Dict

class App:
    def __init__(self) -> None:
        pg.init()
        pg.key.set_repeat(400, 40)
        self.display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("IceTrap")
        self.is_running: bool = True
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        self.events = None

        self.game_scene_manager = GameSceneManager("title_screen")

        self.title_screen = TitleScreen(self.display, self.game_scene_manager)
        self.main_menu = MainMenu(self.display, self.game_scene_manager)
        self.settings = Settings(self.display, self.game_scene_manager)
        self.leaderboard = Leaderboard(self.display, self.game_scene_manager)
        self.level = Level(self.display, self.game_scene_manager)
        

        self.states: Dict[str, object] = {"title_screen": self.title_screen, 
                                          "main_menu": self.main_menu,
                                          "settings": self.settings,
                                          "leaderboard": self.leaderboard, 
                                          "level": self.level}

    def run(self) -> None:
        while self.is_running and not self.game_scene_manager.exit_game:
            self._handle_events()
            self._update()
        pg.quit()
        sys.exit()

    def _update(self) -> None:
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001

    def _handle_events(self) -> None:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.is_running = False
                self.game_scene_manager.exit_game = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False
                    self.game_scene_manager.exit_game = True
        self.events = events

        current_scene = self.states[self.game_scene_manager.get_scene()]
        current_scene.run(self.events)        
