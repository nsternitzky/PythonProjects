class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move(self, location):
        self.location = location