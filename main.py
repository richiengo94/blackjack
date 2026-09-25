import pygame
import enum
import button
import game
import shoe
import blackjack

class MouseButton(enum.Enum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

def main():

    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600

    BG_COLOR: tuple = (0, 128, 0) # Mid-dark green

    GAME_DIRECTORY: str = "blackjack/assets"
    GRAPHICS_DIRECTORY: str = GAME_DIRECTORY + "/graphics"

    game_state: str = "welcome"

    pygame.font.init()
    pygame.display.init()

    display_surf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display_surf.fill('Black')
    pygame.display.set_caption("Blackjack")
    blackjack_icon = pygame.image.load(f"{GRAPHICS_DIRECTORY}/Red.png")
    pygame.display.set_icon(blackjack_icon)
    clock = pygame.time.Clock()
    FPS = clock.tick(60)
    game_font = pygame.font.Font(f"{GAME_DIRECTORY}/fonts/PixeloidMono.ttf", 32)

    card_spritesheet = pygame.image.load(f"{GRAPHICS_DIRECTORY}/playing_cards_spritesheet.png")

    new_game = game.Game(100)
    new_shoe = shoe.Shoe(1)
    player_hands: list = [game.Hand()]
    dealer_hand = game.Hand()

    blackjack.deal_hand(player_hands[0], dealer_hand, new_shoe)

    running: bool = True
    button_clicked: bool = False
    player_turn: bool = True
    player_busted: bool = False

    player_hand_sum: int = 0
    hand_index: int = 0

    curr_hand: game.Hand = player_hands[0]
    next_hand = None

    while(running):

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == "welcome":
                display_welcome_screen(display_surf, game_font, SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR)

                welcome_buttons_x: int = (SCREEN_WIDTH - 250) // 2
                welcome_buttons_y: int = (SCREEN_HEIGHT // 2) + 50
                welcome_buttons_width: int = 250
                welcome_buttons_height: int = 50

                start_button_x: int = welcome_buttons_x
                start_button_y: int = welcome_buttons_y
                start_button: button.Button = button.Button(start_button_x, start_button_y, welcome_buttons_width, welcome_buttons_height)
                start_button.set_button_text("Start Game", game_font)
                start_button_rect: pygame.Rect = start_button.draw(display_surf)

                quit_button_x: int = welcome_buttons_x
                quit_button_y: int = welcome_buttons_y + 70
                quit_button: button.Button = button.Button(quit_button_x, quit_button_y, welcome_buttons_width, welcome_buttons_height)
                quit_button.set_button_text("Quit", game_font)
                quit_button_rect: pygame.Rect = quit_button.draw(display_surf)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == MouseButton.LEFT.value:
                        if start_button_rect.collidepoint(mouse_pos) and not start_button.is_button_clicked():
                            game_state = "playing"
                            start_button.set_button_clicked(True)
                        if quit_button_rect.collidepoint(mouse_pos) and not quit_button.is_button_clicked():
                            running = False
                            quit_button.set_button_clicked(False)
                if event.type == pygame.MOUSEBUTTONUP:
                    start_button.set_button_clicked(False)
                    quit_button.set_button_clicked(False)

            elif game_state == "playing":

                display_surf.fill(BG_COLOR)

                playing_buttons_x: int = SCREEN_WIDTH - 150
                playing_buttons_y: int = (SCREEN_HEIGHT // 3) + 50
                playing_buttons_width: int = 120
                playing_buttons_height: int = 50

                hit_button_x: int = playing_buttons_x
                hit_button_y: int = playing_buttons_y
                hit_button: button.Button = button.Button(hit_button_x, hit_button_y, playing_buttons_width, playing_buttons_height)
                hit_button.set_button_text("Hit", game_font)
                hit_button_rect: pygame.Rect = hit_button.draw(display_surf)

                stand_button_x: int = playing_buttons_x
                stand_button_y: int = playing_buttons_y + 70
                stand_button: button.Button = button.Button(stand_button_x, stand_button_y, playing_buttons_width, playing_buttons_height)
                stand_button.set_button_text("Stand", game_font)
                stand_button_rect: pygame.Rect = stand_button.draw(display_surf)

                quit_button_x: int = playing_buttons_x
                quit_button_y: int = playing_buttons_y + 140
                quit_button: button.Button = button.Button(quit_button_x, quit_button_y, playing_buttons_width, playing_buttons_height)
                quit_button.set_button_text("Quit", game_font)
                quit_button_rect: pygame.Rect = quit_button.draw(display_surf)
  
                for card in range(len(curr_hand.hand)):
                    card_surf = pygame.image.load(f"{GRAPHICS_DIRECTORY}/{curr_hand.hand[card][0]}_{curr_hand.hand[card][1]}.png")
                    card_rect = card_surf.get_rect(center = (50 + 60 * (card + 1), 400))
                    display_surf.blit(card_surf, card_rect)

                    player_hand_sum, player_busted = curr_hand.calculate_hand()

                    sum_text = game_font.render(str(player_hand_sum), True, 'White')
                    sum_text_rect = sum_text.get_rect(center = (140, 470))
                    display_surf.blit(sum_text, sum_text_rect)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == MouseButton.LEFT.value and not button_clicked:
                        if quit_button_rect.collidepoint(mouse_pos) and not quit_button.is_button_clicked():
                            running = False
                            quit_button.set_button_clicked(True)
                        if hit_button_rect.collidepoint(mouse_pos) and not quit_button.is_button_clicked():
                            hit_button.set_button_clicked(True)
                            if not player_busted:
                                player_hands[hand_index].deal_card(new_shoe)
                            else:
                                if next_hand is not None:
                                    curr_hand = next_hand
                        if stand_button_rect.collidepoint(mouse_pos) and not quit_button.is_button_clicked():
                            stand_button.set_button_clicked(True)
                            if next_hand is not None:
                                curr_hand = next_hand

                dealer_hand_sum, dealer_busted = display_card(display_surf, dealer_hand, True, SCREEN_WIDTH, (1,1), GRAPHICS_DIRECTORY, game_font)

                if event.type == pygame.MOUSEBUTTONUP:
                    hit_button.set_button_clicked(False)
                    stand_button.set_button_clicked(False)
                    quit_button.set_button_clicked(False)

        pygame.display.update()

    pygame.quit()

def display_welcome_screen(display_surf: pygame.Surface, game_font: pygame.font.Font, SCREEN_WIDTH: int, SCREEN_HEIGHT: int, color: tuple):
    """Displays the welcome screen with a message"""

    display_surf.fill(color)  # Fill the screen with green color
    text = game_font.render("Welcome to Blackjack!", True, 'White')
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    display_surf.blit(text, text_rect)

def get_card_sprite(suit: str, rank: str, graphics_directory: str) -> tuple:

    rank_dict: dict = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
    suit_dict: dict = {"heart": 1, "club": 2, "diamond": 3, "spade": 4}

    return (suit_dict[suit], rank_dict[rank])

def display_card(display_surf: pygame.Surface, hand: game.Hand, is_dealer_start: bool, screen_width: int, position: tuple, graphics_directory: str, font: pygame.font) -> tuple[int, bool]:
    """Displays card to the display surface"""

    for card in range(len(hand.hand)):
        if card == 1:
            card_surf = pygame.image.load(f"{graphics_directory}/back_red.png")
        else:
            card_surf = pygame.image.load(f"{graphics_directory}/{hand.get_suit(card)}_{hand.get_rank(card)}.png")
        card_rect = card_surf.get_rect(center = (screen_width // 2 + 60 * (card + 1) - 90, 150))
        display_surf.blit(card_surf, card_rect)
        hand_sum, busted = hand.calculate_hand()

        sum_text = font.render(str(hand_sum), True, 'White')
        sum_text_rect = sum_text.get_rect(center = (screen_width // 2, 220))
        display_surf.blit(sum_text, sum_text_rect)

    return hand_sum, busted


if __name__ == "__main__":
    main()