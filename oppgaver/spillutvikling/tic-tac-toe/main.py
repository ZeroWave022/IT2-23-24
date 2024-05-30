import sys
import pygame

from sprites import Board, Cell
from config import WIDTH, HEIGHT, FPS


class Game:
    """Hovedklasse for game loop"""

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.board = Board()
        self.cells = Cell.generate_cell_table((3, 3), self.board.cell_size)
        self.player = 1
        self.score = 0
        self.score_font = pygame.font.SysFont("Calibri", 42)

        self.game_on = True
        self.winner = None

        pygame.display.set_caption("Tic Tac Toe")

    def run(self) -> None:
        """Main game loop: Inneholder alle deler av en vanlig game loop"""
        while self.game_on:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def process_input(self) -> None:
        """Game loop del 1: Process game inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not pygame.mouse.get_pressed()[0] or self.winner:
            return

        mouse_pos = pygame.mouse.get_pos()
        # empty_cells = [cell for cell in self.cells if not cell.selected]
        for cell in self.cells:
            if cell.selected:
                continue

            if cell.rect.collidepoint(mouse_pos):
                cell.select("green" if self.player == 1 else "red", self.player)
                self.player = 2 if self.player == 1 else 1
                break

    def update(self) -> None:
        """Game loop del 2: Sjekk kollisjoner, oppdater spillet og objekter"""
        # Check if someone won by taking over a whole row or column
        for i in range(3):
            cells_in_row = [cell for cell in self.cells if cell.position[0] == i]
            cells_in_col = [cell for cell in self.cells if cell.position[1] == i]
            row_owner = cells_in_row[0].owner
            col_owner = cells_in_col[0].owner

            # If all owners are the same
            if row_owner and all(cell.owner == row_owner for cell in cells_in_row):
                self.winner = row_owner
                return

            if col_owner and all(cell.owner == col_owner for cell in cells_in_col):
                self.winner = col_owner
                return

        for diagonal in [[0, 4, 8], [2, 4, 6]]:
            cells = []

            for i in diagonal:
                cells.append(self.cells[i])

            first_owner = cells[0].owner

            if first_owner and all(cell.owner == first_owner for cell in cells):
                self.winner = first_owner
                return

    def render(self) -> None:
        """Game loop del 3: Fyll bakgrunnen, tegn objekter"""
        self.screen.fill((255, 255, 255))

        self.board.draw(self.screen)
        for cell in self.cells:
            self.screen.blit(cell.surface, cell.rect)

        if self.winner:
            text = self.score_font.render(
                f"Player {self.winner} won!", True, "black", "white"
            )
            self.screen.blit(
                text,
                (
                    (WIDTH - text.get_width()) // 2,
                    (HEIGHT - text.get_height()) // 2,
                ),
            )

        pygame.display.flip()


if __name__ == "__main__":
    Game().run()
