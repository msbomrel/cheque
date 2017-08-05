import dill
import numpy
import scipy
from scipy.misc import imread
import glob

from os.path import join, dirname, realpath

NNmodel = join(dirname(realpath(__file__)),'static/')

char_number_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                       12: 'C', 13: 'D', 14: 'E',
                       15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
                       25: 'P',
                       26: 'Q', 27: 'R', 28: 'S',
                       29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z', 36: 'a', 37: 'b', 38: 'c',
                       39: 'd',
                       40: 'e', 41: 'f', 42: 'g',
                       43: 'h', 44: 'i', 45: 'j', 46: 'k', 47: 'l', 48: 'm', 49: 'n', 50: 'o', 51: 'p', 52: 'q',
                       53: 'r',
                       54: 's', 55: 't',
                       56: 'u', 57: 'v', 58: 'w', 59: 'x', 60: 'y', 61: 'z'}
with open(NNmodel+'nnnew2.dill', 'rb') as f:  # load the trained Neural Network
    nn = dill.load(f)

UPLOAD_FOLDERL = join(dirname(realpath(__file__)), 'static/croppedL/')
def khojyo_yesle():

    files = sorted(glob.glob(UPLOAD_FOLDERL+'*'))
    data = []
    count = -1

    for file in sorted(list(files)):
        filessss = glob.glob(file + '/*')
        euta = []
        print filessss
        print len(filessss)
        l = []
        for letter in sorted(filessss):
            print 'fileName-------->',letter
            individual_image = imread(letter)
            value = individual_image.flatten()
            inputs = (numpy.asfarray(value // 255 * 0.99 ) + 0.01)
            output = numpy.argmax(nn.predict(inputs))
            euta.append(str(char_number_map[output]))
            print output
        count += 1
        data.append(euta)
    print 'letters--->',count
    print 'data---->',data
    return data
