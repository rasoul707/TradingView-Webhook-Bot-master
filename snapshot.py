
# import requests
# from bs4 import BeautifulSoup
import urllib.request
import cv2
import numpy as np
import config

# def __saveImage():
#     url = 'https://www.tradingview.com/x/ky8cGtAo'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, features="lxml")
#     imgs = soup.find_all('img')
#     imageUrl = None
#     for img in imgs:
#         if img.attrs['alt'] == "TradingView Chart":
#             imageUrl = img.attrs['src']


def saveImage(url):
    id = url.split("/")[-1]
    m = id[0:1].lower()
    imageUrl = 'https://s3.tradingview.com/snapshots/' + m + '/' + id + '.png'
    imgPath = "snapshots/" + m + "-" + id + ".png"
    urllib.request.urlretrieve(imageUrl,  imgPath)
    # cropImage(imgPath)
    return config.baseUrl + "snapshots/" + m + "-" + id


def addWatermark(imgPath, type):
    centerWatermark = cv2.imread("assets/center_watermark.png")
    smallWatermark = cv2.imread("assets/small_watermark.png")
    image = cv2.imread(imgPath)

    background = image
    overlay = centerWatermark

    rows, cols, channels = overlay.shape

    overlay = cv2.addWeighted(
        background[250:250+rows, 0:0+cols],
        1,
        overlay,
        1,
        0
    )

    background[250:250+rows, 0:0+cols] = overlay

    cv2.imshow('res', background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cropImage(imgPath):
    image = cv2.imread(imgPath)
    crop_image = image[24:994, 0:1514]
    cv2.imwrite("snapshots/k-ky8cGtAo-cropped.png", crop_image)