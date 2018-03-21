from PIL import Image
import sys
import math

def translation(image,new_x,new_y):
    size = image.size
    size = size[0] + abs(new_x) , size[1] + abs(new_y)
    new = Image.new("L",(size))
    # X positive Y Positive
    if new_x >= 0 and new_y >= 0:
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i+new_x,j), image.getpixel(p)) 
        return new
    # X negative , Y negative
    if new_x < 0 and new_y < 0:
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i,j+ abs(new_y)), image.getpixel(p)) 
        return new
    # X negative, Y positive
    if new_x < 0 and new_y > 0: 
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i,j), image.getpixel(p)) 
        return new  
    # X positive , Y negative
    else:
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i + abs(new_x), j + abs(new_y)), image.getpixel(p)) 
        return new  
        
        
def reflexao(image, eixo):    
    x = lambda x: x
    y = lambda y: y    
    
    if "x" in eixo:
        x = lambda x: image.size[0] -1 -x
    elif "y" in eixo: 
        y = lambda y: image.size[1] -1 -y

    new_image = Image.new("L", image.size)

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            new_image.putpixel( (x(i), y(j) ), image.getpixel( (i,j) ) )

    return new_image

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("compile like this 'python geometric.py 'imagem' 't|r' ")
        exit()
    else :
        if sys.argv[2] == 't' :           
            if len(sys.argv) < 5:
                print("compile like this 'python geometric.py 'imagem' 'opcao' 'X Y' ")
                exit()
            else:
                opt = int(sys.argv[3])
                opt1 = int(sys.argv[4])
                translation(Image.open(sys.argv[1]).convert("L"), opt, opt1).show()
        elif sys.argv[2] == 'r' :
            if len(sys.argv) < 4:
                print("compile like this 'python Interplation.py 'imagem' 'opcao' 'X ou Y' ")
                exit()
            else :
                reflexao(Image.open(sys.argv[1]).convert("L"), sys.argv[3]).show()