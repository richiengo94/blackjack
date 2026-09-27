from shoe import Shoe
import game

def player_turn(player_hand: game.Hand, shoe: Shoe) -> list[int, bool, bool, bool]:
    """Player's turn to play hand"""
    
    is_player_turn: bool = True

    print("---------- Player Turn ----------")

    while(is_player_turn):

        n_cards : int = len(player_hand.hand)
        options : list[str] = ["hit", "stand"]
        blackjack : bool = False
        bust : bool = False
        double_down : bool = False
        quit_game : bool = False

        hand_sum = player_hand.calculate_hand()
        print(f"Player hand value: {hand_sum}")

        # Determines if hand is a blackjack
        if(hand_sum == 21 and len(player_hand.hand) == 2):
            blackjack = True
            is_player_turn = False

        if(blackjack):
            print("You have a blackjack!\n")
        else:
            if(n_cards == 2):
                options.append("double down")

            options.append("quit")
            
            if(hand_sum < 21):
                print(options)
                player_input = input("Enter action: ")

                if((player_input == "hit" or player_input == "double down")):
                    player_hand.deal_card(shoe)
                    print("Player hand: ")
                    player_hand.display_hand(False)

                    if(player_input == "double down"):
                        is_player_turn = False
                        double_down = True

                elif(player_input == "stand"):
                    is_player_turn = False
                elif(player_input == "quit"):
                    is_player_turn = False
                    quit_game = True
                else:
                    print("Invalid action.\n")
            else:
                # Determines if hand is busted
                if(hand_sum > 21):
                    bust = True
                    print("You have busted!")
                elif(hand_sum == 21):
                    is_player_turn = False

        if(blackjack or bust):
            is_player_turn = False

    return [hand_sum, blackjack, bust, double_down, quit_game]

def dealer_turn(dealer_hand: game.Hand, shoe: Shoe) -> list[int, bool, bool]:
    """Dealer's turn to play hand"""
    
    is_dealer_turn : bool = True

    print("---------- Dealer Turn ----------")

    while(is_dealer_turn):

        n_cards : int = len(dealer_hand.hand)
        blackjack : bool = False
        bust : bool = False

        dealer_hand.display_hand(False)
        hand_sum = dealer_hand.calculate_hand()
        print(f"Dealer hand value: {hand_sum}")

        # Determines if hand is busted
        if(hand_sum > 21):
            bust = True
            print("Dealer has busted!\n")

        # Determines if hand is a blackjack
        if(hand_sum == 21 and len(dealer_hand.hand) == 2):
            blackjack = True

        if(blackjack):
            print("Dealer has a blackjack!\n")
        elif(not blackjack and not bust):
            if(hand_sum <= 16):
                dealer_hand.deal_card(shoe)
            else:
                is_dealer_turn = False

        if(blackjack or bust or hand_sum == 21):
            is_dealer_turn = False
            
    return [hand_sum, blackjack, bust]