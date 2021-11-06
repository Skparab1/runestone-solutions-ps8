import image
import random

def makeBlockImage(imgWidth, imgHeight, blockWidth, blockHeight, seed):
    random.seed(seed)
    newImg = image.EmptyImage(imgWidth, imgHeight)

    for x in range(0, imgWidth, blockWidth):
        for y in range(0, imgHeight, blockHeight):
            r = random.randrange(256)
            g = random.randrange(256)
            b = random.randrange(256)
            for row in range(x, x + blockWidth):
                for col in range(y, y + blockHeight):
                    newpixel = image.Pixel(r, g, b)
                    if row < imgWidth and col < imgHeight:
                        newImg.setPixel(row, col, newpixel)
    return newImg

def smooth(img, w, h):
    newImage = image.EmptyImage(w,h)
    for row in range(h):
        for col in range(w):
            if row == 0 and col == 0:
                p1 = img.getPixel(col,row)
                p2 = img.getPixel(col+1,row)
                p3 = img.getPixel(col,row+1)
                p4 = img.getPixel(col+1,row+1)
                newred = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed())//4
                newgreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen())//4
                newblue = (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue())//4

            elif row == 0 and col == w-1:
                p1 = img.getPixel(col-1,row)
                p2 = img.getPixel(col,row)
                p3 = img.getPixel(col,row+1)
                p4 = img.getPixel(col-1,row+1)
                newred = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed())//4
                newgreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen())//4
                newblue = (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue())//4


            elif row == h-1 and col == 0:
                p1 = img.getPixel(col+1,row-1)
                p2 = img.getPixel(col,row)
                p3 = img.getPixel(col+1,row)
                p4 = img.getPixel(col,row-1)
                newred = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed())//4
                newgreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen())//4
                newblue = (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue())//4


            elif row == h-1 and col == w-1:
                p1 = img.getPixel(col-1,row-1)
                p2 = img.getPixel(col,row-1)
                p3 = img.getPixel(col-1,row)
                p4 = img.getPixel(col,row)
                newred = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed())//4
                newgreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen())//4
                newblue = (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue())//4
            
            elif row == 0:
                p1 = img.getPixel(col-1,row)
                p2 = img.getPixel(col,row)
                p3 = img.getPixel(col+1,row)
                p4 = img.getPixel(col-1,row+1)
                p5 = img.getPixel(col,row+1)
                p6 = img.getPixel(col+1,row+1)
                newred = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed() + p5.getRed() + p6.getRed())//6
                newgreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen() + p5.getGreen() + p6.getGreen())//6
                newblue = (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue() + p5.getBlue() + p6.getBlue())//6
                
            elif row == h-1:
                p1 = img.getPixel(col-1,row-1)
                p2 = img.getPixel(col,row-1)
                p3 = img.getPixel(col+1,row-1)
                p4 = img.getPixel(col-1,row)
                p5 = img.getPixel(col,row)
                p6 = img.getPixel(col+1,row)
                newred = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed() + p5.getRed() + p6.getRed())//6
                newgreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen() + p5.getGreen() + p6.getGreen())//6
                newblue = (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue() + p5.getBlue() + p6.getBlue())//6
            
            elif col == 0:
                p1 = img.getPixel(col,row-1)
                p2 = img.getPixel(col+1,row-1)
                p3 = img.getPixel(col,row)
                p4 = img.getPixel(col+1,row)
                p5 = img.getPixel(col,row+1)
                p6 = img.getPixel(col+1,row+1)
                newred = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed() + p5.getRed() + p6.getRed())//6
                newgreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen() + p5.getGreen() + p6.getGreen())//6
                newblue = (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue() + p5.getBlue() + p6.getBlue())//6
  
            elif col == w-1:
                p1 = img.getPixel(col-1,row-1)
                p2 = img.getPixel(col,row-1)
                p3 = img.getPixel(col-1,row)
                p4 = img.getPixel(col,row)
                p5 = img.getPixel(col-1,row+1)
                p6 = img.getPixel(col,row+1)
                
                newred = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed() + p5.getRed() + p6.getRed())//6
                newgreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen() + p5.getGreen() + p6.getGreen())//6
                newblue = (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue() + p5.getBlue() + p6.getBlue())//6
                
            else:    
                p1 = img.getPixel(col-1,row-1)
                p2 = img.getPixel(col,row-1)
                p3 = img.getPixel(col+1,row-1)
                p4 = img.getPixel(col-1,row)
                p5 = img.getPixel(col,row)
                p6 = img.getPixel(col+1,row)
                p7 = img.getPixel(col-1,row+1)
                p8 = img.getPixel(col,row+1)
                p9 = img.getPixel(col+1,row+1)
            
                newred = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed() + p5.getRed() + p6.getRed() + p7.getRed() + p8.getRed() + p9.getRed())//9
                newgreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen() + p5.getGreen() + p6.getGreen() + p7.getGreen() + p8.getGreen() + p9.getGreen())//9
                newblue = (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue() + p5.getBlue() + p6.getBlue() + p7.getBlue() + p8.getBlue() + p9.getBlue())//9

            newPixel = image.Pixel(newred,newgreen,newblue)
            newImage.setPixel(col,row,newPixel)
   
    return newImage



    return newImg

def main():
    win = image.ImageWin()
    width = 100
    height = 50
    img = makeBlockImage(width, height, 10, 10, 1)
    img.draw(win)

    smooth(img, width, height).draw(win)
    win.exitonclick()

if __name__ == "__main__":
    main()

