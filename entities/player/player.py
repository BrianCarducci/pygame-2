from entities.entity import Entity

class Player(Entity):
    def __init__(self, sprite, vel):
        super().__init__(sprite, vel)
