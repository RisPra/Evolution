import os
import time
import random
from cell import Cell

def clear() -> None:
    os.system("cls")

class Simulation:

    def __init__(self, dimensions: tuple[int, int] = None) -> None:

        self.beings = []
        self.icons = {
            "empty": "  ",
            "default": "AA",
            "caution": "!!",
            "vertical_border": "--",
            "horizontal_border": "|",
        }

        if dimensions is None:
            dimensions = (10, 10)
        self.dimensions = dimensions

        # self.map = [[None for _ in range(self.dimensions[0])] for _ in range(self.dimensions[1])]
        # dimensions

    def birth(self, parent: Cell = None, position: tuple[int, int] = None):
        
        # Create being
        if type(parent) is Cell:

            # DNA replication
            dna = parent.dna

            # Mutation
            print("trying to mutate")
            if random.randint(1, 100) < 50:
                mutated = random.randint(0, len(dna)-1)
                dna = dna[:mutated] + "#" + dna[mutated+1:]
                print(f'! Mutated: {dna}')

            being = Cell(dna=dna, icon=parent.icon)

        # Position being
        if position:
            self.map[position[0]][position[1]] = being
        else:
            occupied = [_[1] for _ in self.beings]
            while True:
                _x = random.randint(0, self.dimensions[0]-1)
                _y = random.randint(0, self.dimensions[1]-1)
                if (_x, _y) in occupied:
                    continue
                else:
                    position = (_x, _y)
                    break

        self.beings.append((being, position))
    
    def draw(self, draw_borders: bool = True) -> None:
        
        # Population details
        for being, positions in self.beings:
            print(f'  {being}')

        map = [[None for _ in range(self.dimensions[0])] for _ in range(self.dimensions[1])]

        for being, position in self.beings:
            map[position[0]][position[1]] = (being.icon if being.icon else self.icons["default"])

        print(self.icons["vertical_border"]*((self.dimensions[0]+1)*int(draw_borders)))

        for y, row in enumerate(map):
            
            print(self.icons["horizontal_border"]*int(draw_borders), end="")
            
            for x, cell in enumerate(row):
                print(cell if cell else self.icons["empty"], end="")

            print(self.icons["horizontal_border"]*int(draw_borders))

        print(self.icons["vertical_border"]*((self.dimensions[0]+1)*int(draw_borders)))

    def handle(self, Cell):
        pass

    def simulate(self, duration: int = None, framerate: int = None):
        
        if duration is None:
            duration = 10

        if framerate is None:
            framerate = 1

        for frame in range(duration):
            clear()
            
            # Events

            print(f'# Frame: {int(frame)+1}')
            self.draw()
            time.sleep(framerate)
    
        print("END")
