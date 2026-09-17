import pygame
import enum
import button

class MouseButton(enum.Enum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

def main():

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    GAME_DIRECTORY = "blackjack/assets"

    game_state = "welcome"

    pygame.font.init()
    pygame.display.init()

    display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display_surface.fill('Black')
    pygame.display.set_caption("Blackjack")
    clock = pygame.time.Clock()
    FPS = clock.tick(60)
    game_font = pygame.font.Font(f"{GAME_DIRECTORY}/fonts/PixeloidMono.ttf", 32)

    running: bool = True

    button_clicked: bool = False

    while(running):

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == "welcome":
                display_welcome_screen(display_surface, game_font, SCREEN_WIDTH, SCREEN_HEIGHT)

                start_button_x = (SCREEN_WIDTH - 250) // 2
                start_button_y = (SCREEN_HEIGHT // 2) + 50
                start_button = button.Button(start_button_x, start_button_y, 250, 50)
                start_button.set_button_text("Start Game", game_font)
                start_button_rect = start_button.draw(display_surface)

                quit_button_x = start_button_x
                quit_button_y = start_button_y + 70
                quit_button = button.Button(quit_button_x, quit_button_y, 250, 50)
                quit_button.set_button_text("Quit", game_font)
                quit_button_rect = quit_button.draw(display_surface)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == MouseButton.LEFT.value:
                        if start_button_rect.collidepoint(mouse_pos) and not start_button.is_button_clicked():
                            game_state = "playing"
                            start_button.set_button_clicked = True
                        if quit_button_rect.collidepoint(mouse_pos) and not quit_button.is_button_clicked():
                            running = False
                            quit_button.set_button_clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    start_button.set_button_clicked(False)
                    quit_button.set_button_clicked(False)

            elif game_state == "playing":

                display_surface.fill('Blue')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == MouseButton.LEFT.value and not button_clicked:
                        pass
                        button_clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if button_clicked:
                        button_clicked = False

        pygame.display.update()

    pygame.quit()

def display_welcome_screen(display_surface: pygame.Surface, game_font: pygame.font.Font, SCREEN_WIDTH: int, SCREEN_HEIGHT: int):
    """Displays the welcome screen with a message"""

    display_surface.fill((0, 128, 0))  # Fill the screen with green color
    text = game_font.render("Welcome to Blackjack!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    display_surface.blit(text, text_rect)

if __name__ == "__main__":
    main()