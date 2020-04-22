import pygame


class Slab:
    def __init__(self, window, size, position, num, color):
        """Size: (width, height), position: (line, column), color: ('color_name')"""
        self._window = window
        self._size = (size, size) if isinstance(size, int) else size
        self._position = position
        self._number = num
        self._color = pygame.Color(color) if isinstance(color, str) else color
        self.draw()

    def px_position(self):
        return self._position[0] * self._size[0], self._position[1] * self._size[1]

    def draw(self):
        pos = self.px_position()
        pygame.draw.rect(self._window, self._color, (pos[0], pos[1], self._size[0], self._size[1]))

    def is_mouse_in(self, click):
        """Renvoie True si les coordonnées sont dans la zone du bouton"""
        coord = self.px_position()
        return coord[0] < click[0] < (coord[0] + self._size[0]) and coord[1] < click[1] < (coord[1] + self._size[0])

    def on_clicked(self):
        print("Click", self._number)
