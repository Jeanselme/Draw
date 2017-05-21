"""
    Draw Project
    By Vincent Jeanselme
    vincent.jeanselme@gmail.com

    Display script : Allows to read the given .njson file
"""

from obj.Category import Category
import argparse
import os

def transformNjson(fileNames, numberOfImage, dimension, color):
    """
        Extracts from data/fileName, a random selection of size numberOfImage
        Saves them in image/fileName_NUM
        Dimension allows to change the dimension of the output image (square)
        And if color is True, changes the black and white into a color which
        represents the evolution through time
    """
    if fileNames is None:
        # Go through all file in data/
        fileNames = os.listdir('data/')

    for fileName in fileNames:
        # Verify that the given file is a file
        if os.path.isfile(os.path.join('data/', fileName)):
            cat = Category(fileName, 'data/')
            cat.extractJson(numberOfImage)
            cat.plotAll('image/', dimension, color)
        else:
            print("{} is not a file in data/".format(fileName))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw Project by Vincent Jeanselme (vincent.jeanselme@gmail.com)')
    parser.add_argument('-i', '--inputs', nargs='+', help='Files to transform in "data/" (by default all)', default=None)
    parser.add_argument('-n', '--number', help='Number of image to extract (by default 10) - Put None if you want all', default=10)
    parser.add_argument('-d', '--dimension', help='Dimension of the output image (by default 128)', default=128)
    parser.add_argument('-c', '--color', dest='color', action='store_true', help='Activate the color evolution', default=False)
    args = parser.parse_args()

    transformNjson(args.inputs, args.number, args.dimension, args.color)
