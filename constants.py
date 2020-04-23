SLAB_SIZE = 80
PAWN_RADIUS = 25

game_tray = {
    'slabs': None,
    'pawns': None
}


def update_tray(new):
    global game_tray
    game_tray = new
