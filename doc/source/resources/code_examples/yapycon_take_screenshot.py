"""
Takes a screenshot from YASARA and displays it inline
in the Python Console.

This code is meant to be executed from
the YaPyCon Python Console.
"""

from yasara_kernel import *
from matplotlib import pyplot as plt

%matplotlib inline

LoadPDB("1crn", download="latest")
screenshot_image = SavePNG("some_screenshot.png")
plt.imshow(screenshot_image)