from PIL import Image, ImageDraw, PILLOW_VERSION
import os.path

class MapDrawer:
    def __init__(self, mapFile, flagFile):
        self.flagPath = os.path.join(flagFile)
        self.mapPath = os.path.join(mapFile)

    def drawMap(self, territories, concejos, conqueredTerritory):
        mapImg = Image.open(self.mapPath)
        for territory in territories:
            ownerConcejo = concejos[territory.owner]
            ImageDraw.floodfill(mapImg, xy=territory.posMapa, value=ownerConcejo.color)
        output_img = os.path.join('mapaPintado.png')
        mapImg.save(output_img)