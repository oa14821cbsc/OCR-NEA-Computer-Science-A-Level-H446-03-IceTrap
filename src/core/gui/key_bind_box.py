import pygame as pg

class KeyBindBox:
    COLOUR_ACTIVE = (43, 210, 43)
    COLOUR_PASSIVE = (255, 255, 255)
    COLOUR_ERROR = (255, 0, 0)

    def __init__(self, display, x, y, w, h, action, keybinds):
        self.display = display
        self.font = pg.font.Font("assets/fonts/ARIAL.TTF", 30)
        self.action = action
        self.keybinds = keybinds
        self.text_box_rect = pg.Rect(x, y, w, h)
        self.active = False
        self.warning = ""
    
    def input(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.active = self.text_box_rect.collidepoint(event.pos)
                if self.active:
                    self.warning = False

            if event.type == pg.KEYDOWN and self.active:
                new_key = event.key

                if new_key in self.keybinds.values() and new_key != self.keybinds[self.action]:
                    self.warning = "Duplicate Keys are not allowed!"
                else:
                    self.keybinds[self.action] = new_key
                    self.warning = ""
                    self.active = False

    def draw(self):
        colour = self.COLOUR_ACTIVE if self.active else self.COLOUR_PASSIVE

        pg.draw.rect(self.display, (30, 30, 30), self.text_box_rect)
        pg.draw.rect(self.display, colour, self.text_box_rect, 10)

        if self.warning:
            text = self.warning
            text_colour = self.COLOUR_ERROR
        elif self.active:
            text = "Press a key..."
            text_colour = (180, 180, 180)
        else:
            key = self.keybinds[self.action]
            text = pg.key.name(key)
            text_colour = colour

        text_surface = self.font.render(text, True, text_colour)
        self.display.blit(text_surface, (self.text_box_rect.x + 175, self.text_box_rect.y + 10))


