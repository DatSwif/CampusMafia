import Hitbox

class Wall(Hitbox.Hitbox):
    """can't go through"""
    def __init__(self, abs_topLeft, dimensions):
        super().__init__(None, abs_topLeft, None, dimensions, None)