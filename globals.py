SLAB_SIZE = 80
PAWN_RADIUS = 25

game_tray = {
    'slabs': None,
    'pawns': None
}

turn = 'black'


def update_tray(new):
    global game_tray
    game_tray = new


def get_turn():
    return turn


def alternate_turn():
    global turn
    white_turn = not turn
