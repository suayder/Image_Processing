from PIL import Image
import sys

def powerLaw(img, y):
    new_image = Image.new("L", (img.size[0],img.size[1]) )
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            p = (i,j)
            a = float(img.getpixel(p))/255
            a2 = pow(a,y)
            p =  a2* 255
            new_image.putpixel((i,j), int(p))                       
    return new_image


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("compile like this 'python3 intesity.py 'image' 'intensity")
        exit()
    else :
        y = float(sys.argv[2])
        powerLaw(Image.open(sys.argv[1]).convert("L"), y).show()
        