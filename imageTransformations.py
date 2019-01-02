import numpy as np

#Turning a 3Dimensions Image in 2 using only Numpy
def rgbToGrayNP(img):
  r,g,b = img[:,:,0], img[:,:,1], img[:,:,2]
  return 0.2989 * r + 0.5870 * g + 0.1140 * b
