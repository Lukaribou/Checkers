import pygame
from globals import SLAB_SIZE, PAWN_RADIUS


class Pawn:
    def __init__(self, window, position, num, color):
        self._window = window
        self._num = num
        self._color = None
        self._team = ('white', 'black')[color == 'black']
        self._alive = True
        self._position = self.px_position(position)
        self._mvt_choice = False

        self.set_color(color)

    def get_team(self):
        return self._team

    def set_color(self, color):
        self._color = pygame.Color(color) if isinstance(color, str) else color
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

    def on_movement_choice(self):
        self._mvt_choice = True
        self.set_color("green")

    def on_clicked(self):
        from globals import get_turn
        if get_turn() == self._team:
            if not self._mvt_choice:
                self.on_movement_choice()
            else:
                self._mvt_choice = False
        #self.dead()

    def dead(self):
        from globals import game_tray
        self._alive = False
        game_tray['slabs'][self._num].draw()
        game_tray['pawns'][self._num] = self
