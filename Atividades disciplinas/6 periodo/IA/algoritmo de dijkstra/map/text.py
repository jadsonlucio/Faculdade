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
            posY = posY - len(text.split("\n")) * self.size // 2
            posX = posX - max([len(t) for t in text.split("\n")]) * int(self.size * 0.7)

        for idx, line in enumerate(text.split("\n")):
            text_render = self.pygame_font.render(line, True, self.color)
            surface.blit(text_render, (posX, posY + idx * self.size + idx * self.margin))