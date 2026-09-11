import blackjack
import game
from shoe import Shoe
import pygame

def main():

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    pygame.init()

    display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display_surface.fill((0, 128, 0))  # Fill the screen with green color
    pygame.display.set_caption("Blackjack")

    game_font = pygame.font.Font('blackjack/assets/fonts/PixeloidMono.ttf', 32)

    text = game_font.render("Welcome to Blackjack!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    display_surface.blit(text, text_rect)

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
        pygame.display.update()

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

    pygame.quit()

if __name__ == "__main__":
    main()