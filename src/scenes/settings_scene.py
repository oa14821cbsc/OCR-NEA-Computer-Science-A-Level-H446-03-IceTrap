import json
import pygame as pg
import os

from core.base_scene import BaseScene
from core.gui import *
from settings import *

class Settings(BaseScene):
    def __init__(self, display, game_scene_manager):
        super().__init__(display, game_scene_manager)

        default_settings = {
            "player_name": "Player",
            "keybinds": {"left": pg.K_a, 
                         "right": pg.K_d, 
                         "jump": pg.K_SPACE}
        }

        if not os.path.exists("settings.json"):
            with open("settings.json", "w") as f:
                json.dump(default_settings, f, indent=4)

        self.quit_button_image = pg.image.load("assets/images/quit_button.png").convert_alpha()
        self.quit_button_hover_image = pg.image.load("assets/images/quit_button_hover.png").convert_alpha()
        
        self.move_left_image = pg.image.load("assets/images/move_left.png").convert_alpha()
        self.left_width = self.move_left_image.get_width()
        self.left_height = self.move_left_image.get_height()
        self.scaled_move_left_image = pg.transform.scale(self.move_left_image,
                                                         (int(self.left_width * 0.66), (self.left_height * 0.66))
                                                         )
        self.move_right_image = pg.image.load("assets/images/move_right.png").convert_alpha()
        self.right_width = self.move_right_image.get_width()
        self.right_height = self.move_right_image.get_height()
        self.scaled_move_right_image = pg.transform.scale(self.move_right_image,
                                                         (int(self.left_width * 0.66), (self.left_height * 0.66))
                                                         )
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
        self.move_left_box = KeyBindBox(self.display, 634, 321, 398, 70, "left", keybinds)
        self.move_right_box = KeyBindBox(self.display, 634, 431, 398, 70, "right", keybinds)
        self.load_settings()
    
    def run(self, events):
        self._handle_events(events)
        self.name_text_box.input(events)
        self.move_left_box.input(events)
        self.move_right_box.input(events)
        self._draw()

    def save_settings(self):
        data = {
            "player_name": self.name_text_box.user_text,
            "keybinds": keybinds
        }
        with open("settings.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Debug: Settings Saved!")
    
    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                data = json.load(f)
                self.name_text_box.user_text = data.get("player_name", "")
                saved_keybinds = data.get("keybinds", {})
                for action, key in saved_keybinds.items():
                    if action in keybinds:
                        keybinds[action] = key
                        if action == "left":
                            self.move_left_box.keybinds[action] = key
                        elif action == "right":
                            self.move_right_box.keybinds[action] = key
        except (json.JSONDecodeError, FileNotFoundError):
            print("Settings file is invalid. Using defaults.")
    
    def _draw(self):
        self.display.fill(BACKGROUND_COLOUR)
        self.display.blit(self.title, self.title_rect)
        self.display.blit(self.scaled_move_left_image, (305, 321))
        self.display.blit(self.scaled_move_right_image, (305, 431))
        self.name_text_box.draw()
        self.move_left_box.draw()
        self.move_right_box.draw()
        self.quit_button.on_hover()
        self.quit_button.draw()
        pg.display.flip()

    def _handle_events(self, events):
        for event in events:
            if self.quit_button.is_clicked(event):
                self.save_settings()
                self.game_scene_manager.set_scene("main_menu")