import cv2
import numpy as np
from roi_location import ROI
import pygame

pygame.init()
pygame.mixer.init()


HI=pygame.mixer.Sound('samples/HiHats1/hihat23.wav')
snare=pygame.mixer.Sound('samples/SnareDrums1/snaredrum1.wav')
KD=pygame.mixer.Sound('samples/KickDrums1/kickdrum11.wav')
bass=pygame.mixer.Sound('samples/Cymbals2/cymbalcrash1.wav')


green=[]
X=np.arange(20,165)
Y=np.arange(230,340)
green.append(X)
green.append(Y)

red=[]
X=np.arange(465,610)
Y=np.arange(230,340)
red.append(X)
red.append(Y)

white=[]
X=np.arange(150,300)
Y=np.arange(370,470)
white.append(X)
white.append(Y)

############pos4
black=[]
X=np.arange(350,500)
Y=np.arange(370,470)
black.append(X)
black.append(Y)

####for red ####
count1 = 1               # inside count
count2 = 0               # outside count
count3 = 1
count4 = 0
count5 = 1
count6 = 0
count7 = 1
count8 = 0

###for blue ###

count9 = 1               # inside count
count10 = 0               # outside count
count11 = 1
count12 = 0
count13 = 1
count14 = 0
count15 = 1
count16 = 0



# capturing video through webcam
cap = cv2.VideoCapture(0)
while (1):
    _, img = cap.read()
    cv2.flip(img,1)
    # converting frame(img i.e BGR) to HSV (hue-saturation-value)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # definig the range of red color
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)

    # defining the Range of Blue color
    blue_lower = np.array([99, 115, 150], np.uint8)
    blue_upper = np.array([110, 255, 255], np.uint8)

    # finding the range of red,blue and yellow color in the image
    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)

    # Morphological transformation, Dilation
    kernal = np.ones((5, 5), "uint8")

    red = cv2.dilate(red, kernal)
    red = cv2.morphologyEx(red, cv2.MORPH_OPEN, kernal)
    red = cv2.morphologyEx(red, cv2.MORPH_CLOSE, kernal)

    res = cv2.bitwise_and(img, img, mask=red)

    blue = cv2.dilate(blue, kernal)
    blue = cv2.dilate(blue, kernal)
    blue = cv2.morphologyEx(blue, cv2.MORPH_OPEN, kernal)
    blue = cv2.morphologyEx(blue, cv2.MORPH_CLOSE, kernal)

    res1 = cv2.bitwise_and(img, img, mask=blue)

    X=ROI(img)
    # Tracking the Red Color

    (_, contours, hierarchy) = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cv2.findContours(red.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if (area > 300):

            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))


            cv2.circle(img, (int(x), int(y)), int(radius), (0,0,255), 2)
            cv2.putText(img," red ball", (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 0, 255))

            if center[0] in green[0] and center[1] in green[1] and count1 == 0:
                if count2 < 1:

                    HI.play()
                    count2 = count2+1


            else:
                count1=0
                count2=0


            if center[0] in red[0] and center[1] in red[1] and count3 == 0:
                if count4 < 1:
                    snare.play()
                    count4 = count4 + 1

            else:
                count3 = 0
                count4 = 0

            if center[0] in white[0] and center[1] in white[1] and count5 == 0:
                if count6 < 1:
                    KD.play()
                    count6 = count6 + 1

            else:
                count5 = 0
                count6 = 0

            if center[0] in black[0] and center[1] in black[1] and count7 == 0:

                if count8 < 1:
                    bass.play()
                    count8 = count8 + 1


            else:
                count7 = 0
                count8 = 0

# blue
    (_, contours, hierarchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = cv2.findContours(red.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        c1 = max(cnts1, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c1)
        if (area > 300):

            M = cv2.moments(c1)
            center1 = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.circle(img, (int(x), int(y)), int(radius), (0, 0, 255), 2)
            cv2.putText(img, " red ball", (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (255, 0, 0))



            if center1[0] in green[0] and center1[1] in green[1] and count9 == 0:
                if count10 < 1:

                    HI.play()
                    count10 = count10+1


            else:
                count9=0
                count10=0


            if center1[0] in red[0] and center1[1] in red[1] and count11 == 0:
                if count12 < 1:
                    snare.play()
                    count12 = count12 + 1

            else:
                count11 = 0
                count12 = 0

            if center1[0] in white[0] and center1[1] in white[1] and count13 == 0:
                if count14 < 1:
                    KD.play()
                    count14 = count14 + 1

            else:
                count13 = 0
                count14 = 0

            if center1[0] in black[0] and center1[1] in black[1] and count15 == 0:

                if count16 < 1:
                    bass.play()
                    count16 = count16 + 1


            else:
                count15 = 0
                count16 = 0



    # cv2.imshow("Redcolour",red)
    cv2.imshow("Color Tracking", img)
    # cv2.imshow("red",res)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

''' # Tracking the Blue Color
            
'''
