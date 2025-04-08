import os
import pygame

class Terminal:

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
        return object.dna[:2]
        
    def visualize(self, objects: list, locations: list) -> None:

        being = objects[0]
        pygame.circle()
        self.surface.draw.re
        self.surface.blit()

        environment = [[None for j in range(self.width)] for i in range(self.height)]
        for object, location in zip(objects, locations):
            environment[location[1]][location[0]] = object
        
        # for i, row in enumerate(environment):
        #     print()
        #     print(self.BOX_CHARACTERS["middle"][0], end = "")
        #     for j, point in enumerate(row):
        #         object = environment[i][j]
        #         if self.is_valid_object(object):
        #             print(self._get_object_appearance(object), end = "")
        #         else:
        #             print(self.BOX_CHARACTERS["middle"][1], end = "")
        #     print(self.BOX_CHARACTERS["middle"][2], end = "")