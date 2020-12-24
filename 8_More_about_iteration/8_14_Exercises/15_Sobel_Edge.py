import sys
#import pillow

#import image
# sys.setExecutionLimit(20000)

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for x in range(1, img.getWidth()-1):
    for y in range(1, img.getHeight()-1):
        Gx = 0
        Gy = 0

        #top left
        p
