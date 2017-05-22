"""
    Draw Project
    By Vincent Jeanselme
    vincent.jeanselme@gmail.com

    Analysis script : Computes a simple analysis of the data
        - Computes number of success by image (and order thanks to percentage
            of success)
"""

from obj.Category import Category
import numpy as np
import argparse
import os

def topSuccess(fileNames):
    """
        Computes the success for each file and reorder the top 10 of best and
        worst
    """
    if fileNames is None:
        # Go through all file in data/
        fileNames = os.listdir('data/')

    successPercentage = []
    for fileName in fileNames:
        # Verify that the given file is a file
        if os.path.isfile(os.path.join('data/', fileName)):
            cat = Category(fileName, 'data/')
            cat.extractJson()
            successPercentage.append(cat.success())
        else:
            print("{} is not a file in data/".format(fileName))

    # Order
    order = np.argsort(successPercentage)
    fileNames = np.array(fileNames)
    successPercentage = np.array(successPercentage)
    print("Top 10 of the easiest images to draw")
    for percentage, fileName in zip(successPercentage[order[-10:]][::-1], fileNames[order[-10:]][::-1]):
        print("{} - {}".format(fileName, percentage))

    print("Top 10 of the hardest")
    for percentage, fileName in zip(successPercentage[order[:10]], fileNames[order[:10]]):
        print("{} - {}".format(fileName, percentage))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw Project by Vincent Jeanselme (vincent.jeanselme@gmail.com)')
    parser.add_argument('-i', '--inputs', nargs='+', help='Files to transform in "data/" (by default all)', default=None)
    args = parser.parse_args()

    topSuccess(args.inputs)
