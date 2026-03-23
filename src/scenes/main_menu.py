import pygame as pg

from core.base_scene import BaseScene
from core.gui import Button
from settings import *

class MainMenu(BaseScene):
    def __init__(self, display, game_scene_manager):
        super().__init__(display, game_scene_manager)
        self.quit_button_image = pg.image.load("assets/images/quit_button.png").convert_alpha()
        self.quit_button_hover_image = pg.image.load("assets/images/quit_button_hover.png").convert_alpha()
        self.play_button_image = pg.image.load("assets/images/play_here_button.png").convert_alpha()
        self.play_button_hover_image = pg.image.load("assets/images/play_here_button_hover.png").convert_alpha()
        self.settings_button_image = pg.image.load("assets/images/settings_button.png").convert_alpha()
        self.settings_button_hover_image = pg.image.load("assets/images/settings_button_hover.png").convert_alpha()
        self.leaderboard_button_image = pg.image.load("assets/images/leaderboard_button.png").convert_alpha()
        self.leaderboard_button_hover_image = pg.image.load("assets/images/leaderboard_button_hover.png").convert_alpha()

        self.font = pg.font.Font("assets/fonts/sitka-small-599.ttf", 100)
        self.title = self.font.render("Main Menu", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.quit_button = Button(display, 
                                  0, 
                                  0, 
                                  self.quit_button_image, 
                                  self.quit_button_hover_image, 
                                  0.66)
        self.play_button = Button(display, 
                                  365, 
                                  199, 
                                  self.play_button_image, 
                                  self.play_button_hover_image, 
                                  0.66)
        self.settings_button = Button(display, 
                                  365, 
                                  350, 
                                  self.settings_button_image, 
                                  self.settings_button_hover_image, 
                                  0.66)
        self.leaderboard_button = Button(display, 
                                  365, 
                                  501, 
                                  self.leaderboard_button_image, 
                                  self.leaderboard_button_hover_image, 
                                  0.66)
    
    def run(self, events):
        self._handle_events(events)
        self._draw()
    
    def _draw(self):
        self.display.fill(BACKGROUND_COLOUR)
        self.display.blit(self.title, self.title_rect)
        self.quit_button.on_hover()
        self.quit_button.draw()
        self.play_button.on_hover()
        self.play_button.draw()
        self.settings_button.on_hover()
        self.settings_button.draw()
        self.leaderboard_button.on_hover()
        self.leaderboard_button.draw()
        pg.display.flip()

    def _handle_events(self, events):
        for event in events:
            if self.play_button.is_clicked(event):
                self.game_scene_manager.set_scene("level")
            if self.settings_button.is_clicked(event):
                self.game_scene_manager.set_scene("settings")
            if self.leaderboard_button.is_clicked(event):
                self.game_scene_manager.set_scene("leaderboard")
            if self.quit_button.is_clicked(event):
                self.game_scene_manager.exit_game = True