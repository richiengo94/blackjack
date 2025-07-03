from shoe import Shoe
import game

def deal_hand(player_hand: game.Hand, dealer_hand: game.Hand, shoe: Shoe) -> None:
    """Deals starting hand in alternating order starting with player"""

    for i in range(2):
        player_hand.deal_card(shoe)
        dealer_hand.deal_card(shoe)

def player_turn(player_hand: game.Hand, dealer_hand: game.Hand, shoe: Shoe) -> list[int, bool, bool]:
    
    is_player_turn: bool = True

    print("---------- Player Turn ----------")

    while(is_player_turn):

        n_cards : int = len(player_hand.hand)
        options : list[str] = ["hit", "stand"]
        blackjack : bool = False
        bust : bool = False
        
        hand_sum = player_hand.calculate_hand()
        print(f"Player hand value: {hand_sum}")

        # Determines if hand is a blackjack
        if(hand_sum == 21 and len(player_hand.hand) == 2):
            blackjack = True
            is_player_turn = False

        if(blackjack):
            print("You have a blackjack!")
        else:
            if(n_cards == 2):
                options.append("double down")
            
            if(hand_sum < 21):
                print(options)
                player_input = input("Enter action: ")

                if((player_input == "hit" or player_input == "double down")):
                    player_hand.deal_card(shoe)
                    print("Player hand: ")
                    player_hand.display_hand(False)

                    if(player_input == "double down"):
                        is_player_turn = False

                elif(player_input == "stand"):
                    is_player_turn = False
                else:
                    print("Invalid action.")
            else:
                # Determines if hand is busted
                if(hand_sum > 21):
                    bust = True
                    print("You have busted!")
                elif(hand_sum == 21):
                    is_player_turn = False

        if(blackjack or bust):
            is_player_turn = False

    return [hand_sum, blackjack, bust]

def dealer_turn(dealer_hand: game.Hand, shoe: Shoe) -> list[int, bool, bool]:
    
    is_dealer_turn : bool = True

    print("---------- Dealer Turn ----------")

    while(is_dealer_turn):

        n_cards : int = len(dealer_hand.hand)
        blackjack : bool = False
        bust : bool = False

        dealer.display_hand(False)
        hand_sum = dealer_hand.calculate_hand()
        print(f"Dealer hand value: {hand_sum}")

        # Determines if hand is busted
        if(hand_sum > 21):
            bust = True
            print("Dealer has busted!")

        # Determines if hand is a blackjack
        if(hand_sum == 21 and len(dealer_hand.hand) == 2):
            blackjack = True

        if(blackjack):
            print("Dealer has a blackjack!")
        elif(not blackjack and not bust):
            if(hand_sum <= 16):
                dealer_hand.deal_card(shoe)
            else:
                is_dealer_turn = False

        if(blackjack or bust or hand_sum == 21):
            is_dealer_turn = False
            
    return [hand_sum, blackjack, bust]

def determine_winner(player_result: list, dealer_result: list, game: game.Game, bet: float):

    player_hand_sum = player_result[0]
    player_blackjack = player_result[1]
    player_bust = player_result[2]

    dealer_hand_sum = dealer_result[0]
    dealer_blackjack = dealer_result[1]
    dealer_bust = dealer_result[2]

    if(player_bust):
        print("Player loses.")
        game.set_remaining_credit(game.get_remaining_credit() - bet)
    elif(player_blackjack):
        print("Player wins!")
        game.set_remaining_credit(game.get_remaining_credit() + (bet * 1.5))
    else:
        if(dealer_blackjack):
            print("Player loses.")
            game.set_remaining_credit(game.get_remaining_credit() - bet)
        elif(dealer_bust or (player_hand_sum > dealer_hand_sum)):
            print("Player wins!")
            game.set_remaining_credit(game.get_remaining_credit() + bet)
        elif(player_hand_sum < dealer_hand_sum):
            print("Player loses.")
            game.set_remaining_credit(game.get_remaining_credit() - bet)
        else:
            print("Push.")
    
    print(f"Remaining credit: {game.get_remaining_credit()}")

#start_credit = float(input("Welcome. Enter starting credit: "))
start_credit = 100.0

new_game = game.Game(start_credit)
print(f"Remaining credit: {new_game.get_remaining_credit()}")

#n_decks = int(input("Enter number of decks: "))
n_decks = 1
new_shoe = Shoe(n_decks)
player = game.Hand()
dealer = game.Hand()

while(not new_game.game_over):
    #bet = float(input("Enter bet amount: "))
    bet = 10.0

    deal_hand(player, dealer, new_shoe)
    print("Player hand: ")
    player.display_hand(False)
    print("Dealer hand: ")
    dealer.display_hand(True)

    player_result = player_turn(player, new_shoe)
    dealer_result = dealer_turn(dealer, new_shoe)

    determine_winner(player_result, dealer_result, new_game, bet)
    player.clear_hand()
    dealer.clear_hand()
    new_shoe.check_shoe()

    if(new_game.get_remaining_credit() <= 0):
        new_game.game_over = True
        print("You are out of credits.")
    #new_game.is_game_over()