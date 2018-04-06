from PIL import Image
import sys
import math

def media_filter(image, mask_size):
    n_image = Image.new("L", (image.size[0], image.size[1]))

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            sum_p = 0
            for i in range(-math.floor(mask_size/2),math.ceil(mask_size/2)):
                a = i
                for j in range(-math.floor(mask_size/2),math.ceil(mask_size/2)):
                    b = j
                    if((x+i)<0 or (x+i)>=image.size[0]):
                        a = i*(-1)
                    if((y+j)<0 or (y+j)>=image.size[1]):
                        b = j*(-1)
                    sum_p += image.getpixel((x+a,y+b))
            n_image.putpixel((x,y),round(sum_p/(mask_size*mask_size)))
    n_image.show()
                     

def main():
    if len(sys.argv)!=3:
        print("Compile like this: python3 media_filter.py 'image_name' 'mask_size'")
        exit()
    else:
        image = Image.open(sys.argv[1]).convert("L")
        mask_size = int(sys.argv[2])
        media_filter(image, mask_size)

        image.show()

if __name__=="__main__":
    main();