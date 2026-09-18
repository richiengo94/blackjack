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
    clock = pygame.time.Clock()
    FPS = clock.tick(60)
    game_font = pygame.font.Font(f"{GAME_DIRECTORY}/fonts/PixeloidMono.ttf", 32)

    new_game = game.Game(100)
    new_shoe = shoe.Shoe(1)
    player_hand = game.Hand()
    dealer_hand = game.Hand()

    blackjack.deal_hand(player_hand, dealer_hand, new_shoe)


    running: bool = True

    button_clicked: bool = False

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

                for i in range(len(player_hand.hand)):
                    card_surf = pygame.image.load(f"{GRAPHICS_DIRECTORY}/{player_hand.hand[i][0]}_{player_hand.hand[i][1]}.png")
                    card_rect = card_surf.get_rect(center = (50 + 60 * (i + 1), 400))
                    display_surf.blit(card_surf, card_rect)

                    sum_text = game_font.render(str(player_hand.calculate_hand()), True, 'White')
                    sum_text_rect = sum_text.get_rect(center = (140, 470))
                    display_surf.blit(sum_text, sum_text_rect)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == MouseButton.LEFT.value and not button_clicked:
                        if quit_button_rect.collidepoint(mouse_pos) and not quit_button.is_button_clicked():
                            running = False
                            quit_button.set_button_clicked(True)
                        if hit_button_rect.collidepoint(mouse_pos) and not quit_button.is_button_clicked():
                            hit_button.set_button_clicked(True)

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

if __name__ == "__main__":
    main()