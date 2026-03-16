import pygame as pg

class Button:
    def __init__(self, display, x, y, image, hover_image, scale):
        self.display = display
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pg.transform.scale(image, 
                                        (int(self.width * scale), int(self.height * scale))
                                        )
        self.hover_image = pg.transform.scale(hover_image, 
                                        (int(self.width * scale), int(self.height * scale))
                                        )
        self.base_image = self.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def set_position(self, x, y):
        self.rect.topleft = (x, y)
    
    def set_size(self, w, h):
        self.width = w
        self.height = h
    
    def is_clicked(self) -> bool:
        action = False
        mouse_pos = pg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):

            if pg.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

    def on_hover(self):
        mouse_pos = pg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.image = self.hover_image
        else:
            self.image = self.base_image

    def draw(self):
        self.display.blit(self.image, self.rect.topleft)