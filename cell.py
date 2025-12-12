from random import (randint)
from utils import (get_rgb)

class Cell:
    ...

class Cell:
    
    # color should not be an individual expression, it should be made out of dna representation
    # 00 00 00000000
    ATTRIBUTES = ["colour", "will", "up", "down", "left", "right"]
    MUTATION_PERCENT = 5
    MOVEMENT_WILL_BOUNDARIES = [5, 90, 100]
    GENE_LENGTH = 2
        
    def __init__(self, dna: str = None) -> None:
        if dna is None:
            dna = self._get_random_dna()
        self.dna = dna
        self.attributes = {attribute: None for attribute in self.ATTRIBUTES}
        self._decode_dna()
    
    def __str__(self) -> str:
        string = f"# Cell: {self.dna[:2]} {self.dna[2:]}"
        # for key, value in self.attributes.items():
        #     string += f"\n\t{key:6} : {value}"
        return string
    
    @classmethod
    def _get_random_dna(cls) -> str:
        dna_length = len(cls.ATTRIBUTES)*cls.GENE_LENGTH
        dna = f"{randint(0, int('9'*dna_length)):0>{dna_length}}"
        return dna
    
    def _get_dna(self, can_mutate: bool = None) -> str:
        if can_mutate is None:
            can_mutate = True
        dna = self.dna
        if can_mutate is True:
            if randint(0, 99) < self.MUTATION_PERCENT:
                index = randint(0, len(dna))
                changed = str(randint(0, 9))
                dna = self.dna[:index] + changed + self.dna[index+1:]
        return dna
    
    def _decode_dna(self) -> None:
        separators = [i for i in range(0, len(self.dna)+1, 2)]
        decoded = [self.dna[separators[i-1]:separators[i]] for i in range(1, len(separators))]
        for index, (key, value) in enumerate(self.attributes.items()):
            self.attributes[key] = int(decoded[index])
            
        # turn 2 digit color into rgb value
        self.attributes["colour"] = get_rgb(self.attributes["colour"])
        
    def reproduce(self) -> Cell:
        return Cell(self._get_dna(True))
    
    def act(self) -> tuple:
        
        # How many directions at one time?
        moves = 0
        will = self.attributes["will"]
        for index, boundary in enumerate(self.MOVEMENT_WILL_BOUNDARIES):
            if will < boundary:
                moves = index
                break
        
        # Which direction
        move = 0
        directions = ["up", "down", "left", "right"][::-1]
        vectors = {direction: self.attributes[direction] for direction in directions}
        
        for _ in range(moves):
            invd = {v: k for k, v in vectors.items()}
            direction = invd[max(vectors.values())]
            move += 1 * 10**directions.index(direction)
            vectors.pop(direction, None)
        
        temp = list(map(int, list(f"{move:0>4}")))
        
        reduced = (temp[0]-temp[1], temp[2]-temp[3])[::-1]
        
        return reduced