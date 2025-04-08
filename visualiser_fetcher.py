from visualisers.terminal import Terminal


class VisualiserFetcher:

    @staticmethod
    def get_class(visualiser: str) -> type:
        if visualiser == "terminal":
            return Terminal
        elif visualiser == "pygame":
            return Terminal
        else:
            raise ValueError(f"Visualiser '{visualiser}' not found.")