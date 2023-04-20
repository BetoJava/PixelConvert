import numpy as np
import matplotlib.pyplot as plt
import os

# PARAMETERS --------------------------------------------- #
scale = 4
outlineColor = [.0, .0, .0, 1.0]

# FUNCTIONS ---------------------------------------------- #
def equals(a,b):
    """
    for i in range(a.size):
        if a[i] != b[i]:
            return False
    return True
    """
    return a[-1] == b[-1]


def resizeImage(img, scale, width, height):
    resizedImage = np.array([[[.0, .0, .0, .0] for i in range(height*(scale))] for j in range(width*(scale))])
    for i in range(height):
        for j in range(width):
            for k in range(scale):
                for l in range(scale):
                    resizedImage[i*scale+k,j*scale+l] = img[i,j]
    return resizedImage

def centerImageIn(img, content, scale, width, height, oldSize):
    iStart = oldSize//2
    jStart = oldSize//2
    for i in range(scale*height):
        for j in range(scale*width):
            content[iStart+i, jStart+j] = img[i,j]


def outLine(img, scale):
    copyImg = img.copy()
    void = [.0, .0, .0, .0]
    (width, height, a) = img.shape
    for i in range(0, height-scale, scale):
        for j in range(0, width-scale, scale):
            if not equals(copyImg[i,j], void):
                # Top #
                if equals(copyImg[i-1, j-1], void):
                    img[i-1,j-1] = outlineColor

                if equals(copyImg[i-1, j], void):
                    for k in range(scale):
                        img[i-1,j+k] = outlineColor

                if equals(copyImg[i-1, j+scale], void):
                    img[i-1,j+scale] = outlineColor
                # Middle #
                if equals(copyImg[i, j-1], void):
                    for k in range(scale):
                        img[i+k,j-1] = outlineColor

                if equals(copyImg[i, j+scale], void):
                    for k in range(scale):
                        img[i+k,j+scale] = outlineColor
                # Bottom #
                if equals(copyImg[i+scale, j-1], void):
                    img[i+scale,j-1] = outlineColor

                if equals(copyImg[i+scale, j], void):
                    for k in range(scale):
                        img[i+scale,j+k] = outlineColor

                if equals(copyImg[i+scale, j+scale], void):
                    img[i+scale,j+scale] = outlineColor


def pixelConvert(name, scale = 4.0):
    image = plt.imread(folder + name)
    (width, height, a) = image.shape
    oldSize = width

    finalArray = np.array([[[.0, .0, .0, .0] for i in range(height*(scale+1))] for j in range(width*(scale+1))])

    img = resizeImage(image, scale, width, height)

    centerImageIn(img, finalArray, scale, width, height, oldSize)

    outLine(finalArray, scale)

    #plt.imsave(source + "\\converted\\" + name[:-4] + str(scale*width) + '.png', finalArray)
    
    plt.imsave(source + "\\converted\\" + name[:-4] + '.png', finalArray)

# ----------------------------------------------------- #


source = os.path.realpath(__file__)[:-15]
folder = source + "\\toConvert\\"

images = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

for name in images:
    print(name)
    pixelConvert(name, scale)

os.system('pause')





"""
continuer = True
while continuer:
    name = input("Nom de l'image : ")
    scale = int(input("Agrandissement de : "))

    pixelConvert(name, scale)

    choix = ''
    while choix not in ["O", "o", "n", "N"]:
        choix = input("Continuer (O/N) :")
    
    if choix in ["n", "N"]:
        continuer = False

"""











