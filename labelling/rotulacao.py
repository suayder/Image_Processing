# -*- coding: utf-8 -*-
# LABELLING METHODO USING UNION-FIND ARRAYS
import PIL
from PIL import Image, ImageDraw

import sys
import math, random
from itertools import product
from ufarray import *

def BinarizarImagem(image):
    new_image = Image.new("RGB",(image.size[0],image.size[1]))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel((i,j))
            m = (p[0] + p[1] + p[2])/3
            if m > 127:
                new_image.putpixel((i,j),(255,255,255))
            else:
                new_image.putpixel((i,j),(0,0,0))
    return new_image

def Rotulacao(img):
    img = img.convert('L')
    matrizPixel = img.load()
    width, height = img.size
 
    
    uf = UFarray()
    labels = {}
    colors = {}
 
    for y, x in product(range(height), range(width)):
 
    
        if matrizPixel[x, y] == 255:
            pass
     
        elif y > 0 and matrizPixel[x, y-1] == 0:
            labels[x, y] = labels[(x, y-1)]
 
        elif x+1 < width and y > 0 and matrizPixel[x+1, y-1] == 0:
 
            c = labels[(x+1, y-1)]
            labels[x, y] = c
            if x > 0 and matrizPixel[x-1, y-1] == 0:
                a = labels[(x-1, y-1)]
                uf.union(c, a)
 
            elif x > 0 and matrizPixel[x-1, y] == 0:
                d = labels[(x-1, y)]
                uf.union(c, d)
 
        elif x > 0 and y > 0 and matrizPixel[x-1, y-1] == 0:
            labels[x, y] = labels[(x-1, y-1)]
        elif x > 0 and matrizPixel[x-1, y] == 0:
            labels[x, y] = labels[(x-1, y)]
 
        else: 
            labels[x, y] = uf.criaLabel()
 
   
 
    uf.flatten()
    
   

 
    saida_img = Image.new("RGB", (width, height))
    outmatrizPixel = saida_img.load()

    for (x, y) in labels:
 
 
        component = uf.find(labels[(x, y)])

 
        if component not in colors: 
            colors[component] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

 
        outmatrizPixel[x, y] = colors[component]
    print("Regiões: "+str(len(colors)))
    return saida_img
 
def main():
    
    
    img = Image.open(sys.argv[1])
    img.show() #SHOW IMG ORIGINAL
    img = BinarizarImagem(img)      
    img.show() #SHOW IMG BINARIZADA
    img.save(sys.argv[1].split(".")[0] + "_Binarizada." + sys.argv[1].split(".")[1])
    img = Rotulacao(img)
    img.show() #Show IMG ROTULADA
    img.save(sys.argv[1].split(".")[0] + "_Rotulada." + sys.argv[1].split(".")[1])
if __name__ == "__main__": main()