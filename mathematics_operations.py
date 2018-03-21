from PIL import Image 
import sys


def soma(image1, image2):
    new_image = Image.new("L", image1.size)
    for i in range(new_image.size[0]):
        for j in range(new_image.size[1]):
            p = (i, j)
            pixelvalue = image1.getpixel(p) + image2.getpixel(p)
            if pixelvalue > 255:
                pixelvalue = 255
            new_image.putpixel((i,j), pixelvalue)
    return new_image


def sub(image1, image2):
    newImage = Image.new("L", image1.size)
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            p = (i, j)
            pixelvalue = image1.getpixel(p) - image2.getpixel(p)
            if pixelvalue < 0:
                pixelvalue = 0
            newImage.putpixel((i,j), pixelvalue)
    return newImage

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print(" compile like this 'python3 mathematics_operations.py 'image1' 'image2' operation(sum|sub)")
        exit()
    else :
        image1 = Image.open(sys.argv[1]).convert("L")
        image2 = Image.open(sys.argv[2]).convert("L")
        if sys.argv[3] == 'sum':
            soma(image1,image2).show();
        elif sys.argv[3] == 'sub':
            sub(image1, image2).show();