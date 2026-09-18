import pygame

class Button():

    def __init__(self, x: int, y: int, button_width: int, button_height: int) -> None:

        self.clicked: bool = False
        self.x: int = x
        self.y: int = y
        self.button_width: int = button_width
        self.button_height: int = button_height
        self.button_text: str
        self.button_rect: pygame.Rect
        self.button_text_font: pygame.font
        self.text_color: tuple = (0, 128, 0)

    def draw(self, surface: pygame.Surface) -> pygame.rect:

        self.button_rect = pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.button_width, self.button_height))

        if self.button_text:
            button_text = self.button_text_font.render(self.button_text, True, self.text_color)
            button_text_rect = button_text.get_rect(center=(self.button_rect.x + (self.button_width // 2), self.y + (self.button_height // 2)))
            surface.blit(button_text, button_text_rect)

        return self.button_rect
        
    def set_button_text(self, button_text: str, font: pygame.font) -> None:

        self.button_text = button_text
        self.button_text_font = font

    def set_button_position(self, x: int, y: int) -> None:

        self.x = x
        self.y = y

    def set_button_dimensions(self, button_width: int, button_height: int) -> None:

        self.button_width = button_width
        self.button_height = button_height

    def get_button_rect(self) -> pygame.Rect:

        return self.button_rect

    def set_button_clicked(self, clicked: bool) -> None:

        self.clicked = clicked

    def is_button_clicked(self) -> bool:

        return self.clicked

    def set_button_text_color(self, color: tuple) -> None:

        self.text_color = color