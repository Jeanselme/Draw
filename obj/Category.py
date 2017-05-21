import os
import json
from obj.Image import Image

class Category:
    """
        Represents a full class of drawing
    """
    def __init__(self, fileName, path):
        self.fileName = fileName
        self.path = path
        self.images = []

    def extractJson(self, numberOfImage):
        """
            Opens the json file and extract only numberOfImage
        """
        with open(os.path.join(self.path, self.fileName)) as injson:
            i = 0
            for image in injson:
                if numberOfImage is None or i < numberOfImage:
                    ext = json.loads(image)
                    self.images.append(Image(ext["key_id"], ext["countrycode"],
                        ext["timestamp"], ext["recognized"], ext["drawing"]))
                    i += 1
                else:
                    break
            self.type = ext["word"]

    def plotAll(self, savePath, dimension, color):
        """
            Plots and saves all the image
        """
        for i, image in enumerate(self.images):
            image.plot(color, dimension, os.path.join(savePath, self.fileName + "_{}.png".format(i)))
