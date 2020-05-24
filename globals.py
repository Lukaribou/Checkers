from Window import Window

SLAB_SIZE = 80
PAWN_RADIUS = 25

game_tray = {
    'slabs': None,
    'pawns': None
}

turn = 'black'

PAWN_WHITE_COLOR = 'whitesmoke'
PAWN_BLACK_COLOR = 'black'

window: Window


def update_tray(new):
    global game_tray
    game_tray = new


def get_turn():
    return turn


def alternate_turn():
    global turn
    turn = not turn


def get_window() -> Window:
    return window


def update_window(n_window):
    global window
    window = n_window
