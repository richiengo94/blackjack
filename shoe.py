from random import shuffle

class Shoe:

    def __init__(self, n_decks: int) -> None:
        self._remaining_cards: list[tuple] = []
        self._num_decks: int = n_decks
        self.create_shoe()
        self._max_shoe_size: int = self.get_n_remaining_cards()

    @property
    def remaining_cards(self) -> list:
        return self._remaining_cards
    
    def create_shoe(self) -> None:
        """Creates a shoe of n number of decks and shuffles"""

        self._remaining_cards = []

        for curr_deck in range(self._num_decks):

            ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
            suits = ["heart", "diamond", "club", "spade"]

            for i in range(len(suits)):
                for j in range(len(ranks)):
                    self._remaining_cards.append((suits[i], ranks[j]))

        self.shuffle_shoe()
    
    def shuffle_shoe(self) -> None:
        """Shuffles the shoe"""
        
        shuffle(self._remaining_cards)

    def get_n_remaining_cards(self) -> int:
        """Returns number of remaining cards in shoe"""

        return len(self._remaining_cards)

    def check_shoe(self) -> None:
        """Checks if the shoe needs to be recreated when the deck penetration threshold has been reached"""

        deck_penetration = 0.7
        if(self.get_n_remaining_cards() <= round(self._max_shoe_size * (1 - deck_penetration))):
            self.create_shoe()