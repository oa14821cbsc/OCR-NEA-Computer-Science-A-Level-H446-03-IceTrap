import pygame as pg

from core.base_scene import BaseScene
from core.gui import Button
from settings import *

class TitleScreen(BaseScene):
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
        self.font_title = pg.font.Font("assets/fonts/sitka-small-599.ttf", 150)
        self.font_text_prompt = pg.font.Font("assets/fonts/sitka-small-599.ttf", 30)
        self.title = self.font_title.render("IceTrap", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.text_prompt = self.font_text_prompt.render("Click anywhere on the screen with your left mouse button to continue.",
                                            True,
                                            (255, 255, 255))
        self.text_prompt_rect = self.text_prompt.get_rect(center=(SCREEN_WIDTH // 2, 500))

    def run(self):
        self._handle_events()
        self._draw()

    def _draw(self):
        self.display.fill(BACKGROUND_COLOUR)
        self.display.blit(self.title, self.title_rect)
        self.display.blit(self.text_prompt, self.text_prompt_rect)
        self.quit_button.on_hover()
        self.quit_button.draw()
        pg.display.flip()

    def _handle_events(self):
        if pg.mouse.get_pressed()[0] == 1:
            self.game_scene_manager.set_scene("main_menu")

        if self.quit_button.is_clicked():
            self.game_scene_manager.exit_game = True