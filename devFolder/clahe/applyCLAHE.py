import argparse
import cv2
import copy

CLAHE_CLIP_LIMIT = 3.0
CLAHE_TILE_GRID_SIZE = (8,8)
IMG_DEFALT_SIZE = (360,480)


parser = argparse.ArgumentParser(description='Script to Apply CLAHE on RGB Images.')

parser.add_argument(
    'path',
    type=str,
    help='The path to load the image.')

parser.add_argument(
    '-S',
    '--save',
    type=str,
    default=None,
    required=False,
    help='The local where the image will be saved.')

parser.add_argument(
    '--showImage',
    type=str,
    default="True",
    required=False,
    help='If true shows the image.')


def applyCLAHE(
    image,
    save,
    showImage,
    clipLimit=CLAHE_CLIP_LIMIT,
    tileGridSize=CLAHE_TILE_GRID_SIZE,
    size = IMG_DEFALT_SIZE):

    image = cv2.imread(image)

    #-----Converting image to LAB Color model----------------------------------- 
    labImage = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    #-----Splitting the LAB image to different channels-------------------------
    lChannel,aChannel,bChannel = cv2.split(labImage)

    #-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
    claheLChannel = clahe.apply(lChannel)

    #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    claheLABImage = cv2.merge((claheLChannel,aChannel,bChannel))

    #-----Converting image from LAB Color model to RGB model--------------------
    claheFinalImage = cv2.cvtColor(claheLABImage, cv2.COLOR_LAB2BGR)

    #-----Show the image--------------------------------------------------------
    if showImage:
        sourceImage  = copy.deepcopy(image)
        sourceImage = cv2.resize(sourceImage,size)

        resizedImage = copy.deepcopy(claheFinalImage)
        resizedImage = cv2.resize(resizedImage,size)

        cv2.imshow('Source Image', sourceImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        cv2.imshow('CLAHE Output', resizedImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    if save:
        cv2.imwrite(save, claheFinalImage) 

    return claheFinalImage

if __name__ == '__main__':
    args = parser.parse_args()
    path = args.path
    save = args.save

    if args.showImage.upper() == 'TRUE' or args.showImage.upper() == 'T':
        showImage = True
    else:
        showImage = False

    applyCLAHE(path, save, showImage)