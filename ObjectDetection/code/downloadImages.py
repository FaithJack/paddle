# coding=utf-8

import os
import requests
import re
import uuid

class DownloadImage:
    def __init__(self, downloadNum, key_word):
        self.download_sum = 0
        self.download_max = downloadNum
        self.key_word = key_word

    def start_download(self, images_path):
        self.download_sum = 0
        gsm = 80
        str_gsm = str(gsm)

        if not os.path.exists(images_path):
            os.makedirs(images_path)

        while self.download_sum < self.download_max:
            str_sum = str(self.download_sum)
            url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&' \
                  'word=' + self.key_word + '&pn=' + str_sum + '&gsm=' + str_gsm + '&ct=&ic=0&lm=-1&width=0&height=0'
            result = requests.get(url)
            self.downloadImage(result.text, images_path)
        print "下载完成"

    def downloadImage(self, html, images_path):
        # 正则表达式
        img_urls = re.findall('"objURL":"(.*?)",', html, re.S)
        print '找到关键词:' + self.key_word + '的图片，现在开始下载图片...'

        for img_url in img_urls:
            print '正在下载第' + str(self.download_sum + 1) + '张图片，图片地址:' + str(img_url)
            try:
                pic = requests.get(img_url, timeout=50)
                pic_path = images_path+ '/' + str(uuid.uuid1()) + '.jpg'
                with open(pic_path, 'wb') as f:
                    f.write(pic.content)
                self.download_sum += 1
                if self.download_sum >= self.download_max:
                    break
            except Exception, e:
                print '【错误】当前图片无法下载，%s' % e
                continue




if __name__ == '__main__':
    downer3 = DownloadImage(100, '车牌')
    downer3.start_download("../data/plate_number/images")