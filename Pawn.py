import pygame
from constants import SLAB_SIZE, PAWN_RADIUS


class Pawn:
    def __init__(self, window, position, num, color):
        self._window = window
        self._num = num
        self._color = pygame.Color(color) if isinstance(color, str) else color
        self._alive = True
        self._position = self.px_position(position)

        self.draw()

    @staticmethod
    def px_position(pos):
        return pos[0] * SLAB_SIZE + SLAB_SIZE // 2, pos[1] * SLAB_SIZE + SLAB_SIZE // 2

    def draw(self):
        pygame.draw.circle(self._window, self._color, self._position, PAWN_RADIUS)
        pygame.draw.circle(self._window, pygame.Color('navy'), self._position, PAWN_RADIUS, 1)

    def is_mouse_in(self, click):
        return self._position[0] - PAWN_RADIUS < click[0] < self._position[0] + PAWN_RADIUS and \
               self._position[1] - PAWN_RADIUS < click[1] < self._position[1] + PAWN_RADIUS

    def on_clicked(self):
        from constants import game_tray
        self.dead()

    def dead(self):
        from constants import game_tray
        self._alive = False
        game_tray['slabs'][self._num].draw()
