import pygame

from constants import *


class Text(pygame.font.Font):
    def __init__(self, text, color, font_size, x, y):
        super().__init__(FONT, font_size)
        self.text = text
        self.color = color
        self.x = x
        self.y = y

    def draw(self, screen):
        img = self.render(self.text, True, self.color)
        screen.blit(img, (self.x, self.y))


# class Panel (Text):
#    def __init__(self, text, color, position):
#        self.text = text
#        self.color = color
#        self.position = position
#        super().__init__()
