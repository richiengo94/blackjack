from shoe import Shoe

class Hand:

    def __init__(self):
        self._hand: list[tuple] = []

    def deal_card(self, shoe: Shoe) -> None:
        """Deals a single card"""

        if shoe.get_n_remaining_cards():
            self._hand.append(shoe.remaining_cards.pop())

    def calculate_hand(self) -> tuple[int, bool, bool]:
        """Calculates value of given hand"""

        hand_sum: int = 0
        n_ace: int = 0

        for card_index in range(len(self._hand)):
            if(self._hand[card_index][1] == "J" or self._hand[card_index][1] == "Q" or self._hand[card_index][1] == "K"):
                hand_sum += 10
            elif(self._hand[card_index][1] == "A"):
                hand_sum += 1
                n_ace += 1
            else:
                hand_sum += int(self._hand[card_index][1])

        # Calculates for aces
        for i in range(n_ace):
            if(hand_sum + 10 <= 21):
                hand_sum += 10

        return hand_sum

    def clear_hand(self) -> None:
        """Clears hand after new round"""
        
        self._hand = []

    def get_suit(self, card_index: int) -> str:
        return self._hand[card_index][0]

    def get_rank(self, card_index: int) -> str:
        return self._hand[card_index][1]

    @property
    def hand(self) -> list:
        return self._hand

    def add_to_hand(self, card: tuple) -> None:
        self._hand.append(card)