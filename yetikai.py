import cv2
from os.path import join, dirname, realpath

UPLOAD_FOLDERS = join(dirname(realpath(__file__)),'static/steps/')
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/images/')
def horaw():
    img1 = cv2.imread(UPLOAD_FOLDER + 'firstImage.png')

    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(UPLOAD_FOLDERS+'grayImage.png', gray)

    edges = cv2.Canny(gray,350,350)
    cv2.imwrite(UPLOAD_FOLDERS+'edgedImage.png', edges)

    ret, threshold = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imwrite(UPLOAD_FOLDERS+'thresholdImage.png', threshold)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9,1))  # to manipulate the orientation of dilution , large x means horizonatally dilating  more, large y means vertically dilating more
    dilated = cv2.dilate(threshold, kernel, iterations=10)  # dilate , more the iteration more the dilation

    cv2.imwrite(UPLOAD_FOLDERS+'dilatedImage.png', dilated)

    _, contours, _ = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    #cv2.drawContours(img, contours, -1, (0,255,0),1)
    print("Counters number--%d"%len(contours))
    index = 0
    for i in range(0, len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(contours[i])
        print(area)
        x,y,w,h = cv2.boundingRect(cnt)
        if (area  < 10000 or area == 0 ):
            continue
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite(UPLOAD_FOLDERS+'BoundedImage.png', img1)
    # cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    # cv2.imshow('Display',img1)
    # cv2.waitKey(0)
    return 'OK'
