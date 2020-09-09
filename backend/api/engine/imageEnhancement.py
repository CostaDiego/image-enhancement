import cv2

CLAHE_CLIP_LIMIT = 3.0
CLAHE_TILE_GRID_SIZE = (8,8)

def applyCLAHE(
    image,
    clipLimit = CLAHE_CLIP_LIMIT,
    tileGridSize = CLAHE_TILE_GRID_SIZE):

    if isinstance(image, str):
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

    #-----Converting image from LAB Color model to BGR model--------------------
    claheFinalImage = cv2.cvtColor(claheLABImage, cv2.COLOR_LAB2BGR)

    return claheFinalImage

def applyRedFree(image):
    if isinstance(image, str):
        image = cv2.imread(image)
        
    #-----Split Channels--------------------------------------------------------
    bChannel, gChannel, rChannel = cv2.split(image)
    rChannel[:] = 0

    #-----Merge the Green and BLue Channel--------------------------------------
    imageBG = cv2.merge((bChannel,gChannel,rChannel))
    
    return imageBG