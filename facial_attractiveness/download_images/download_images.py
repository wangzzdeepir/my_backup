#!/usr/bin/python
"""
"""
import requests
import cv2

image_url = 'http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg'

def write_img(IMG_URL, SAVE_PATH):
    """This function writes the image from IMAGE_URL to the SAVE_PATH
    args:
    returns:
    """
    img_data = requests.get(IMG_URL).content
    with open(SAVE_PATH, 'wb') as handler:
        handler.write(img_data)

def check_img(IMG_PATH):
    """
    """
    img = cv2.open(IMG_PATH)
    print type(img)
