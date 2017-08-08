# import the necessary packages
from Services.transform import four_point_transform
import cv2
import glob
from os.path import join, dirname, realpath

UPLOAD_FOLDER = join(dirname(realpath(__file__)),'static/images/')

def detect():
    print "I am called"
    files = glob.glob(UPLOAD_FOLDER +'*')
    for f in files:
        print f
        image = cv2.imread(f)
        orig = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 100, 100)
        print "I am here in loop"
    # show the original image and the edge detected image
        _, cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

        # loop over the contours
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            print peri
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            print len(approx)

            # if our approximated contour has four points, then we
            # can assume that we have found our screen
            if len(approx) == 4:
                screenCnt = approx
                break
        # show the contour (outline) of the piece of paper
        cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 1)

        warped = four_point_transform(orig, screenCnt.reshape(4, 2))

        cropped = cv2.resize(warped, (1500,750), interpolation=cv2.INTER_LINEAR)
        # cv2.imshow('', warped)
        # cv2.waitKey(0)
        s = UPLOAD_FOLDER +'firstImage'+'.png'
        cv2.imwrite(s, cropped)
    return 'OKay'
