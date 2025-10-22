from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", center, int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt