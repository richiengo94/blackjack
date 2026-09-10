from shoe import Shoe

class Game:

    def __init__(self, start_credit: float, quit_game: bool = False) -> None:
        self.game_over : bool = False
        self.remaining_credit : float = start_credit
        self.quit_game : bool = quit_game

    def get_remaining_credit(self) -> float:
        return self.remaining_credit
    
    def set_remaining_credit(self, credit: float) -> None:
        self.remaining_credit = credit

    def get_quit_game(self) -> bool:
        return self.quit_game

    def set_quit_game(self, quit_game: bool) -> None:
        self.quit_game = quit_game
        
    def is_game_over(self) -> bool:
        """Checks if game is over based on remaining credit and quit_game flag"""

        if(self.get_remaining_credit() <= 0):
            print("You are out of credits.")
            self.set_remaining_credit(0)

        if(self.get_remaining_credit() <= 0 or self.get_quit_game()):
            self.game_over = True
            print("Game over.")
        
        return self.game_over


class Hand:

    def __init__(self):
        self.hand : list = []

    def deal_card(self, shoe: Shoe) -> None:
        """Deals a single card"""

        self.hand.append(shoe.remaining_cards.pop())

    def calculate_hand(self) -> int:
        """Calculates value of given hand"""

        hand_sum : int = 0
        n_ace : int = 0

        for card_index in range(len(self.hand)):
            if(self.hand[card_index][0] == "J" or self.hand[card_index][0] == "Q" or self.hand[card_index][0] == "K"):
                hand_sum += 10
            elif(self.hand[card_index][0] == "A"):
                hand_sum += 1
                n_ace += 1
            else:
                hand_sum += int(self.hand[card_index][0])

        # Calculates for aces
        for i in range(n_ace):
            if(hand_sum + 10 <= 21):
                hand_sum += 10

        return hand_sum
    
    def display_hand(self, is_dealer_start: bool) -> None:
        """Displays hand in terminal"""

        # Hides the dealer's second card on initial deal
        if(is_dealer_start):
            print([self.hand[0], ("*", "********")])
        else:
            print(self.hand)

    def clear_hand(self) -> None:
        """Clears hand after new round"""
        
        self.hand = []