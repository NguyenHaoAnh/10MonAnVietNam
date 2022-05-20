import cv2
import os
import numpy as np
for a in range(1,25):
    filename = 'D:\\\\Anh\\\\Python\\\\10MonAnVietNam\\\\test\\\\banhbao\\\\(' + str(a) +').jpg'
    path = 'D:\\\\Anh\\\\Python\\\\10MonAnVietNam\\\\test\\\\banhbao\\\\(' + str(a) + ').jpg'
    frame = cv2.imread(filename)
    img = cv2.resize(frame,(150,150))
    cv2.imwrite(path,img)
    cv2.waitKey(0)
    print(a)
print('Done file')