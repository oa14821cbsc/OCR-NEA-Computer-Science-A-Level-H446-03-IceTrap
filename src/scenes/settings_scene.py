import pygame as pg

from core.base_scene import BaseScene
from core.gui import *
from settings import *

class Settings(BaseScene):
    def __init__(self, display, game_scene_manager):
        super().__init__(display, game_scene_manager)
        self.quit_button_image = pg.image.load("assets/images/quit_button.png").convert_alpha()
        self.quit_button_hover_image = pg.image.load("assets/images/quit_button_hover.png").convert_alpha()
        self.quit_button = Button(display, 
                                  0, 
                                  0, 
                                  self.quit_button_image, 
                                  self.quit_button_hover_image, 
                                  0.66)
        self.font = pg.font.Font("assets/fonts/sitka-small-599.ttf", 100)
        self.title = self.font.render("Settings", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.name_text_box = TextBox(self.display, 300, 167, 700, 100)
    
    def run(self, events):
        self._handle_events(events)
        self.name_text_box.input(events)
        self._draw()
    
    def _draw(self):
        self.display.fill(BACKGROUND_COLOUR)
        self.display.blit(self.title, self.title_rect)
        self.name_text_box.draw()
        self.quit_button.on_hover()
        self.quit_button.draw()
        pg.display.flip()

    def _handle_events(self, events):
        for event in events:
            if self.quit_button.is_clicked(event):
                self.game_scene_manager.set_scene("main_menu")