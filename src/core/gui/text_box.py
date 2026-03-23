import pygame as pg

class TextBox():
    COLOUR_ACTIVE = (43, 210, 43)
    COLOUR_PASSIVE = (255, 255, 255)
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

    def input(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.text_box_rect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False

            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                elif event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
                    if self.user_text.strip():
                        self.saved_text.append(self.user_text)
                        print("Debug: ", self.user_text)
                else:
                    if event.unicode.isalpha():
                        self.user_text += event.unicode

    def draw(self):
        self.colour = self.COLOUR_ACTIVE if self.active else self.COLOUR_PASSIVE
        pg.draw.rect(self.display, 
                     (30, 30, 30), 
                     self.text_box_rect)
        pg.draw.rect(self.display, 
                     self.colour, 
                     self.text_box_rect, 
                     10)

        if self.user_text == "":
            text_to_display = "Enter the name of the player character..."
            text_colour = (180, 180, 180)
        else:
            text_to_display = self.user_text
            text_colour = self.font_colour

        self.text_surface = self.font.render(text_to_display,
                                             True,
                                             text_colour)
        self.display.blit(self.text_surface, 
                          (self.text_box_rect.x + 50, 
                          self.text_box_rect.y + 30))
