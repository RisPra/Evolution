class Cell:
    
    #        ic ac  u  d  l  r
    # dna = "AA 99 92 45 18 02"
    
    def __init__(
        self,
        dna: str = None,
        icon: str = None
    ) -> None:
        self.dna = dna
        self.icon = icon

        # Intialise Actuators
        self.acuation_force = 0.0
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
    
    def decode_dna(self) -> None:

        # Actuation force range
        # 0 action : < 0.1
        # 1 action : > 0.1, < 0.9
        # 2 action : > 0.9

        ...

    def act(self) -> None:
        ...

    def __str__(self) -> str:
        return f'{self.icon} {self.dna}'