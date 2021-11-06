import image

def convertToSepia(img, w, h):
    newImage = image.EmptyImage(w,h)
    for row in range(h):
        for col in range(w):
            p = img.getPixel(col,row)
            
            newred = int(p.getRed() * 0.393 + p.getGreen() * 0.769 + p.getBlue() * 0.189)
            newgreen = int(p.getRed() * 0.349 + p.getGreen() * 0.686 + p.getBlue() * 0.168)    
            newblue = int(p.getRed() * 0.272 + p.getGreen() * 0.534 + p.getBlue() * 0.131)

            newPixel = image.Pixel(newred,newgreen,newblue)
            newImage.setPixel(col,row,newPixel)
   
    return newImage



def makeImage(w, h):
    newImg = image.EmptyImage(w, h)
    rinit = 255
    ginit = 255
    binit = 0
    for col in range(w):
        r = rinit
        g = ginit
        b = binit
        for row in range(h):
            r = r - 4
            g = g - 2
            b = b + 2
            newpixel = image.Pixel(r, g, b)
            newImg.setPixel(col, row, newpixel)
        rinit = rinit - 3
        ginit = ginit - 2
        binit = binit + 2
    return newImg

win = image.ImageWin()
img = makeImage(30,50)
img.draw(win)

# change the image to sepia tone by calling your routine
# draw the image onto the window
