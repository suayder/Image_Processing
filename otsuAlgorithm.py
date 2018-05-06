import sys
from PIL import Image


def getWeightBackground(index, hist ,imageSize):
    weight = 0
    for i in range(index):
        weight = weight + hist[i]
    
    return float(weight) / float(imageSize)

def getWeightForeground(index, hist ,imageSize):
    weight = 0
    for i in range(index, len(hist)):
        weight = weight + hist[i]
    
    return float(weight)/float(imageSize)


def getimageSizeBefore(indice, hist):
    sumation = 0
    for i in range(0,indice+1):
        sumation = sumation + hist[i]
    
    if sumation == 0:
        sumation = 1
    
    return sumation

def getimageSizeafter(indice, hist):
    sumation = 0
    for i in range(indice,len(hist)):
        sumation = sumation + hist[i]
    
    if sumation == 0 :
        sumation = 1
    
    return sumation

def getMeanBackground(index, hist):
    if index == 0 : return 0
    mean = 0
    for i in range(index+1):
        mean =  mean + (i * hist[i])
        
    return float(mean)/float(getimageSizeBefore(index, hist))

def getMeanForeground(index, hist):
    if index == 0 : return 0
    mean = 0
    for i in range(index, len(hist)):
        mean =  mean + (i * hist[i])
    
    return float(mean)/float(getimageSizeafter(index, hist))

def getVarianceBackground(index, hist, mean):
    variance = 0
    for i in range(0,index+1):
        variance =  variance + (pow((i - mean),2) * hist[i])
    
    return float(variance)/float(getimageSizeBefore(index, hist))

def getVarianceForeground(index, hist, mean):
    variance = 0
    for i in range(index,len(hist)):
        variance =  variance + (pow((i - mean),2) * hist[i])
    
    return float(variance)/float(getimageSizeafter(index, hist))


def otsu(image):
    hist = image.histogram()
    imageSize = image.size[0]*image.size[1]
    Variacao = []
    
    for i in range(len(hist)):
        Wb = getWeightBackground (i, hist, imageSize)
        Wf = getWeightForeground (i+1, hist, imageSize)
        Mb = getMeanBackground   (i, hist)
        Mf = getMeanForeground   (i, hist)
        Vb = getVarianceBackground(i, hist, Mb)
        Vf = getVarianceForeground(i, hist, Mf)
        Variacao.insert(i, float((Wb*Vb)+(Wf*Vf)))

    return Variacao.index(min(Variacao))


def limiarization(img, threshold):
    newImage = Image.new("L", (img.size[0],img.size[1]) )
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            p = (i,j)
            if img.getpixel(p) > threshold:
                newImage.putpixel((i,j), 255)
            else:
                newImage.putpixel((i,j), 0)  
    
    return newImage

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("compile like this 'python 'otsuAlgorithm.py' 'image name' ")
        exit()
    else:
        image = Image.open(sys.argv[1]).convert("L")
        image.show()
        threshold = otsu(image)
        limiarization(image, threshold).show()


if __name__ == "__main__":
    main()