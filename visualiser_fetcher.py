from visualisers.terminal import Terminal
from visualisers.pygame import Pygame


class VisualiserFetcher:

    @staticmethod
    def get_class(visualiser: str) -> type:
        if visualiser == "terminal":
            return Terminal
        elif visualiser == "pygame":
            return Pygame
        else:
            raise ValueError(f"Visualiser '{visualiser}' not found.")