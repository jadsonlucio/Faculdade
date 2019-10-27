import pygame

pygame.font.init()

class PyGameText:
    def __init__(self, font, size, color, margin):
        self.font = font 
        self.size = size
        self.color = color
        self.margin = margin

        self.pygame_font = pygame.font.Font(font, size) 

    
    def render(self, surface, text, posX, posY, center = True):
        if center:
            posY = posY - (len(text.split("\n")) - 1) * self.size // 2

        for idx, line in enumerate(text.split("\n")):
            text_render = self.pygame_font.render(line, True, self.color)
            posX = posX - text_render.get_width() - 15
            surface.blit(text_render, (posX, posY + idx * self.size + idx * self.margin))