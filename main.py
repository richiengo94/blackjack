import pygame
import enum

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
    display_surface.fill((0, 128, 0))  # Fill the screen with green color
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
                start_button_rect = display_button(display_surface, game_font, "Start Game", SCREEN_WIDTH, SCREEN_HEIGHT)
                quit_button_rect = display_button(display_surface, game_font, "Quit", SCREEN_WIDTH, SCREEN_HEIGHT + 120)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == MouseButton.LEFT.value and not button_clicked:
                        if start_button_rect.collidepoint(mouse_pos):
                            game_state = "playing"
                        if quit_button_rect.collidepoint(mouse_pos):
                            running = False
                        button_clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if button_clicked:
                        button_clicked = False

            elif game_state == "playing":

                display_surface.fill('Black')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == MouseButton.LEFT.value and not button_clicked:
                        pass
                        button_clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if button_clicked:
                        button_clicked = False

        print(button_clicked)
        pygame.display.update()

    pygame.quit()

def display_welcome_screen(display_surface: pygame.Surface, game_font: pygame.font.Font, SCREEN_WIDTH: int, SCREEN_HEIGHT: int):
    """Displays the welcome screen with a message"""

    display_surface.fill((0, 128, 0))  # Fill the screen with green color
    text = game_font.render("Welcome to Blackjack!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    display_surface.blit(text, text_rect)

def display_button(display_surface: pygame.Surface, game_font: pygame.font.Font, button_text: str, SCREEN_WIDTH: int, SCREEN_HEIGHT: int) -> pygame.Rect:
    """Displays a button on the welcome screen"""

    button_width = 250
    button_height = 50
    button_x = (SCREEN_WIDTH - button_width) // 2
    button_y = (SCREEN_HEIGHT // 2) + 50

    button_rect = pygame.draw.rect(display_surface, (255, 255, 255), (button_x, button_y, button_width, button_height))

    # Draws the text (smaller than button itself)
    button_text = game_font.render(button_text, True, (0, 128, 0))
    button_text_rect = button_text.get_rect(center=(SCREEN_WIDTH // 2, button_y + (button_height // 2)))
    display_surface.blit(button_text, button_text_rect)

    return button_rect  # Return the entire button's rectangle for click detection

if __name__ == "__main__":
    main()