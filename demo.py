# coding:utf-8
import time
from glob import glob

import numpy as np
from PIL import Image

import model

paths = glob('./test/*.*')

if __name__ == '__main__':
    im = Image.open("./test/010.png")
    img = np.array(im.convert('RGB'))
    t = time.time()
    result, img, angle = model.model(
        img, model='keras', adjust=True, detectAngle=True)
    print("It takes time:{}s".format(time.time() - t))
    print("---------------------------------------")
    for key in result:
        print(result[key][1])
