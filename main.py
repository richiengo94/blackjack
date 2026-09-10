import blackjack
import game
from shoe import Shoe

def main():
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

        blackjack.deal_hand(player, dealer, new_shoe)
        print("Player hand: ")
        player.display_hand(False)
        print("Dealer hand: ")
        dealer.display_hand(True)

        player_result = blackjack.player_turn(player, new_shoe)
        blackjack.check_quit_game(player_result, new_game)
        
        if(not new_game.is_game_over()):
            dealer_result = blackjack.dealer_turn(dealer, new_shoe)
            blackjack.determine_winner(player_result, dealer_result, new_game, bet)
            player.clear_hand()
            dealer.clear_hand()
            new_shoe.check_shoe()

if __name__ == "__main__":
    main()