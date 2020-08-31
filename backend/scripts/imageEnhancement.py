import cv2

CLAHE_CLIP_LIMIT = 3.0
CLAHE_TILE_GRID_SIZE = (8,8)

def applyCLAHE(
    image,
    clipLimit = CLAHE_CLIP_LIMIT,
    tileGridSize = CLAHE_TILE_GRID_SIZE):

    if isinstance(image, str):
        image = cv2.imread(image)

    labImage = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    lChannel,aChannel,bChannel = cv2.split(labImage)

    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)

    claheLChannel = clahe.apply(lChannel)

    claheLABImage = cv2.merge((claheLChannel,aChannel,bChannel))

    claheFinalImage = cv2.cvtColor(claheLABImage, cv2.COLOR_LAB2BGR)

    return claheFinalImage