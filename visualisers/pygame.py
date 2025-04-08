import os
import pygame
from utils import get_rgb

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

class Pygame:

    BOX_CHARACTERS = {
        "top"   : ("╔", "══", "╗"),
        "middle": ("║", "  ", "║"),
        "bottom": ("╚", "══", "╝"),
    }
    
    def __init__(self, width: int, height: int, object) -> None:
        self.width = width
        self.height = height
        self.set_valid_object_class(object)
        self._setup_surface()
    
    def set_valid_object_class(self, object) -> None:
        self.valid_object_class = object
        
    def is_valid_object(self, object) -> bool:
        return self.valid_object_class is type(object)
    
    def _setup_surface(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((self.width*10, self.height*10))

    def _get_object_appearance(self, object) -> str:
        # dependant on chars not separate appearance
        return get_rgb(int(object.dna[:2]))
        
    def visualize(self, name: str, objects: list, locations: list, time: int) -> None:

        radius = 5
        offset = {
            "x" : radius,
            "y" : radius
        }

        self.surface.fill(BLACK)

        environment = [[None for j in range(self.width)] for i in range(self.height)]
        for object, location in zip(objects, locations):
            environment[location[1]][location[0]] = object
        
        for i, row in enumerate(environment):
            for j, point in enumerate(row):
                object = environment[i][j]
                if self.is_valid_object(object):
                    pygame.draw.circle(
                        self.surface,
                        self._get_object_appearance(object),
                        (
                            (j*radius*2)+(offset["x"]),
                            (i*radius*2)+(offset["y"])
                        ),
                        radius = 5
                    )

        font = pygame.font.SysFont("consolas", 20, bold=True)

        text = font.render(f"{name} : {time}", True, GRAY)
        self.surface.blit(text, (+1, +1))
        text = font.render(f"{name} : {time}", True, WHITE)
        self.surface.blit(text, (0, 0))

        pygame.display.update()