from PIL import Image
import sys

def get_pixel(image, pixel):
    if pixel[0]<0 and pixel[1]<0:
        return image.get_pixel((pixel[0]+1,pixel[1]+1))
    elif pixel[0]<0 and pixel[1]>image.size[1]:
        return image.get_pixel((pixel[0]+1,pixel[1]-1))
    elif pixel[0]>image.size[0] and pixel[1]>image.size[1]:
        return image.get_pixel((pixel[0]-1,pixel[1]-1))
    elif pixel[0]>image.size[0] and pixel[1]<0:
        return image.get_pixel((pixel[0]-1,pixel[1]+1))
    elif pixel[0]<0 and pixel[1]>0:
        return image.get_pixel((pixel[0]+1,pixel[1]))
    elif pixel[0]>image.size[0] and pixel[1]>0:
        return image.get_pixel((pixel[0]-1,pixel[1]))
    elif pixel[0]>0 and pixel[1]<0:
        return image.get_pixel((pixel[0],pixel[1]+1))
    elif pixel[0]>0 and pixel[1]>image.size[1]:
        return image.get_pixel((pixel[0],pixel[1]-1))

def mask_1(image, pixel):
    p2 = get_pixel(image,(pixel[0]-1,pixel[1]))
    p4 = get_pixel(image,(pixel[0],pixel[1]-1))
    p5 = get_pixel(image,(pixel[0],pixel[1]))
    p6 = get_pixel(image,(pixel[0],pixel[1]+1))
    p8 = get_pixel(image,(pixel[0]+1,pixel[1]))
    
    pMedia = p2 + p4 + (p5*-4) + p6 + p8

    return pMedia/9

def mask_2(image, pixel):
    p1 = get_pixel(image,(pixel[0]-1,pixel[1]-1)) 
    p2 = get_pixel(image,(pixel[0]-1,pixel[1]))
    p3 = get_pixel(image,(pixel[0]-1,pixel[1]+1))
    p4 = get_pixel(image,(pixel[0],pixel[1]-1))
    p5 = get_pixel(image,(pixel[0],pixel[1])) 
    p6 = get_pixel(image,(pixel[0],pixel[1]+1))
    p7 = get_pixel(image,(pixel[0]+1,pixel[1]-1))
    p8 = get_pixel(image,(pixel[0]+1,pixel[1]))
    p9 = get_pixel(image,(pixel[0]+1,pixel[1]+1))
    pMedia = (p1 + p2 + p3 + p4 + (p5*-8) + p6 + p7 + p8 + p9)
    
    return pMedia/9

def mask_3(image, pixel):
    p2 = get_pixel(image,(pixel[0]-1,pixel[1]))
    p4 = get_pixel(image,(pixel[0],pixel[1]-1))
    p5 = get_pixel(image,(pixel[0],pixel[1])) 
    p6 = get_pixel(image,(pixel[0],pixel[1]+1))
    p8 = get_pixel(image,(pixel[0]+1,pixel[1]))
    pMedia = (-p2) + (-p4) + (p5 *4) + (-p6) + (-p8)
    
    return pMedia/9

def mask_4(image, pixel):
    p1 = get_pixel(image,(pixel[0]-1,pixel[1]-1)) 
    p2 = get_pixel(image,(pixel[0]-1,pixel[1]))
    p3 = get_pixel(image,(pixel[0]-1,pixel[1]+1))
    p4 = get_pixel(image,(pixel[0],pixel[1]-1))
    p5 = get_pixel(image,(pixel[0],pixel[1])) 
    p6 = get_pixel(image,(pixel[0],pixel[1]+1))
    p7 = get_pixel(image,(pixel[0]+1,pixel[1]-1))
    p8 = get_pixel(image,(pixel[0]+1,pixel[1]))
    p9 = get_pixel(image,(pixel[0]+1,pixel[1]+1))
    pMedia = (-p1) + (-p2) + (-p3) + (-p4) + (p5*8) + (-p6) + (-p7) + (-p8) + (-p9)
    
    return pMedia/9

def Laplacian_transform(image, masknum):
    n_image = Image.new("L", (image.size[0], image.size[1]))
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if masknum==1:
                media = mask_1(image, (x,y))
            elif masknum==2:
                media = mask_2(image, (x,y))
            elif masknum==3:
                media = mask_3(image, (x,y))
            elif masknum==4:
                media = mask_4(image, (x,y))
            
            n_image.putpixel((x,y), int(media))

def main():
    if len(sys.argv)!=3:
        print("Compile like this: python3 laplaciano.py 'image_name' 'mask_num'")
        exit()
    else:
        image = Image.open(sys.argv[1]).convert("L")
        mask_num = int(sys.argv[2])
        Laplacian_transform(image, mask_num)

        image.show()

if __name__=="__main__":
    main();