import torch.nn as nn
import torch

# DarkNet_C not include Flatten() and fully connected layers
# C stands for Convolution
DarkNet_C = [
    # kernel size # channels output # strides # padding
    (7, 64, 2, 3),
    # "M" stands for MaxPooling, number 128,256 is output channels
    ("M",192, 
    "M",128, 256, 256, 512,
    "M",256, 512, 256, 512, 256, 512, 256, 512, 512, 1024,
    "M",512, 1024, 512, 1024),
    
    # channels: 1024, size_for_kernel: 3
    (1, 2, 1, 1)
]

# rgb color image
inputChannels = 3 

# There is only two kinds of kernel size: 3 or 1.
size_for_kernel = (3, 1) 
kernel_size_index = 0

# LAYERS [Head, Body, Tail]
Layers_C = []

# [Head] # (7, 64, 2, 3) # kernel size # channels output # strides # padding
first_unit = DarkNet_C[0]
kernelSize = first_unit[0]; outChannels = first_unit[1]; strides = first_unit[2]; padding = first_unit[3]
# first Convolution layer is quite different from others
Layers_C.append(nn.Conv2d(inputChannels, outChannels, kernelSize, strides, padding))

# update input channels
inputChannels = outChannels

# [Body]
for index, unit in enumerate(DarkNet_C[1:-1]):
    # unit is tuple contain "M" or output channels for each layer
    for layer in unit: 

        if layer == "M": 
            # kernel size is 2 and strides is 2 for maxpooling layer
            Layers_C.append(nn.MaxPool2d(kernel_size = 2, stride = 2))

        else: 
            # for this instance: layer is output channels 
            size = size_for_kernel[kernel_size_index % 2]
            Layers_C.append(nn.Conv2d(inputChannels, layer, size, stride = 1, padding = (size-1)//2))

            kernel_size_index += 1
            # update kernel size index and input channels
            inputChannels = layer

# [Tail] # (1, 2, 1, 1) # channels: 1024, kernel size: 3, padding: 1
last_unit = DarkNet_C[-1]
for stride in last_unit:
    Layers_C.append(nn.Conv2d(in_channels = 1024, out_channels = 1024, kernel_size = 3, stride = stride, padding = 1))


darkNet_C = nn.Sequential(*Layers_C)


class DarkNet(nn.Module):
    def __init__(self, convolution_layers, how_many_class = 20):
        super(DarkNet, self).__init__()
        self.conv = convolution_layers
        self.fcl = self._create_fcl(how_many_class)

    def _create_fcl(self, num_cls):
        return nn.Sequential(
            nn.Flatten(),
            nn.Linear(1024 * 7*7, 4096),
            nn.Dropout(0.1),
            nn.LeakyReLU(),
            # 7*7: split whole graph as 7*7 cells, so yolo V1 could only detect 49 object once
            # 2:each cell predict twice, for each time's predict: 1: confidence score, 4: coordinates: x,y, w,h
            # num_cls: how many class could a cell predict, default is 20, so yolo V1 could only predict up to 20 classes
            nn.Linear(4096, 7*7 * ( (2*(1+4)) + num_cls) ),
        )

    def forward(self, x):
        x = self.conv(x)

        return self.fcl(x)

real = DarkNet(darkNet_C)
rng = torch.rand(4, 3, 448, 448) # 4:batch size, 3:rgb, 448,448:image size
result = real(rng)