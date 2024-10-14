import pygame


class Slider:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        min_val,
        max_val,
        current_val,
        title,
        radius=10,
        type="float",
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_val = min_val
        self.max_val = max_val
        self.current_val = current_val
        self.pos = (self.current_val - self.min_val) / (self.max_val - self.min_val) * self.width + self.x  # Position of the slider handle
        self.radius = radius
        self.dragging = False
        self.title = title
        self.font = pygame.font.SysFont(None, 36)
        self.type = type

    def draw(self, screen, colors):
        """Draws the slider on the screen"""
        GRAY, GREEN, BLACK = colors
        pygame.draw.rect(screen, GRAY, (self.x, self.y, self.width, self.height))
        pygame.draw.circle(
            screen, GREEN, (self.pos, self.y + self.height // 2), self.radius
        )
        value_surf = self.font.render(
            f"{self.title}: {self.current_val:.2f}", True, BLACK
        )
        screen.blit(value_surf, (self.x, self.y - 50))

    def handle_event(self, event):
        """Manages mouse events for the slider"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (
                abs(mouse_x - self.pos) < self.radius
                and abs(mouse_y - (self.y + self.height // 2)) < self.radius
            ):
                self.dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        if event.type == pygame.MOUSEMOTION and self.dragging:
            mouse_x, _ = event.pos
            self.pos = max(self.x, min(mouse_x, self.x + self.width))
            self.current_val = (self.pos - self.x) / self.width * (
                self.max_val - self.min_val
            ) + self.min_val
            if self.type=='int':
                self.current_val=int(self.current_val)

    def get_value(self):
        """Returns the current value of the slider"""
        return self.current_val
