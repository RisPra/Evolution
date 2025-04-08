import os

class Terminal:

    BOX_CHARACTERS = {
        "top"   : ("╔", "══", "╗"),
        "middle": ("║", "  ", "║"),
        "bottom": ("╚", "══", "╝"),
    }
    
    def __init__(self, width: int, height: int, object) -> None:
        self.width = width
        self.height = height
        self._set_valid_object_class(object)
    
    def _set_valid_object_class(self, object) -> None:
        self.valid_object_class = object
        
    def _is_valid_object(self, object) -> bool:
        return self.valid_object_class is type(object)
    
    def _get_object_appearance(self, object) -> str:
        return object.dna[:2]
        
    def visualize(self, objects: list, locations: list) -> None:
        # print(f"visualising on ({self.width}, {self.height})")
        # for object, location in zip(objects, locations):
        #     print(f"{str(object)} {location}")
        # return
        
        # top
        
        print(self.BOX_CHARACTERS["top"][0], end = "")
        print(self.BOX_CHARACTERS["top"][1]*(self.width) , end = "")
        print(self.BOX_CHARACTERS["top"][2], end = "")
        
        # middle
        
        environment = [[None for j in range(self.width)] for i in range(self.height)]
        for object, location in zip(objects, locations):
            environment[location[1]][location[0]] = object
        
        for i, row in enumerate(environment):
            print()
            print(self.BOX_CHARACTERS["middle"][0], end = "")
            for j, point in enumerate(row):
                object = environment[i][j]
                if self._is_valid_object(object):
                    print(self._get_object_appearance(object), end = "")
                else:
                    print(self.BOX_CHARACTERS["middle"][1], end = "")
            print(self.BOX_CHARACTERS["middle"][2], end = "")
            
        # bottom

        print()
        print(self.BOX_CHARACTERS["bottom"][0], end = "")
        print(self.BOX_CHARACTERS["bottom"][1]*(self.width), end = "")
        print(self.BOX_CHARACTERS["bottom"][2])