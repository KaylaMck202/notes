from PIL import Image
img = Image.open("beach.jpg")
#img.show() #original img

pixmap = img.load()

def mirror(img):
    for i in range(img.size[0]//2):
        for j in range(img.size[1]):
            pixmap[i,j], pixmap[img.size[0]-1-i,j] = pixmap[img.size[0]-1-i,j], pixmap[i,j]
        
    img.show()

def bottom_to_top(img):
    for i in range(img.size[0]):
        for j in range(img.size[1]//2):
            pixmap[i,j], pixmap[i,img.size[1]-1-j] = pixmap[i,img.size[1]-1-j], pixmap[i,j]
    img.show()
    
#def mir_1(img):
#    for i in range(img.size[0]//2):
#        for j in range(img.size[1]):
#            pixmap[i,j], pixmap[img.size[0]-1-i,j] = pixmap[img.size[0]-1-i,j], pixmap[i,j]
#        
#    img.show()
def main():
    #mir_1(img)
    #bottom_to_top(img)
    #mirror(img)
    
if __name__=="__main__":
    main()

#pixmap[0,0] = pixmap[639,0]

#pixmap[0,0], pixmap[639,0] = pixmap[639,0], pixmap[0,0]

###Horizontal reflect
#for i in range(img.size[0]//2):
#    for j in range(img.size[1]):
#        pixmap[i,j], pixmap[img.size[0]-1-i,j] = pixmap[img.size[0]-1-i,j], pixmap[i,j]
#        
#img.show()

#new_img = Image.new("RGB",img.size)
#
#new_map = new_img.load()
#from random import randint
#for i in range(img.size[0]):
#    for j in range(img.size[1]):
#        n = randint(0,9)
#        if n >7:
#            pixmap[i,j]=(0,0,0)
#img.show()

#        new_map[i,j] = pixmap[randint(0,img.size[0]-1),randint(0,img.size[1]-1)]
#        new_map[i,j] = pixmap[i%(img.size[0]//2),j]
#new_img.show()