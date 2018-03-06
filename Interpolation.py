from PIL import Image
import sys
import timeit

def nearest_neighbor(image, factorx, factory):
    width = int(image.size[0]*factorx)
    height = int(image.size[1]*factory)
    print ("New size: ({},{})".format(width, height))

    output = Image.new("L", (width, height))
    for i in range(width):
        for j in range(height):
            pixel = (int(i/factorx), int(j/factory))
            output.putpixel((i,j), image.getpixel(pixel))
    return output

def bilinear(image, factorx, factory):
    width = int(image.size[0]*factorx)
    height = int(image.size[1]*factory)
    print ("New size: ({},{})".format(width, height))

    ratio_x = float(image.size[0]/width)
    ratio_y = float(image.size[1]/height)

    output = Image.new("L", (width, height))

    for y in range(height):
        py = int(y*ratio_y)
        dy = float(y*ratio_y)-py

        for x in range(width):

            px = int(x*ratio_x)
            dx = float(x*ratio_x)-px

            if(px==image.size[0]-1 or py==image.size[1]-1):
                break
            pixelValue = dx*dy*image.getpixel(((px+1),(py+1)))+(1-dy)*dx*image.getpixel(((px+1),py))+dy*(1-dx)*image.getpixel((px,(py+1)))+(1-dx)*(1-dy)*image.getpixel((px,py))
            output.putpixel((x,y),round(pixelValue))
    return output


def main():
    if(len(sys.argv) < 5):
        print ("Compile like this: python3 Interpolation.py 'image_name' 'interpolation_type (b|n) b = bilinear n = nearest_neighbor' 'factor_x (a real number)' 'factor_y (a real number)'")
    else:
        img = Image.open(sys.argv[1]).convert("L");
        factorx = float(sys.argv[3]);
        factory = float(sys.argv[4])
        img.show()
        if(sys.argv[2] == 'b'):
            start = timeit.default_timer()
            im = bilinear(img, factorx, factory)
            stop = timeit.default_timer()
            print("Time running: {}".format(stop-start))
        elif sys.argv[2] == 'n':
            start = timeit.default_timer()
            im = nearest_neighbor(img, factorx, factory)
            stop = timeit.default_timer()
            print("Time running: {}".format(stop-start))
        else:
            return 0
        im.show()

if __name__== "__main__":
    main();