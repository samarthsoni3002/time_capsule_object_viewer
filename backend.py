from duckduckgo_search import ddg_images
from fastcore.all import * 
from fastai.vision.all import * 
from time import sleep


from duckduckgo_search import ddg_images
from fastcore.all import * 

def search_images(temp, max_images=3):
    return L((ddg_images(temp,max_results=max_images))).itemgot("image")


im = input("Enter object you want to see the images of:- ")
number = int(input("Enter the number of images:- "))


def future_images(im):

    search = im
    path = Path(path/photos)
    destination = (path/search)
    destination.mkdir(exsist_ok = True, parent=True)
    download_images(destination, urls=(f"Futuristic images of {im}"))
    sleep(10)
    resize_images(path/im, max_sizes= 400, destination = path/im)


def old_images(im):
    search = im
    path = Path(path/photos)
    destination = (path/search)
    destination.mkdir(exsist_ok = True, parent=True)
    download_images(destination, urls=(f"old images of {im}"))
    sleep(10)
    resize_images(path/im, max_sizes= 400, destination = path/im)


future_images(im)
