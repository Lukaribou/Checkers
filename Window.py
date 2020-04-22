import pygame
from Slab import Slab
from Pawn import Pawn

"""
self.slabs = [
 0  1  2  3  4  5  6  7  8  9
10 11 12 13 14 15 16 17 18 19
.............................
90 91 92 93 94 95 96 97 98 99
]
"""


class Window:
    def __init__(self, size, name="Fenêtre PyGame", icon=None, wait_display=False):
        self._window = None
        self._size = size
        self._slabs = []
        self._pawns = []
        if not wait_display:
            self.display(name, icon)

    def get_slabs(self):
        return self._slabs

    def get_pawns(self):
        return self._pawns

    def display(self, name, icon):
        import os
        # Placer la fenêtre sur l'écran
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (pygame.display.Info().current_w / 5, 50)

        self._window = pygame.display.set_mode(self._size)
        pygame.display.set_caption(name)
        self._window.fill(pygame.Color("darkgreen"))
        if icon:
            pygame.display.set_icon(pygame.image.load(icon))

        light = True
        for i in range(10):  # 10 lignes
            for j in range(10):  # 10 dalles par ligne
                self._slabs.append(
                    Slab(self._window, (j, i), i * 10 + j, "antiquewhite" if light else "goldenrod"))
                if not light and (i < 3 or i > 6):  # Pions sur les cases foncées
                    self._pawns.append(
                        Pawn(self._window, (j, i), i * 10 + j, "black" if i < 3 else "whitesmoke"))
                light = not light  # => antiquewhite = !antiquewhite
            light = not light  # On inverse encore pour faire les cases
