import sys
import pygame
from sprites import Player, Sheep, Ghost, Obstacle
from config import WIDTH, HEIGHT, SAFE_ZONE_WIDTH, FPS


class Game:
    """Hovedklasse for game loop"""

    def __init__(self, width, height) -> None:
        pygame.init()
        self.width = width
        self.height = height

        # Egenskapen objects er erstattet med
        # separate lister med de ulike objektene som er brukt i spillet
        self.ghosts = [Ghost()]
        self.obstacles = [Obstacle(), Obstacle(), Obstacle()]
        self.sheep = [Sheep(), Sheep(), Sheep()]

        # Legger til pygames skjerm og klokke som kreves for at spillet skal kjøres
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        # Legger til spiller og fonten som skal brukes til å vise score
        self.player = Player((SAFE_ZONE_WIDTH // 2, self.height // 2, 25, 25))
        self.score_font = pygame.font.SysFont("Calibri", 42)

        # Denne er True så lenge spillet kjører
        # Endres til False for å avslutte spillet
        self.game_on = True

        pygame.display.set_caption("Manic Mansion")

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

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player.move("right", self.obstacles)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.player.move("down", self.obstacles)
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player.move("left", self.obstacles)
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player.move("up", self.obstacles)

    def update(self) -> None:
        """Game loop del 2: Sjekk kollisjoner, oppdater spillet og objekter"""
        # Løft sauen hvis spilleren kolliderer med en
        collided_sheep_index = self.player.check_collision(self.sheep)
        if collided_sheep_index != -1:
            if self.player.lifted_sheep:
                self.game_on = False
                return
            self.player.lift_sheep(self.sheep[collided_sheep_index])
            self.sheep.remove(self.player.lifted_sheep)
            self.player.change_speed(2)

        # Slipp sauen, øk poengsum og spawn inn nye objekter
        # når spilleren er tilbake på venstre side
        if self.player.rect.right < 80 and self.player.lifted_sheep:
            self.player.change_speed(3)
            self.player.lifted_sheep = None
            self.player.increment_score()
            self.ghosts.append(Ghost())
            self.obstacles.append(Obstacle())
            self.sheep.append(Sheep())

        if self.player.rect.collidelist(self.ghosts) != -1:
            self.game_on = False

        for ghost in self.ghosts:
            ghost.update()

    def render(self) -> None:
        """Game loop del 3: Fyll bakgrunnen, tegn objekter"""
        self.screen.fill((255, 255, 255))

        self.screen.fill("black", (SAFE_ZONE_WIDTH, 0, 10, self.height))
        self.screen.fill(
            "black", (self.width - SAFE_ZONE_WIDTH - 10, 0, 10, self.height)
        )

        text = self.score_font.render(str(self.player.score), True, "black")
        self.screen.blit(text, (self.width - text.get_width() - 25, 25))

        self.player.draw(self.screen)

        for obj in [*self.ghosts, *self.sheep, *self.obstacles]:
            obj.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    Game(WIDTH, HEIGHT).run()
