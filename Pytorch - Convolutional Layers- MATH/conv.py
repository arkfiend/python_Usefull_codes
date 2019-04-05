from PIL import Image
from torchvision import transforms 
from torch import nn

#========================================Global params====================================
#Image path
path        = 'a.png'
#Layers = Put 3 if its RGB or 2 in grayScale case
layer       = 3
#Out = Number of out layers. Usually 1. Change this to understand the magic behind
out         = 1
#Kernel Size - size of a mask to convolutions
kernel_size = 1
#Stride - Number of pixels to jump off after a convolution. Minimum is 1.
stride      = 1
#Padding - How many zeros you wanna add in this image before convolution? Minimum is 0
padding     = 0
#========================================Global params====================================



#[1]===Opening image by PIL lib
img = Image.open(path)

#[2]===Transforming image in tensor. (changing the format: HxWxD to DxHxW)
img2Tensor = transforms.Compose([transforms.ToTensor()])
img_ = img2Tensor(img)
#Printing the shape
print (img_.shape)

#[3]===Adding the number of batch size inside of it. Normally a tensor has 4 coordinates: (batch_size, Dimensions, Height, Width)
#This line put a number '1' in position 0, transforming our image in a 4 dimension tensor
img_ = img_.unsqueeze(0)

#[4]===Convoluting the image with all parameters passed 
#                  in   ,   out  ,     kernel       ,    stride  ,  padding
mod = nn.Conv2d( layer  ,   out  ,   kernel_size    ,    stride  ,  padding)
img_ = mod(img_)
#Printing the new shape. 
print (img_.shape)

#[5]===Changing back to image
tensor2Img = transforms.Compose([transforms.ToPILImage()])
#Cutting off the first element of tensor, because to show this one we dont need it
img_ = img_.squeeze(0)
#Was a tensor but for now Image again
img_ = tensor2Img(img_)

#[6]===Showing Image
img_.show()
