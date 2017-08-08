import cv2
import glob

from os.path import join, dirname, realpath


def segment():
    UPLOAD_FOLDERW = join(dirname(realpath(__file__)),'static/croppedW/')
    UPLOAD_FOLDERL = join(dirname(realpath(__file__)),'static/croppedL/')

    all = sorted(glob.glob(UPLOAD_FOLDERW +'*'))
    folderNo = 0
    for f in all:
        print "FolderName--->", folderNo
        print "FileName---->",f
        img_final = cv2.imread(f)
        img2gray = cv2.cvtColor(img_final, cv2.COLOR_BGR2GRAY)
        _, image = cv2.threshold(img2gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        _, contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        our_contours = []
        for contour in contours:
            [x, y, w, h] = cv2.boundingRect(contour)
            our_contours.append([x, y, w, h])
            # print(our_contours)
        our_contours.sort(key=lambda x: x[0])
        print('CountourLength---->',len(our_contours))

        # print("Counters number--%d"%len(contours))
        index = 10
        for contour in our_contours:
            [x, y, w, h] = contour
            area = w * h
            print(area)
            if area < 100:
                continue
            ik = cv2.rectangle(img_final, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cropped = image[y:y + h, x: x + w]
            cropped = cv2.resize(cropped, (32,32), interpolation=cv2.INTER_LINEAR)

            row, col = cropped.shape[:2]
            bottom = cropped[row - 2:row, 0:col]
            bordersize = 2
            border = cv2.copyMakeBorder(cropped, top=bordersize, bottom = bordersize, left=bordersize, right=bordersize,
                                                 borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0])
            s = UPLOAD_FOLDERL + str(folderNo) +'/letters_' +str(folderNo)+ str(index) + '.png'
            print s
            cv2.imwrite(s,border)
            index = index + 1
            cv2.waitKey(0)
        folderNo = folderNo + 1

    print("Finished")
    return "I have segmented all characters"
