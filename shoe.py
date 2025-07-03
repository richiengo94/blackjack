from random import shuffle

class Shoe:

    def __init__(self, n_decks: int) -> None:
        self.remaining_cards = []
        self.num_decks = n_decks
        self.create_shoe()
        self.max_shoe_size = self.get_remaining_cards()
    
    def create_shoe(self) -> None:
        """Creates a shoe of n number of decks and shuffles"""

        self.remaining_cards = []

        for curr_deck in range(self.num_decks):

            values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
            suits = ["heart", "diamond", "club", "spade"]

            for i in range(len(values)):
                for j in range(len(suits)):
                    self.remaining_cards.append((values[i], suits[j]))

        self.shuffle_shoe()
    
    def shuffle_shoe(self) -> None:
        """Shuffles the shoe"""
        shuffle(self.remaining_cards)

    def get_remaining_cards(self) -> int:
        """Returns number of remaining cards in shoe"""

        return len(self.remaining_cards)

    def check_shoe(self) -> None:

        deck_penetration = 0.7
        if(self.get_remaining_cards() <= round(self.max_shoe_size * (1 - deck_penetration))):
            self.create_shoe()