from PIL import Image
from matplotlib import pyplot as plt
import sys

def escalaCinza(image):
    new_image = Image.new("L",(image.size[0],image.size[1]))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel((i,j))
            m = (p[0] + p[1] + p[2])/3
            new_image.putpixel((i,j),(m))
    return new_image

def histogramGraph(image):
    x,y = image.size
    colors = image.getcolors(x*y)
    for idx, c in enumerate(colors):
        plt.bar(idx, c[0], color="black")
    plt.show()

def getFrequency(image):    
    qtdPixels = image.size[0]*image.size[1]    
    list2 = image.histogram()
    PrRk = [ (float(list2[i])/float(qtdPixels),i) for i in range(256) ]    
    #print PrRk
    freqEq = []   
    for i in range(256):
        #print i
        #print PrRk[i][0]
        if i == 0:            
            freqEq.append(255*PrRk[i][0])
        else:
            freqEq.append( 255*(PrRk[i][0]) + freqEq[i-1] )
    #print freqEq

    new_image = Image.new("L",(image.size))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel((i,j))
            m = round(freqEq[p])
            new_image.putpixel((i,j), int(m) )
    return new_image

def contrastStrech(image):
    list = image.getcolors()
    c =  list[0][1] 
    d =  list[len(list) - 1][1]
    #print('{} {}'.format(c,d))

    new_image = Image.new("L",(image.size))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = ( image.getpixel((i,j)) - c ) * (float(255)/float((d-c)))
            round(p)
            if p < 0:
                p = 0
                
            new_image.putpixel( (i,j), int(p) )
            
    return new_image

    

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("compile like this 'python3 'equalization.py' 'imageName' ")
        exit()
    else:
        image = Image.open(sys.argv[1]).convert("L")
        image.show()
        histogramGraph(image)
        imageEqualized = getFrequency(image)
        imageEqualized.show()
        histogramGraph(imageEqualized)
    
   