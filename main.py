import pygame
from Window import Window


# 1 case = 80*80px
# 10 cases par ligne sur 10 lignes


def run():
    pygame.init()
    window = Window((900, 800))

    while True:
        ev = pygame.event.poll()  # Récupérer tous les évènements
        if ev.type == pygame.QUIT:  # Croix rouge
            break
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    run()
