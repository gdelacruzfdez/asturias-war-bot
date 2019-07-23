import randomcolor

rand_color = randomcolor.RandomColor()

def hex_to_rgb(hex):
     hex = hex.lstrip('#')
     hlen = len(hex)
     return tuple(int(hex[i:i+hlen/3], 16) for i in range(0, hlen, hlen/3))

class Concejo:
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.color = hex_to_rgb(rand_color.generate()[0])
        self.owned = [index]

    def isAlive(self):
        return len(self.owned) > 0