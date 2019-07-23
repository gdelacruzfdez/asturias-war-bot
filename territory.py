
class Territory:
    def __init__(self, index, name, xPos, yPos, neighbours):
        self.index = index
        self.name = name
        self.posMapa = (xPos, yPos)
        self.neighbours = neighbours
        self.owner = index