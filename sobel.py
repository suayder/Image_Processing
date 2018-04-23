from PIL import Image
import sys

def get_pixel(image, pixel):

    if pixel[0]<0 and pixel[1]<0:
        return image.getpixel((pixel[0]+1,pixel[1]+1))
    elif pixel[0]<0 and pixel[1]>=image.size[1]:
        return image.getpixel((pixel[0]+1,pixel[1]-1))
    elif pixel[0]>=image.size[0] and pixel[1]>=image.size[1]:
        return image.getpixel((pixel[0]-1,pixel[1]-1))
    elif pixel[0]>=image.size[0] and pixel[1]<0:
        return image.getpixel((pixel[0]-1,pixel[1]+1))
    elif pixel[0]<0 and pixel[1]>=0:
        return image.getpixel((pixel[0]+1,pixel[1]))
    elif pixel[0]>=image.size[0] and pixel[1]>=0:
        return image.getpixel((pixel[0]-1,pixel[1]))
    elif pixel[0]>=0 and pixel[1]<0:
        return image.getpixel((pixel[0],pixel[1]+1))
    elif pixel[0]>=0 and pixel[1]>=image.size[1]:
        return image.getpixel((pixel[0],pixel[1]-1))
    else:
        return image.getpixel(pixel)

def horizontal(image, coord):
    p1 = get_pixel(image,(coord[0]-1,coord[1]-1)) 
    p2 = get_pixel(image,(coord[0]-1,coord[1]))
    p3 = get_pixel(image,(coord[0]-1,coord[1]+1))
    p7 = get_pixel(image,(coord[0]+1,coord[1]-1))
    p8 = get_pixel(image,(coord[0]+1,coord[1]))
    p9 = get_pixel(image,(coord[0]+1,coord[1]+1))
    pMedia = int((-p1) + (-2*p2) + (-p3) + p7 + (2*p8) + p9)
    
    return pMedia

def vertical(image, coord):
    p1 = get_pixel(image,(coord[0]-1,coord[1]-1)) 
    p3 = get_pixel(image,(coord[0]-1,coord[1]+1))
    p4 = get_pixel(image,(coord[0],coord[1]-1))
    p6 = get_pixel(image,(coord[0],coord[1]+1))
    p7 = get_pixel(image,(coord[0]+1,coord[1]-1))
    p9 = get_pixel(image,(coord[0]+1,coord[1]+1))
    pMedia = int((-p1) + p3 + (-2*p4) + (2*p6) + (-p7) + p9)
    
    return pMedia

def sobel(image, masktype):
    new_image = Image.new("L",(image.size),0)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = x,y
            if masktype == 1:
                media = horizontal(image,pixel)
            elif masktype == 2:
                media = vertical(image,pixel)
            new_image.putpixel((x,y), media)
    return new_image

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("compile like this 'python3 'sobel.py' imagePath filter")
        exit()
    else:
        sobel(Image.open(sys.argv[1]).convert("L"), int(sys.argv[2])).show()

if __name__=="__main__":
    main();