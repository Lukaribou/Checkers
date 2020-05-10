SLAB_SIZE = 80
PAWN_RADIUS = 25

game_tray = {
    'slabs': None,
    'pawns': None
}

turn = 'black'

pawn_white_color = 'whitesmoke'
pawn_black_color = 'black'


def update_tray(new):
    global game_tray
    game_tray = new


def get_turn():
    return turn


def alternate_turn():
    global turn
    turn = not turn
