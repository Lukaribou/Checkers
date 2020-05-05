import pygame
from globals import SLAB_SIZE


class Slab:
    def __init__(self, window, position, num, color):
        self._window = window
        self._position = self.px_position(position)
        self._number = num
        self._color = pygame.Color(color) if isinstance(color, str) else color
        self.draw()

    @staticmethod
    def px_position(pos):
        return pos[0] * SLAB_SIZE, pos[1] * SLAB_SIZE

    def draw(self):
        pygame.draw.rect(
            self._window, self._color, (self._position[0], self._position[1], SLAB_SIZE, SLAB_SIZE))
