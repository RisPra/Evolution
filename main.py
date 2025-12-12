from simulation import Simulation
from cell import Cell

def main():
    s = Simulation("Test", (150, 100), Cell)
    s._set_framerate(10)
    s.run(2, 25)
    
if __name__ == "__main__":
    main()