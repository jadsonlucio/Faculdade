import pygame
import threading


class DisplayCitys:
    def __init__(self, citys_pos, best_path, width, height):
        pygame.init()
        self.citys_pos = citys_pos
        self.best_path = best_path
        self.screen = pygame.display.set_mode((width, height))
        self.__running = False

    def run(self):
        self.__running = True
        while self.__running:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            self.__running = False
            
            self.screen.fill((255,255,255))
            self.draw_path()

            pygame.display.flip()

    def draw_path(self):
        for city_pos in self.citys_pos:
            pygame.draw.circle(self.screen, (0,0,0), city_pos, 5)
        
        start_pos = self.citys_pos[self.best_path[0]]

        for city_number in self.best_path[1:]:
            end_pos = self.citys_pos[city_number]
            pygame.draw.line(self.screen, (0,0,0), start_pos, end_pos)
            start_pos = end_pos


if __name__ == "__main__":
    screen = DisplayCitys([[25,100],[100, 25], [100, 100]], [2,0,1], 400, 400)
    screen.run()