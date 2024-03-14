from duckduckgo_search import ddg_images
from fastcore.all import *
from duckduckgo_search import ddg_images
from fastcore.all import *


import os


iskaggle = os.environ.get('KAGGLE_KERNEL_RUN_TYPE', '')

print("Hi")


if iskaggle:
    pip install -Uqq fastai duckduckgo_search
    pip install -U fastcore
def search_images(term, max_images=30):
    print(f"Searching for '{term}'")
    return L(ddg_images(term, max_results=max_images)).itemgot('image')



def search_images(term, max_images=30):
    print(f"Searching for '{term}'")
    return L(ddg_images(term, max_results=max_images)).itemgot('image')