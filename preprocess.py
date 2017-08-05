import cv2
import numpy as np
from os.path import join, dirname, realpath


def preprocess():
    UPLOAD_FOLDERW = join(dirname(realpath(__file__)),'static/croppedW/')
    UPLOAD_FOLDER = join(dirname(realpath(__file__)),'static/images/')
    img = cv2.imread(UPLOAD_FOLDER +'secondImage.png')
    height = np.size(img, 0)
    width = np.size(img, 1)
    print width,height
    # cv2.imshow('', img)
    # cv2.waitKey(0)
    #img[y:h, x:w]
    crop_amountn = img[257:308, 1097:1393]
    cv2.imwrite(UPLOAD_FOLDERW + '4cropamountN.png', crop_amountn)

    crop_amountw = img[219:267, 320:986]
    cv2.imwrite(UPLOAD_FOLDERW + '3cropamountW.png', crop_amountw)

    crop_date = img[56:109, 1084:1475]
    cv2.imwrite(UPLOAD_FOLDERW + '2cropdate.png', crop_date)

    crop_name = img[158:222, 350:885]
    cv2.imwrite(UPLOAD_FOLDERW + '1cropname.png', crop_name)
    print "I have cropped all the images"
    return "I have cropped all the images"