from duckduckgo_search import ddg_images
from fastcore.all import * 
import urllib.request
from time import sleep


def search_images(temp, max_images=300):
    return L((ddg_images(temp,max_results=max_images))).itemgot("image")

im = input("Enter object you want to see the images of:- ")
number = int(input("Enter the number of images:- "))


def future_photos(im):
    search = im
    path = Path(im)
    destination = (path/search)
    l = []
    destination.mkdir(exist_ok = True, parents=True)
    download_images(destination, urls=search_images(f"Futuristic images of {im}", max_images=number))
    sleep(20)
    resize_images(path/im, max_sizes= 400, destination = path/im)
    

def past_photos(im):
    os.chdir("photos")
  
    search = im
    path = Path(im)
    destination = (path/search)
    destination.mkdir(exist_ok = True, parents=True)
    download_images(destination, urls=search_images(f"old images of {im}", max_images=number))
    sleep(10)
    resize_images(path/im, max_sizes= 400, destination = path/im)
  

