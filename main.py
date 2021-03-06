import pygame
from Window import Window
import globals

# 1 case = 80*80px
# 10 cases par ligne sur 10 lignes


def run():
    pygame.init()
    window = Window((900, 800), "Checkers", "./res/app_icon.png")

    while True:
        globals.update_window(window)
        ev = pygame.event.poll()  # Récupérer tous les évènements
        if ev.type == pygame.QUIT:  # Croix rouge
            break
        if ev.type == pygame.MOUSEBUTTONUP:
            for pawn in window.get_pawns():
                if pawn.is_mouse_in(pygame.mouse.get_pos()):
                    globals.update_tray({'slabs': window.get_slabs(), 'pawns': window.get_pawns()})
                    pawn.on_clicked()
        pygame.display.update()
    pygame.quit()


def get_window():
    return window


if __name__ == '__main__':
    run()
