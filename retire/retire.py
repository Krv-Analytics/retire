# retire/retire.py

from retire.data import load_dataset


class Retire:

    def __init__(self):
        self.raw_df = load_dataset()
