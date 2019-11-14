import pygame 
import numpy as np

class PygameClassifierPlot:
    def __init__(self, model_classifier):
        pygame.init()
        self.running = False
        self.model_classifier = model_classifier

        self.x_range = (-10, 10)
        self.y_range = (-10, 10)

        self.line_space = 0.1
        self.line_size = 0.05

        self.width = 400
        self.height = 400
        self._display = pygame.display.set_mode((self.width, self.height))
        self.cartesian_surface = pygame.Surface((self.width, self.height))
        self.prediction_surface = pygame.Surface((self.width, self.height))

    def on_screen(self):
        pass
    
    def on_event(self, event):
        pass

    def set_cartesian_surface(self):
        line_x_pos = ((0, int(self.height/2)), (self.width, int(self.height/2)))
        line_y_pos = ((int(self.width/2), 0), (int(self.width/2), self.height))

        x_grid_size = abs(self.x_range[1] - self.x_range[0])
        y_grid_size = abs(self.y_range[1] - self.y_range[0])

        x_units_pixel_size = int(self.width / x_grid_size)
        y_units_pixel_size = int(self.height / y_grid_size)


        for i in range(x_grid_size):
            pygame.draw.line(self.cartesian_surface, (122, 50, 122), (i * x_units_pixel_size, 0), 
                                                            (i * x_units_pixel_size, self.height))

        
        for j in range(y_grid_size):
            pygame.draw.line(self.cartesian_surface, (122, 50, 122), (0, j * y_units_pixel_size), 
                                                            (self.width, j * y_units_pixel_size))

        pygame.draw.line(self.cartesian_surface, (255, 255, 255), line_x_pos[0], line_x_pos[1])
        pygame.draw.line(self.cartesian_surface, (255, 255, 255), line_y_pos[0], line_y_pos[1])

    def pixel_point_to_cartesian(self, pixel_point):
        x, y = pixel_point     
        x_grid_size = abs(self.x_range[1] - self.x_range[0])
        y_grid_size = abs(self.y_range[1] - self.y_range[0])

        x_units_pixel_size = int(self.width / x_grid_size)
        y_units_pixel_size = int(self.height / y_grid_size)

        x_real_pixel = x - self.width / 2
        y_real_pixel = y - self.height / 2

        x = x_real_pixel / x_units_pixel_size
        y = y_real_pixel / y_units_pixel_size

        return x,y

    
    def cartesian_to_pixel_point(self, cartesian_point):
        x_half_screen_size = self.width / 2
        y_half_screen_size = self.height / 2

        x, y = cartesian_point     
        x_grid_size = abs(self.x_range[1] - self.x_range[0])
        y_grid_size = abs(self.y_range[1] - self.y_range[0])

        x_units_pixel_size = int(self.width / x_grid_size)
        y_units_pixel_size = int(self.height / y_grid_size)

        return x_half_screen_size + x * x_units_pixel_size, y_half_screen_size + y * y_units_pixel_size


    def update_screen_predictions(self):
        surface = pygame.Surface((self.width, self.height))
        pixels = []
        for i in range(self.width):
            row = []
            for j in range(self.height):
                x, y = self.pixel_point_to_cartesian((i, j))
                result = self.model_classifier.output([x, y])

                if result:
                    row.append((0, 0, 255))
                else:
                    row.append((255, 0, 0))
            
            pixels.append(row)
        


        pygame.pixelcopy.array_to_surface(surface, np.array(pixels))
        surface.set_alpha(40)

        self.prediction_surface = surface

    def add_prediction_points(self, X, y):
        for inputs, output in zip(X, y):
            if output:
                color = (0, 0, 255)
            else:
                color = (255, 0, 0)

            inputs = self.cartesian_to_pixel_point(inputs)
            
            pygame.draw.rect(self.cartesian_surface, color, pygame.Rect(inputs, (10, 10)))


    def run(self):
        self.set_cartesian_surface()
        self.running = True

        while self.running:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    else:
                        self.on_event(event)

            self._display.blit(self.cartesian_surface, (0,0))
            self._display.blit(self.prediction_surface, (0, 0))
            self.on_screen()

            pygame.display.flip()