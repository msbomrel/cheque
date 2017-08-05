from PIL import Image
from os.path import join, dirname, realpath


UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/images/')
def proc():
    im = Image.open(UPLOAD_FOLDER +"firstImage.png") #Can be many different formats.
    pix = im.load()
    print(im.size) #Get the width and hight of the image for iterating over
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if (pix[i, j][0] > 0  and pix[i, j][1] > 105 and pix[i,j][2] > 0):
                 # print(pix[i, j][1]
                 # print(pix[i, j][1]
                 # print(pix[i, j][2])
                 pix[i,j] = (255,255,255)
            #print(pix[i, j]
    # im.show()
    im.save(UPLOAD_FOLDER + "secondImage.png")
    print 'I am process in 2nd stage'
    return 'OK'