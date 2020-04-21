import pygame
from Slab import Slab


class Window:
    def __init__(self, size, name="Fenêtre PyGame", wait_display=False):
        self._window = None
        self._size = size
        self._slabs = []
        if not wait_display:
            self.display(name)

    def display(self, name):
        self._window = pygame.display.set_mode(self._size)
        pygame.display.set_caption(name)
        antiquewhite = True
        for i in range(10):  # 10 lignes
            temp = []
            for j in range(10):  # 10 dalles par ligne
                c = "antiquewhite" if antiquewhite else "maroon"
                temp.append(Slab(self._window, (80, 80), (i, j), c))
                antiquewhite = not antiquewhite  # => antiquewhite = !antiquewhite
            self._slabs.append(temp)
            antiquewhite = not antiquewhite  # On inverse encore pour faire les cases
