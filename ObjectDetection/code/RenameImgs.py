# coding=utf-8

import os

def rename(img_folder):
    # dd
    images_name = os.listdir(img_folder)
    i = 1
    for image_name in images_name:
        img_path = img_folder + image_name
        # 以六位数字命名，符合VOC数据集格式
        name = '%06d.jpg' % i
        dst_name = img_folder + name
        os.rename(img_path, dst_name)
        i += 1
    print "OK"


if __name__ == '__main__':
    images_dir = '../data/plate_number/images/'
    rename(images_dir)