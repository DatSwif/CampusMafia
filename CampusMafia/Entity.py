import Hitbox

class Entity(Hitbox.Hitbox):
    """description of class"""
    def __init__(self, abs_topLeft, dimensions, sprites):
        super().__init__(abs_topLeft, dimensions, sprites)