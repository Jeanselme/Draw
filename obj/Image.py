import matplotlib.pyplot as plt
import matplotlib.cm as cm

class Image:
    """
        Represents a quick draw
    """

    def __init__(self, key, country, time, recognized, drawing):
        self.key = key
        self.country = country
        self.time = time
        self.recognized = recognized
        self.drawing = drawing

    def plot(self, color, dimension, savefile = None):
        """
            Plots the image
            If color is True : Create a mapping between time and color
            Dimension defined a new square
            If no save file is indicated, prints on screen
        """
        fig = plt.figure()
        for line in self.drawing:
            plt.plot(line[0], line[1])

        # For more realistic output
        plt.gca().invert_yaxis()
        plt.axis('off')

        # Save
        if savefile is None:
            plt.show()
        else:
            plt.savefig(savefile)
