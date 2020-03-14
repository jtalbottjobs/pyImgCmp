import numpy as np
import pyImgCmp
import cv2

show_images = False

# _is_np_array()
def test_is_np_array_1():
    assert pyImgCmp._is_np_array([]) is False
def test_is_np_array_2():
    assert pyImgCmp._is_np_array(np.arange(20).reshape(4,5)) is True

# _is_img_url()
def test_is_img_url_1():
    google_logo = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
    assert pyImgCmp._is_img_url(google_logo) is True
def test_is_img_url_2():
    bad_google_logo = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp-doesnotexist.png'
    assert pyImgCmp._is_img_url(bad_google_logo) is False
def test_is_img_url_3():
    google_homepage = 'https://i.imgur.com/5q2qGJXXXXXX.jpg'
    assert pyImgCmp._is_img_url(google_homepage) is False

# _resolve_img_input()
def test_resolve_img_input_img_path():
    path = "tests\\googlelogo.png"
    np_img = pyImgCmp.resolve_img_input(path)
    if show_images:
        cv2.imshow('test_resolve_img_input_img_path', np_img)
        cv2.waitKey(0)
def test_resolve_img_input_img_url():
    google_logo = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
    np_img = pyImgCmp.resolve_img_input(google_logo)
    if show_images:
        cv2.imshow('test_resolve_img_input_img_url', np_img)
        cv2.waitKey(0)
def test_resolve_img_input_np_array():
    path = "tests\\googlelogo.png"
    np_img = cv2.imread(path, 0)
    np_img = pyImgCmp.resolve_img_input(np_img)
    if show_images:
        cv2.imshow('test_resolve_img_input_img_url', np_img)
        cv2.waitKey(0)

def test_compareImages_1():
    a = "tests\\googlelogo.png"
    b = a
    print(f"Difference between two identical images {pyImgCmp.compareImages(a,b)}")

def test_compareImages_2():
    a = "tests\\googlelogo.png"
    b = "tests\\googlelogo_x2.png"
    if show_images:
        cv2.imshow('a', a)
        cv2.waitKey(0)
        cv2.imshow('b', b)
        cv2.waitKey(0)
    print(f"Difference between two of the same image but difference scales {pyImgCmp.compareImages(a,b)}")

def test_compareImages_3():
    a = "tests\\googlelogo.png"
    b = "tests\\googllogo.png"
    if show_images:
        cv2.imshow('a', a)
        cv2.waitKey(0)
        cv2.imshow('b', b)
        cv2.waitKey(0)
    print(f"Difference between google and googl {pyImgCmp.compareImages(a,b)}")

def test_compareImages_4():
    a = "tests\\googlelogo.png"
    b = "tests\\binglogo.png"
    if show_images:
        cv2.imshow('a', a)
        cv2.waitKey(0)
        cv2.imshow('b', b)
        cv2.waitKey(0)
    print(f"Difference between google and bing {pyImgCmp.compareImages(a,b)}")

def test_compareImages_5():
    a = "tests\\sunset.jpg"
    b = "tests\\sunsetspam.jpg"
    if show_images:
        cv2.imshow('a', a)
        cv2.waitKey(0)
        cv2.imshow('b', b)
        cv2.waitKey(0)
    print(f"Difference between sunset and sunsetspam {pyImgCmp.compareImages(a,b)}")

def test_compareImages_6():
    a = "tests\\sunset.jpg"
    b = "tests\\sunset2.jpg"
    if show_images:
        cv2.imshow('a', a)
        cv2.waitKey(0)
        cv2.imshow('b', b)
        cv2.waitKey(0)
    print(f"Difference between sunset and sunset2 {pyImgCmp.compareImages(a,b)}")