#pyImgCmp
import os
import urllib.request
import cv2
import numpy as np
import requests
from PIL import ImageChops

READ_MODE = 0


def _is_img_url(img_input):
    # Taken from https://stackoverflow.com/a/48909668
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(img_input)
    try:
        if r.headers["content-type"] in image_formats:
            return True
    except KeyError:
        pass
    return False


def _is_np_array(img_input):
    if type(img_input) == type(np.arange(1)):
        return True
    else:
        return False


def __is_url_with_img(img_input):
    # search the webpage for an img url
    # return true if it contains ANY
    return True


def __get_img_links_from_url(img_input):
    return []


def __img_url_to_np_array(img_input):
    if type(img_input) is not str:
        return None
    save_path = os.path.join(f"{os.getcwd()}", img_input.split('/')[-1])
    urllib.request.urlretrieve(img_input, save_path)
    np_array = cv2.imread(save_path, READ_MODE)
    os.remove(save_path)
    return np_array


def _is_path_to_file(path):
    rtn = False
    if type(path) != type(''):
        return rtn

    try:
        rtn = os.path.exists(path)
    except:
        pass
    return rtn


def resolve_img_input(img_input):
    np_array = None
    # Determine if img path is local or http
    if _is_path_to_file(img_input):
        # Load the img from local file into numpy array
        np_array = cv2.imread(img_input, READ_MODE)
    elif _is_np_array(img_input):
        # Handle np array
        try:
            np_array = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)
        except:
            np_array = img_input
    elif type(img_input) == type(''):
        if _is_img_url(img_input):
            np_array = __img_url_to_np_array(img_input)
        elif __is_url_with_img(img_input):
            # Print warning to USER that the img link provided was
            # a website and not a direct img link. We'll be parsing the largest img
            img_links = __get_img_links_from_url(img_input)
            height = 0
            for img_link in img_links:
                tmp = __img_url_to_np_array(img_link)
                h = (tmp.shape)[0]
                if h > height:
                    height = h
                    np_array = tmp
    else:
        raise ValueError(
            f"Could not resolve Image for input '{img_input}' of type '{type(img_input)}'")

    return np_array


def normalize_images(imgA, imgB):
    heightA, widthA = imgA.shape[:2]
    heightB, widthB = imgB.shape[:2]
    smallest = heightA if heightA <= heightB else heightB
    largest = heightA if heightA >= heightB else heightB

    if largest == smallest:
        return imgA, imgB

    inter_type = cv2.INTER_AREA
    scaling_factor = float(smallest) / float(largest)

    if heightA == largest:
        imgA = cv2.resize(imgA, None, fx=scaling_factor,
                          fy=scaling_factor, interpolation=inter_type)
    if heightB == largest:
        imgB = cv2.resize(imgB, None, fx=scaling_factor,
                          fy=scaling_factor, interpolation=inter_type)

    heightA, widthA = imgA.shape[:2]
    heightB, widthB = imgB.shape[:2]

    if heightA < heightB:
        imgB = imgB[0:heightA, 0:widthB]
    if widthA < widthB:
        imgB = imgB[0:heightB, 0:widthA]
    if heightB < heightA:
        imgA = imgA[0:heightB, 0:widthA]
    if widthB < widthA:
        imgA = imgA[0:heightA, 0:widthB]

    return imgA, imgB


def _init(imgA, imgB):
    imgA = resolve_img_input(imgA)
    imgB = resolve_img_input(imgB)
    imgA, imgB = normalize_images(imgA, imgB)
    return imgA, imgB

def compareImages(imgA, imgB):
    imgA, imgB = _init(imgA, imgB)
    dif = imgA - imgB
    cv2.imshow('dif', dif)
    cv2.waitKey(0)
    return np.sqrt(((imgA - imgB) ** 2).mean())
