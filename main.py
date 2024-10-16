from cell import Cell
from simulation import Simulation

def main() -> None:
    sim = Simulation(
        dimensions=(20, 20)
    )

    # Add beings
    population = 5
    for _ in range(population):
        sim.birth(Cell(dna=str(_)*4, icon=chr(_+65)*2))

    sim.simulate()

if __name__ == "__main__":
    main()