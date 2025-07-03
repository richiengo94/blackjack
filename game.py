from shoe import Shoe

class Game:

    def __init__(self):
        self.game_over : bool = False
        self.remaining_credit : float = 500

    def get_remaining_credit(self) -> float:

        return self.remaining_credit
    
    def set_remaining_credit(self, credit: float) -> None:

        self.remaining_credit = credit

game = Game()
shoe = Shoe(1)

player_hand = []
dealer_hand = []

def deal_hand(player_hand: list, dealer_hand: list, shoe: Shoe) -> None:
    """Deals starting hand in alternating order starting with player"""

    for i in range(2):
        deal_card(player_hand, shoe)
        deal_card(dealer_hand, shoe)

def deal_card(hand: list, shoe: Shoe) -> None:
    """Deals a single card"""

    hand.append(shoe.shoe.pop())

def calculate_hand(hand: list) -> tuple[int, bool]:
    """Calculates value of given hand"""

    hand_sum : int = 0
    n_ace : int = 0
    blackjack : bool = False

    for i in range(len(hand)):
        if(hand[i][0] == "J" or hand[i][0] == "Q" or hand[i][0] == "K"):
            hand_sum += 10
        elif(hand[i][0] == "A"):
            hand_sum += 1
            n_ace += 1
        else:
            hand_sum += int(hand[i][0])

    # Calculates for aces
    for i in range(n_ace):
        if(hand_sum + 10 <= 21):
            hand_sum += 10

    # Determines if hand is a blackjack
    if(hand_sum == 21 and len(hand) == 2):
        blackjack = True

    return hand_sum, blackjack

deal_hand(player_hand, dealer_hand, shoe)
print(player_hand)
print(dealer_hand)
#player_hand = [("A", "diamond"), ("A", "spade"), ("5", "heart"), ("8", "diamond"), ("8", "diamond")]
print(calculate_hand(player_hand))
print(calculate_hand(dealer_hand))
deal_card(player_hand, shoe)
print(player_hand)
print(calculate_hand(player_hand))

while(not game.game_over):
    if(game.get_remaining_credit() <= 0):
       game.game_over = True

    game.set_remaining_credit(game.get_remaining_credit() - 10)
    #print(game.get_remaining_credit())