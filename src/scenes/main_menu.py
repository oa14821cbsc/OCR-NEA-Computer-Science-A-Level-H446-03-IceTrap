import pygame as pg

from core.base_scene import BaseScene
from settings import *

class MainMenu(BaseScene):
    def __init__(self, display, game_scene_manager):
        super().__init__(display, game_scene_manager)
        self.font_placeholder = pg.font.Font("assets/fonts/sitka-small-599.ttf", 50)
        self.placeholder = self.font_placeholder.render("PLACEHOLDER MAIN MENU", 
                                                        False, 
                                                        (255, 255, 255))
        self.placeholder_rect = self.placeholder.get_rect(
            center=(SCREEN_WIDTH // 2, 360)
            )
    
    def run(self):
        self._handle_events()
        self._draw()
    
    def _draw(self):
        self.display.fill(BACKGROUND_COLOUR)
        self.display.blit(self.placeholder, self.placeholder_rect)
        pg.display.flip()

    def _handle_events(self):
        pass