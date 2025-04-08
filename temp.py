
import random

def get_num() -> int:
    return random.randint(0, 1)

print([get_num() for i in range(2)]*2)