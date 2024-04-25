from random import choice, randint
import pygame
from config import WIDTH, HEIGHT, SAFE_ZONE_WIDTH


class GameObject(pygame.sprite.Sprite):
    """Baseklassen alle andre klasser arver"""

    def __init__(self, rect_info: tuple) -> None:
        super().__init__()

        # x og y posisjon kan hentes via rect.x og rect.y
        self.rect = pygame.Rect(*rect_info)

    def set_position(self, x: int, y: int) -> None:
        """Endre posisjon til objektet"""
        self.rect.topleft = (x, y)


class Player(GameObject):
    def __init__(self, rect_info: tuple) -> None:
        super().__init__(rect_info)
        self.speed = 3
        self.score = 0
        self.lifted_sheep = None

    def move(self, direction, obstacles):
        """Flytt spiller ved å spesifisere retning og eventuelle hindringer som man skal unngå.
        Utfører sjekk for kollisjon med hindringer."""
        new_rect = self.rect.copy()
        if direction in ["left", "right"]:
            new_rect.x += self.speed if direction == "right" else -self.speed

        if direction in ["up", "down"]:
            new_rect.y += self.speed if direction == "down" else -self.speed

        if new_rect.collidelist(obstacles) != -1:
            return

        self.rect = new_rect

        # Ikke tilatt å flytte utafor skjermen
        if self.rect.x < 0 or self.rect.x > WIDTH:
            self.rect.x = 0 if self.rect.x < 0 else WIDTH - self.rect.width

        if self.rect.y < 0 or self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = 0 if self.rect.y < 0 else HEIGHT - self.rect.height

        if self.rect.collidelist(obstacles) != -1:
            self.rect.x -= self.speed if direction == "right" else -self.speed
            self.rect.y -= self.speed if direction == "down" else -self.speed

    def change_speed(self, speed: int):
        """Endre fart"""
        self.speed = speed

    def increment_score(self):
        """Legg til poeng"""
        self.score += 1

    def lift_sheep(self, sheep):
        """Løft en sau"""
        self.lifted_sheep = sheep

    def check_collision(self, sheep):
        """Sjekk kollisjon(er) med sau(er)"""
        return self.rect.collidelist(sheep)

    def draw(self, dest_surface: pygame.Surface):
        """Tegn spiller"""
        return dest_surface.fill("blue", self.rect)


class Ghost(GameObject):
    def __init__(self) -> None:
        rect_info = (
            randint(SAFE_ZONE_WIDTH, WIDTH - SAFE_ZONE_WIDTH - 25),
            randint(0, HEIGHT - 25),
            25,
            25,
        )
        super().__init__(rect_info)
        self.direction = [choice([-1, 1]), choice([-1, 1])]

    def update(self):
        """Oppdater spøkelset: Endre plassering, eventuelt bytt retning om nødvendig"""
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

        if (
            self.rect.left < SAFE_ZONE_WIDTH + 10
            or self.rect.right > WIDTH - SAFE_ZONE_WIDTH - 10
        ):
            self.rect.x -= self.direction[0]
            self.direction[0] = 1 if self.direction[0] == -1 else -1

        if self.rect.y < 0 or self.rect.y > HEIGHT - 25:
            self.rect.y -= self.direction[1]
            self.direction[1] = 1 if self.direction[1] == -1 else -1

    def draw(self, dest_surface: pygame.Surface):
        """Tegn spøkelse"""
        return dest_surface.fill("yellow", self.rect)


class Obstacle(GameObject):
    def __init__(self) -> None:
        rect_info = (
            randint(SAFE_ZONE_WIDTH, WIDTH - SAFE_ZONE_WIDTH - 25),
            randint(0, HEIGHT - 25),
            25,
            25,
        )
        super().__init__(rect_info)

    def draw(self, dest_surface: pygame.Surface):
        """Tegn hindring"""
        return dest_surface.fill("gray", self.rect)


class Sheep(GameObject):
    def __init__(self) -> None:
        rect_info = (
            randint(WIDTH - SAFE_ZONE_WIDTH, WIDTH - 25),
            randint(0, HEIGHT - 25),
            25,
            25,
        )
        super().__init__(rect_info)
        self.is_lifted = False

    def lift(self):
        """Løft sau"""
        self.is_lifted = True

    def draw(self, dest_surface: pygame.Surface):
        """Tegn sau hvis ikke sauen er løftet"""
        if not self.is_lifted:
            return dest_surface.fill("green", self.rect)
