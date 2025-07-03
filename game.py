from shoe import Shoe

class Game:

    def __init__(self, start_credit: float):
        self.game_over : bool = False
        self.remaining_credit : float = start_credit

    def get_remaining_credit(self) -> float:

        return self.remaining_credit
    
    def set_remaining_credit(self, credit: float) -> None:

        self.remaining_credit = credit
        
    def is_game_over(self) -> bool:

        if(self.get_remaining_credit() <= 0):
            self.game_over = True
        else:
            continue_game : str = ""
            
            while(continue_game != "y" or continue_game != "n"):
                continue_game = input("Continue playing? (y/n): ")
                
                if(continue_game != "y" or continue_game != "n"):
                    print("Invalid response.")

            if(continue_game == "y"):
                self.game_over = False
            elif(continue_game == "n"):
                self.game_over = True
        
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