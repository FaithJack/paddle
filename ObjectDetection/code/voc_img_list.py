# coding=utf-8

import os
import random

def prepare_filelist(images_path, annotation_path, output_dir):
    trainval_list = []
    test_list = []
    all_images_name = os.listdir(images_path)
    # 当前数据量
    data_num = 1

    for images in all_images_name:
        trainval = []
        test = []

        if data_num % 10 == 0:
            name = images.split('.')[0]
            annotation = os.path.join(annotation_path, name + '.xml')
            if not os.path.exists(annotation):
                continue
            test.append(os.path.join(images_path, images))
            test.append(annotation)
            test_list.append(test)

        else:
            name = images.split('.')[0]
            annotation = os.path.join(annotation_path, name + '.xml')
            if not os.path.exists(annotation):
                continue
            trainval.append(os.path.join(images_path, images))
            trainval.append(annotation)
            trainval_list.append(trainval)

        data_num += 1

    # 为了使得训练数据是随机性的,打乱训练数据
    random.shuffle(trainval_list)
    with open(os.path.join(output_dir, 'trainval.txt'), 'w') as ft:
        for item in trainval_list:
            ft.write(item[0] + ' ' + item[1] + '\n')
    with open(os.path.join(output_dir, 'test.txt'), 'w') as ftest:
        for item in test_list:
            ftest.write(item[0] + ' ' + item[1] + '\n')




if __name__ == '__main__':
    images_path = "../data/plate_number/images"
    labels_path = "../data/plate_number/annotation"
    save_path = "../data/plate_number"
    prepare_filelist(images_path=images_path, annotation_path=labels_path, output_dir=save_path)



