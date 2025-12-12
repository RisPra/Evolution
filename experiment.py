from simulation import Simulation
from cell import Cell
from typing import Any

class Experiment:

    FERTILITY_RATE = 2

    def __init__(self, dimensions: tuple, object_class) -> None:
        self.dimensions = dimensions
        self.object_class = object_class

    def set_filters(self, filters: list[tuple[int]]) -> None:
        self.filters = filters

    def select(self, beings, locations) -> Any:
        survivors = []

        filter = self.filters[self.generation-1]
        for index, (being, location) in enumerate(zip(beings, locations)):
            flag = True
            for mask in filter:
                if (
                    mask[0]*self.dimensions[0] <= location[0] and
                    location[0] <= mask[1]*self.dimensions[0] and
                    mask[2]*self.dimensions[1] <= location[1] and
                    location[1] <= mask[3]*self.dimensions[1]
                ):
                    flag = False
                    break
            if flag:
                survivors.append(being)
        next_generation = []
        for being in survivors:
            # TODO implement logic for decimal fertility rate i.e. 2.1
            for _ in range(self.FERTILITY_RATE):
                next_generation.append(being.reproduce())
        return next_generation

    def run(self, generations: int, time_per_generation: int, initial_count: int, framerate: int = None) -> None:
        self.generation = 0
        next_generation = None
        for self.generation in range(1, generations+1):

            if next_generation is not None:
                count = len(next_generation)

            s = Simulation(self.generation, self.dimensions, self.object_class)
            s._set_framerate(framerate)
            s.run(
                time = time_per_generation,
                count = initial_count,
                beings = next_generation,
            )

            next_generation = self.select(*(s.get_surviving_beings()))

def main():
    e = Experiment((50, 50), Cell)
    '''
    ##OOOOOO
    OOOOOOOO
    OOOOOOOO
    OOOOOO##
    
    ##OOOOOO
    ##OOOOOO
    ##OOOOOO
    ##OOOO##
    '''
    e.set_filters(
        [
            [(0, 0.9, 0.1, 1), (0.1, 1, 0, 0.9)]
        ]*25
        +[
            [(0.1, 0.9, 0, 1), (0.1, 1, 0, 0.9)]
        ]*25
    )
    e.run(50, 0.25, 500, 200)


main()