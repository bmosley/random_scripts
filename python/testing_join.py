import os
import shutil
from distutils.dir_util import copy_tree, remove_tree

x = os.path.expanduser('~/Desktop/asd/asd2')
y = os.path.expanduser('~/Desktop/asd/asd3/')

# remove_tree(y)
# copy_tree(x, y)

remove_tree(y)