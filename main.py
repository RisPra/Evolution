from simulation import Simulation
from cell import Cell

def main():
    s = Simulation((30, 20), Cell)
    s._set_framerate(10)
    s.add_beings(15)
    s.run(2)
    
if __name__ == "__main__":
    main()