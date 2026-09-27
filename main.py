import pygame
import enum
import button
import game
import shoe

class MouseButton(enum.Enum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

class Player():

    def __init__(self, hand: game.Hand, credits: int) -> None:
        self._hand_list: list[game.Hand] = [hand]
        self._hand_sum_list: list[int] = self.hand_list[0].calculate_hand()
        self._credits: int = credits
        self._curr_hand: game.Hand = self.hand_list[0]
        self._next_hand = None
        self._turn: bool = True

    @property
    def hand_list(self) -> list[game.Hand]:
        return self._hand_list

    @property
    def credits(self) -> int:
        return self._credits
    
    @property
    def curr_hand(self) -> game.Hand:
        return self._curr_hand

    @curr_hand.setter
    def curr_hand(self, new_hand: game.Hand) -> None:
        self._curr_hand = new_hand

    @property
    def next_hand(self) -> game.Hand:
        return self._next_hand

    @next_hand.setter
    def next_hand(self, new_hand: game.Hand) -> None:
        self._next_hand = new_hand

    def add_hand(self, new_hand: game.Hand) -> None:
        self._hand_list.append(new_hand)

    def check_player_hand(self):
        pass

class Dealer():

    def __init__(self, hand: game.Hand) -> None:
        self._hand: game.Hand = hand

    @property
    def hand(self) -> game.Hand:
        return self._hand

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
    start_font_size: int = 32
    play_font_size: int = 24
    start_game_font = pygame.font.Font(f"{GAME_DIRECTORY}/fonts/PixeloidMono.ttf", start_font_size)
    play_game_font = pygame.font.Font(f"{GAME_DIRECTORY}/fonts/PixeloidMono.ttf", play_font_size)

    card_spritesheet = pygame.image.load(f"{GRAPHICS_DIRECTORY}/playing_cards_spritesheet.png")

    new_shoe = shoe.Shoe(1)
    player: Player = Player(game.Hand(), 100)
    dealer: Dealer = Dealer(game.Hand())

    deal_hand(player.hand_list[0], dealer.hand, new_shoe)

    running: bool = True
    player_turn: bool = True
    player_busted: bool = False
    dealer_start: bool = True
    dealer_turn: bool = False

    player_hand_sum: int = 0
    hand_index: int = 0

    while(running):

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == "welcome":
                display_welcome_screen(display_surf, start_game_font, SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR)

                welcome_buttons_x: int = (SCREEN_WIDTH - 250) // 2
                welcome_buttons_y: int = (SCREEN_HEIGHT // 2) + 50
                welcome_buttons_width: int = 250
                welcome_buttons_height: int = 50

                start_button_x: int = welcome_buttons_x
                start_button_y: int = welcome_buttons_y
                start_button: button.Button = button.Button(start_button_x, start_button_y, welcome_buttons_width, welcome_buttons_height)
                start_button.button_text = "Start Game"
                start_button.button_text_font = start_game_font
                start_button_rect: pygame.Rect = start_button.draw(display_surf)

                quit_button_x: int = welcome_buttons_x
                quit_button_y: int = welcome_buttons_y + 70
                quit_button: button.Button = button.Button(quit_button_x, quit_button_y, welcome_buttons_width, welcome_buttons_height)
                quit_button.button_text = "Quit"
                quit_button.button_text_font = start_game_font
                quit_button_rect: pygame.Rect = quit_button.draw(display_surf)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == MouseButton.LEFT.value:
                        if start_button_rect.collidepoint(mouse_pos) and not start_button.clicked:
                            game_state = "playing"
                            start_button.clicked = True
                        if quit_button_rect.collidepoint(mouse_pos) and not quit_button.clicked:
                            running = False
                            quit_button.clicked = False
                if event.type == pygame.MOUSEBUTTONUP:
                    start_button.clicked = False
                    quit_button.clicked = False

            elif game_state == "playing":

                display_surf.fill(BG_COLOR)

                playing_buttons_x: int = SCREEN_WIDTH - 150
                playing_buttons_y: int = (SCREEN_HEIGHT // 3) + 50
                playing_buttons_width: int = 100
                playing_buttons_height: int = 40

                hit_button_x: int = playing_buttons_x
                hit_button_y: int = playing_buttons_y
                hit_button: button.Button = button.Button(hit_button_x, hit_button_y, playing_buttons_width, playing_buttons_height)
                hit_button.button_text = "Hit"
                hit_button.button_text_font = play_game_font
                hit_button_rect: pygame.Rect = hit_button.draw(display_surf)

                stand_button_x: int = playing_buttons_x
                stand_button_y: int = playing_buttons_y + 50
                stand_button: button.Button = button.Button(stand_button_x, stand_button_y, playing_buttons_width, playing_buttons_height)
                stand_button.button_text = "Stand"
                stand_button.button_text_font = play_game_font
                stand_button_rect: pygame.Rect = stand_button.draw(display_surf)

                double_down_button_x: int = playing_buttons_x
                double_down_button_y: int = playing_buttons_y + 100
                double_down_button: button.Button = button.Button(double_down_button_x, double_down_button_y, playing_buttons_width, playing_buttons_height)
                double_down_button.button_text = "Double Down"
                double_down_button.button_text_font = play_game_font
                double_down_button_rect: pygame.Rect = double_down_button.draw(display_surf)

                split_button_x: int = playing_buttons_x
                split_button_y: int = playing_buttons_y + 150
                split_button: button.Button = button.Button(split_button_x, split_button_y, playing_buttons_width, playing_buttons_height)
                split_button.button_text = "Split"
                split_button.button_text_font = play_game_font
                split_button_rect: pygame.Rect = split_button.draw(display_surf)

                quit_button_x: int = playing_buttons_x
                quit_button_y: int = playing_buttons_y + 200
                quit_button: button.Button = button.Button(quit_button_x, quit_button_y, playing_buttons_width, playing_buttons_height)
                quit_button.button_text = "Quit"
                quit_button.button_text_font = play_game_font
                quit_button_rect: pygame.Rect = quit_button.draw(display_surf)
  
                for card in range(len(player.curr_hand.hand)):
                    card_surf = pygame.image.load(f"{GRAPHICS_DIRECTORY}/{player.curr_hand.hand[card][0]}_{player.curr_hand.hand[card][1]}.png")
                    card_rect = card_surf.get_rect(center = (50 + 60 * (card + 1), 400))
                    display_surf.blit(card_surf, card_rect)

                    player_hand_sum = player.curr_hand.calculate_hand()

                    if player_hand_sum > 21:
                        player_busted = True
                    else:
                        player_busted = False

                    sum_text = play_game_font.render(str(player_hand_sum), True, 'White')
                    sum_text_rect = sum_text.get_rect(center = (140, 470))
                    display_surf.blit(sum_text, sum_text_rect)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == MouseButton.LEFT.value and not quit_button.clicked:
                        if quit_button_rect.collidepoint(mouse_pos) and not quit_button.clicked:
                            running = False
                            quit_button.clicked = True
                        if player_turn:
                            if hit_button_rect.collidepoint(mouse_pos) and not hit_button.clicked:
                                hit_button.clicked = True
                                if not player_busted:
                                    player.hand_list[hand_index].deal_card(new_shoe)
                                else:
                                    if player.next_hand is not None:
                                        player.curr_hand = player.next_hand
                            if stand_button_rect.collidepoint(mouse_pos) and not stand_button.clicked:
                                stand_button.clicked = True
                                if player.next_hand is not None:
                                    player.curr_hand = player.next_hand
                                else:
                                    player_turn = False

                if player_busted and not player.next_hand:
                    player_turn = False

                if not player_turn:
                    dealer_start = False
                    dealer_turn = True

                dealer_hand_sum = display_card(display_surf, dealer.hand, dealer_start, SCREEN_WIDTH, (1,1), GRAPHICS_DIRECTORY, play_game_font)
                if dealer_hand_sum < 17 and not player_turn:
                    dealer.hand.deal_card(new_shoe)
                else:
                    dealer_turn = False

                if not player_turn and not dealer_turn:
                    compare_hands(player, dealer)

                if event.type == pygame.MOUSEBUTTONUP:
                    hit_button.clicked = False
                    stand_button.clicked = False
                    quit_button.clicked = False

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
        if card == 1 and is_dealer_start:
            card_surf = pygame.image.load(f"{graphics_directory}/back_red.png")
        else:
            card_surf = pygame.image.load(f"{graphics_directory}/{hand.get_suit(card)}_{hand.get_rank(card)}.png")
        card_rect = card_surf.get_rect(center = (screen_width // 2 + 60 * (card + 1) - 90, 150))
        display_surf.blit(card_surf, card_rect)
        hand_sum = hand.calculate_hand()

        if not is_dealer_start:
            sum_text = font.render(str(hand_sum), True, 'White')
            sum_text_rect = sum_text.get_rect(center = (screen_width // 2, 220))
            display_surf.blit(sum_text, sum_text_rect)

    return hand_sum

def compare_hands(player: Player, dealer: Dealer):
    """Compares all player hands with the dealer hand to determine wins, loses, and pushes"""

    hand_win_list = []
    dealer_hand_sum = dealer.hand.calculate_hand()

    for hand in player.hand_list:
        player_hand_sum = hand.calculate_hand()
        if player_hand_sum > 21:
            hand_win_list.append("Lose")
        else:
            if dealer_hand_sum > 21:
                hand_win_list.append("Win")
            else:
                if player_hand_sum > dealer_hand_sum:
                    hand_win_list.append("Win")
                elif player_hand_sum < dealer_hand_sum:
                    hand_win_list.append("Lose")
                else:
                    hand_win_list.append("Push")

    print(hand_win_list)

def deal_hand(player_hand: game.Hand, dealer_hand: game.Hand, shoe: shoe.Shoe) -> None:
    """Deals starting hand in alternating order starting with player"""

    for i in range(2):
        player_hand.deal_card(shoe)
        dealer_hand.deal_card(shoe)

if __name__ == "__main__":
    main()