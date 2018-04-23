# coding=utf-8

import os
import hashlib
import paddle.v2 as paddle

def get_md5(filename):
    m = hashlib.md5()
    mfile = open(filename, "rb")
    m.update(mfile.read())
    mfile.close()
    md5_value = m.hexdigest()
    return md5_value

if __name__ == '__main__':
    folder_path = "../data/plate_number/images"
    uipath = unicode(folder_path, "utf-8")

    all_imgs_path = os.listdir(uipath)
    for img_name in all_imgs_path:
        img_path = uipath + '/' + img_name
        try:
            img = paddle.image.load_image(img_path)
            height, width = img.shape[:2]
        except:
            os.remove(img_path)



