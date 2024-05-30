from typing import Self
import pygame
from config import WIDTH, HEIGHT, MARGIN


class GameObject(pygame.sprite.Sprite):
    """Baseklassen alle andre klasser arver"""

    def __init__(self, rect_info: tuple) -> None:
        super().__init__()

        # x og y posisjon kan hentes via rect.x og rect.y
        self.rect = pygame.Rect(*rect_info)

    def set_position(self, x: int, y: int) -> None:
        """Endre posisjon til objektet"""
        self.rect.topleft = (x, y)


class Board(GameObject):
    def __init__(self) -> None:
        super().__init__((MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN))
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        self.surface.fill("white")

        self.cell_size = ((self.rect.width - 10) // 3, (self.rect.height - 10) // 3)

        for i in range(4):
            self.surface.fill("black", (0, self.cell_size[1] * i, self.rect.width, 10))
            self.surface.fill("black", (self.cell_size[0] * i, 0, 10, self.rect.height))

    def draw(self, dest_surface: pygame.Surface):
        return dest_surface.blit(self.surface, self.rect)


class Cell(GameObject):
    def __init__(self, rect_info: tuple, position: tuple) -> None:
        super().__init__(rect_info)
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        self.selected = False
        self.owner = None
        self.position = position
        self.surface.fill("white")

    @classmethod
    def generate_cell_table(cls, table_size, cell_size) -> list[Self]:
        cells = []
        for row in range(table_size[0]):
            for col in range(table_size[1]):
                cells.append(
                    cls(
                        (
                            cell_size[0] * col + MARGIN + 10,
                            cell_size[1] * row + MARGIN + 10,
                            cell_size[0] - 10,
                            cell_size[1] - 10,
                        ),
                        (row, col),
                    )
                )
        return cells

    def select(self, color, owner):
        self.surface.fill(color)
        self.selected = True
        self.owner = owner
