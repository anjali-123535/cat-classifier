import cv2
# get the harcascade classifier
face_cascade=cv2.CascadeClassifier("cat_face.xml")

#load the image on which we gonna experiment
coloured_img=cv2.imread("face.jpg")

# turn the colourfull image to black n white bcus the image recognition is much more easy in black n white
# can also read it directly as black n white by
#  img=cv2.imread("face.jpeg",0)
#BLUE GREEN RED TO GRAY SCALE
bnw_img=cv2.cvtColor(coloured_img, cv2.COLOR_BGR2GRAY)

#checking whether the features in cascade file are present in gray scale image or not
faces=face_cascade.detectMultiScale(bnw_img,scaleFactor=1.01,minNeighbors=5)
# scalefactor= accuracy of comparison always >1, if leass than 1 then will alsoconsider the shadows whichlook like cat,lesser the scalefactor more will be the accuracy
#min number of neighboring features around the specific feature
print(type(faces))
print(faces)
for x,y,w,h in faces:
	img=cv2.rectangle(coloured_img,(x,y),(x+w,y+h),(0,255,0),3)
#                                        color    width of the rect
cv2.imshow('cat face',img)
#          name of the window

cv2.waitKey()
# wait for the x key pressed