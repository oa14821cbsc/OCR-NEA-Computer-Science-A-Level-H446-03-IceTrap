import pygame as pg

class TextBox():
    COLOUR_ACTIVE = (43, 210, 43)
    COLOUR_PASSIVE = (255, 255, 255)
    COLOUR_ERROR = (255, 0, 0)
    colour = COLOUR_PASSIVE
    font_colour = (255, 255, 255)

    def __init__(self, display, x, y, w, h):
        self.display = display
        self.font = pg.font.Font("assets/fonts/ARIAL.TTF", 30)
        self.user_text = ""
        self.saved_text = []
        self.position_data = (x, y)
        self.text_box_rect = pg.Rect(x, y, w, h)
        self.active = False
        self.warning = ""

    def input(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.active = self.text_box_rect.collidepoint(event.pos)
                if self.active:
                    self.warning = ""

            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                    self.warning = ""
                elif event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
                    raw_text = self.user_text.strip()
                    if raw_text == "":
                        self.warning = "Empty inputs are not allowed!"
                        self.user_text = ""
                    elif len(raw_text) > 12:
                        self.warning = "Player name is too long!"
                        self.user_text = ""
                    else:
                        self.saved_text.append(raw_text)
                        print("Saved:", raw_text)
                        self.warning = ""
                else:
                    if event.unicode.isalpha():
                        self.user_text += event.unicode
                        self.warning = ""

    def draw(self):
        self.colour = self.COLOUR_ACTIVE if self.active else self.COLOUR_PASSIVE
        pg.draw.rect(self.display, 
                     (30, 30, 30), 
                     self.text_box_rect)
        pg.draw.rect(self.display, 
                     self.colour, 
                     self.text_box_rect, 
                     10)

        if self.user_text == "" and not self.warning:
            text_to_display = "Enter the name of the player character..."
            text_colour = (180, 180, 180)
        else:
            text_to_display = self.user_text if not self.warning else self.warning
            text_colour = self.COLOUR_ERROR if self.warning else self.font_colour

        self.text_surface = self.font.render(text_to_display,
                                             True,
                                             text_colour)
        self.display.blit(self.text_surface, 
                          (self.text_box_rect.x + 50, 
                          self.text_box_rect.y + 30))
