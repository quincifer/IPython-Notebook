#Darren Tirto
#dt2925@bard.edu
#October 10, 2014
#CMSC 143
#Keith O'Hara
#LAB 6
from Myro import*

picture=makePicture("coolguy.jpg")
picture2=makePicture("coolteacher.jpg")
picture3=makePicture("coolclassroom.jpg")
theCoolestClassInTheWorld=[picture,picture2,picture3]

def resize(image,factor):
     x=getWidth(image)
     y=getHeight(image)
     resizeX=x*factor
     resizeY=y*factor
     resizeImage=makePicture(resizeX,resizeY)
     for y in range(int(resizeY)):
        for x in range(int(resizeX)):
            resizePixel = getPixel(image,x/factor,y/factor)
            c = getColor(resizePixel)
            setPixel(resizeImage,x,y,c)
     show (resizeImage)
#resize(picture,0.5)

def mirror(image):
    mirrorImage=makePicture(getWidth(image),getHeight(image))
    for y in range(getHeight(image)):
       for x in range(getWidth(image)):
           mirrorX=(getWidth(image)-x)
           setPixel(mirrorImage,mirrorX,y,getPixel(image,x,y))
    show(mirrorImage)
#mirror(picture)

def flip(image):
    mirrorImage=makePicture(getWidth(image),getHeight(image))
    for y in range(getHeight(image)):
       for x in range(getWidth(image)):
           mirrorY=(getHeight(image)-y)
           setPixel(mirrorImage,x,mirrorY,getPixel(image,x,y))
    show(mirrorImage)
#flip(picture)

def photobooth(listOfImages):
    for i in range(len(listOfImages)):
        strip=makePicture(getWidth(listOfImages[0]),getHeight(listOfImages[0])*len(listOfImages))
        for y in range(getHeight(listOfImages[i])):
            for x in range(getWidth(listOfImages[i])):
                setPixel(strip,x,y*i,getPixel(listOfImages[i],x,y))
    show(strip)
        
photobooth(theCoolestClassInTheWorld)           