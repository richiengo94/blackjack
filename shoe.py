from random import shuffle

class Shoe:

    def __init__(self, n_decks: int) -> None:
        self.shoe = []
        self.create_shoe(n_decks)
    
    def create_shoe(self, n_decks: int) -> None:
        """Creates a shoe of n number of decks and shuffles"""

        for curr_deck in range(n_decks):

            values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
            suits = ["heart", "diamond", "club", "spade"]

            for i in range(len(values)):
                for j in range(len(suits)):
                    self.shoe.append((values[i], suits[j]))

        self.shuffle_shoe()
    
    def shuffle_shoe(self) -> None:
        """Shuffles the shoe"""
        shuffle(self.shoe)