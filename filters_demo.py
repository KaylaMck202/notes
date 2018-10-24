from PIL import Image

img = Image.open("beach.jpg")
img.show() #original img

pixmap = img.load()

#for i in range(img.size[0]):
#    for j in range(0,img.size[1],5):
#        pixmap[i,j] = (255,255,255)

#r,g,b = pixmap[100,100]
#print(r)
#print(g)
#print(b)

#for i in range(img.size[0]):
#    for j in range(img.size[1]):
#        r,g,b = pixmap[i,j]
#        r+=100
#        g-=50
#        b-=50
#        
#        pixmap[i,j]= (r,g,b)

def black_white():
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r,g,b = pixmap[i,j]
            r=b
            g=r
            b=g
            
            pixmap[i,j]= (r,g,b)
def bright():
    for i in range(img.size[0]):
            for j in range(img.size[1]):
                r,g,b = pixmap[i,j]
                r=r*4
                g=g*4
                b=b*4
                
                pixmap[i,j]= (r,g,b)
def darken():                
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r,g,b = pixmap[i,j]
            r=r//2
            g=g//2
            b=b//2
                    
            pixmap[i,j]= (r,g,b)
            
#for i in range(img.size[0]):
#    for j in range(0,img.size[1],5):
#        r,g,b = pixmap[i,j]
#        r=r//2
#        g=g//2
#        b=b//2
#        
#        pixmap[i,j]= (r,g,b)
#        for k in range(2,img.size[1],6):
#            r,g,b = pixmap[i,k]
#            r=80
#            g= 3
#            b= 5
#            pixmap[i,k]= (r,g,b)
#def net():
for i in range(img.size[0]):
    for j in range(0,img.size[1],5):
        r,g,b = pixmap[i,j]
        r=r//2
        g=g//2
        b=b//2
            
        pixmap[i,j]= (r,g,b)
        for k in range(10,img.size[1],50):
            r,g,b = pixmap[k,j]
            r=100
            g= 3
            b= 5
            pixmap[k,j]= (r,g,b)
            img.save("net.jpg")
def pink_stripe():                
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r,g,b = pixmap[i,j]
            r+=100
            g-=50
            b-=50
                
            pixmap[i,j]= (r,g,b)
            for k in range(1,img.size[1],8):
                r,g,b = pixmap[i,k]
                r+=10
                g-=10
                b+=50
                    
                pixmap[i,k]= (r,g,b)
            #img.save("pink_stripe.jpg")
img.show()
