from cell import Cell
from visualiser_fetcher import VisualiserFetcher
from utils import clrscr

from time import sleep
from random import randint

class Simulation:
    
    EMPTY = None
    COUNT = 0
    FRAMERATE = 10

    VISUALISER = "pygame"
    
    def __init__(self, name: str, dimensions: tuple, object_class) -> None:
        self.name = name
        self.framerate = self.FRAMERATE
        self.object_class = object_class
        self._setup_environment(dimensions)
        self.beings = []
        self.locations = []
        
        self.visualizer = VisualiserFetcher.get_class(self.VISUALISER)(*dimensions, object_class)
    
    def _set_framerate(self, framerate: float) -> None:
        if type(framerate) is int:
            self.framerate = framerate
    
    def _setup_environment(self, dimensions: tuple) -> None:
        self.dimensions = dimensions
        w, h = dimensions
        self.environment = [[self.EMPTY for i in range(w)] for j in range(h)]
    
    def _is_available_position(self, position) -> bool:
        if 0 <= position[0] and position[0] < self.dimensions[0] and 0 <= position[1] and position[1] < self.dimensions[1]:
            return self.environment[position[1]][position[0]] is self.EMPTY
        else:
            return False
    
    def _get_available_position(self) -> None:
        position = None
        while True:
            position = (randint(0, self.dimensions[1]-1), randint(0, self.dimensions[0]-1))
            if self._is_available_position(position):
                break
        return position
    
    def get_surviving_beings(self):
        return self.beings, self.locations
    
    def _add_beings(self, count: int, beings: list = None) -> None:
        if beings is None:
            beings = [None] * count
        for being in beings:
            self._add_being(being)

    def _add_being(self, being: str = None) -> None:
        position = self._get_available_position()
        if type(being) is not self.object_class:
            being = self.object_class()
        self.beings.append(being)
        self.locations.append(position)
        self.environment[position[1]][position[0]] = being
        self.COUNT += 1
    
    def handle_events(self) -> None:
        for index, (being, location) in enumerate(zip(self.beings, self.locations)):
            direction = being.act()
            positions = [
                (location[0] + direction[0], location[1] + direction[1]),
                (location[0]               , location[1] + direction[1]),
                (location[0] + direction[0], location[1]),
            ]
            for position in positions:
                if self._is_available_position(position):
                    self.environment[position[1]][position[0]] = self.environment[location[1]][location[0]]
                    self.environment[location[1]][location[0]] = self.EMPTY
                    self.locations[index] = position
                    break
                else:
                    continue
    
    def show(self) -> None:
        self.visualizer.visualize(self.name, self.beings, self.locations, self.time_passed)
        
    def run(self, time: int, count: int, beings: list[str] = None) -> None:

        self._add_beings(count, beings)

        self.time_passed = 0

        self.show()
        # print(f"time {passed}")
        sleep(1/self.framerate)

        while self.time_passed < time:
            
            self.time_passed = round(self.time_passed+(1/self.framerate), 3)
            sleep(1/self.framerate)

            self.handle_events()
            self.show()