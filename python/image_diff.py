import sys
import os

'''


img1 = '/Users/bmosley/Desktop/1.png'
img2 = '/Users/bmosley/Desktop/2.png'

from PIL import Image
from PIL import ImageChops

im1 = Image.open(img1)
im2 = Image.open(img2)

diff = ImageChops.difference(im2, im1).getbbox()

print diff
'''

lst1 = [1, 2, 3, ]
lst2 = [4, 5, 6, ]

lst3 = lst1 + lst2

print(lst3)

lst1.extend(lst2)

print(lst1)

img1 = '/Users/bmosley/Desktop/1.png'

base_name = os.path.basename(img1).split('.')[0]

print(base_name)