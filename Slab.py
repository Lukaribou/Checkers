import pygame


class Slab:
    def __init__(self, window, size, position, num, color):
        """Size: (width, height), position: (line, column), color: ('color_name')"""
        self._window = window
        self._size = (size, size) if isinstance(size, int) else size
        self._position = self.px_position(position)
        self._number = num
        self._color = pygame.Color(color) if isinstance(color, str) else color
        self.draw()

    def px_position(self, pos):
        return pos[0] * self._size[0], pos[1] * self._size[1]

    def draw(self):
        pygame.draw.rect(
            self._window, self._color, (self._position[0], self._position[1], self._size[0], self._size[1]))

    def is_mouse_in(self, click):
        """Renvoie True si les coordonnées sont dans la zone du bouton"""
        return self._position[0] < click[0] < (self._position[0] + self._size[0]) \
            and self._position[1] < click[1] < (self._position[1] + self._size[0])

    def on_clicked(self):
        print("Click", self._number)
