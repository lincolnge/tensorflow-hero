import os
import shutil

import cv2

# hero list
heros = ['zhongwuyan']

for hero in heros:
    path = '/Users/suclogger/Downloads/' + hero + '/'
    path2 = path.replace(hero, hero + '_2')
    if not os.path.exists(path2):
        os.mkdir(path2)
    for key in range(100, 900):
        if key < 10:
            file = 'IMG_000' + str(key) + '.jpg'
        elif key < 100:
            file = 'IMG_00' + str(key) + '.jpg'
        elif key < 1000:
            file = 'IMG_0' + str(key) + '.jpg'
        else:
            file = 'IMG_' + str(key) + '.jpg'
        if os.path.isfile(path+file):
            img = cv2.imread(path+file, 0)
            height, width = img.shape
            if img.size != 921600:
                img = cv2.resize(img, (1280, 720))
            crop_img = img[448:550, 980:1085]
            cv2.imwrite(path2+file, crop_img)
    shutil.rmtree(path)
    os.rename(os.path.join(path2),
              os.path.join(path))

