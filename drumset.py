from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import urllib  # for reading image from URL
import pygame
#from roi_location import ROI
import sys
from PIL import Image
import pygame,time


pygame.init()
pygame.mixer.init()

d2 = Image.open('/home/aamosh/Desktop/opencv/drumset/drumset_images/d2.png').convert('RGBA')
d2 = d2.resize((250,300), Image.ANTIALIAS)

d3 = Image.open('/home/aamosh/Desktop/opencv/drumset/drumset_images/image.png').convert('RGBA')
d3 = d3.resize((230,330), Image.ANTIALIAS)

d4 = Image.open('/home/aamosh/Desktop/opencv/drumset/drumset_images/drum.png').convert('RGBA')
d4 = d4.resize((260,400), Image.ANTIALIAS)


d = Image.open('/home/aamosh/Desktop/opencv/drumset/drumset_images/d1.png').convert('RGBA')
d = d.resize((250,450), Image.ANTIALIAS)

HI=pygame.mixer.Sound('samples/HiHats1/hihat23.wav')
snare=pygame.mixer.Sound('samples/SnareDrums1/snaredrum1.wav')
KD=pygame.mixer.Sound('samples/KickDrums1/kickdrum11.wav')
bass=pygame.mixer.Sound('samples/BassDrums1/bassdrum3.wav')


# define the lower and upper boundaries of the colors in the HSV color space

lower = {'blue': (97, 100, 117), 'red': (166, 84, 141)}
'''
   , }
, 'yellow': (23, 59, 119),'''
# assign new item lower['blue'] = (93, 10, 0)
upper = {'blue': (117, 255, 255),'red': (186, 255, 255)}
''',', }
, 'yellow': (54, 255, 255),
'''
# define standard colors for circle around the object

colors = {'blue': (255, 0, 0),'red': (0, 0, 255)}
'''{, }
, 'yellow': (0, 255, 217),
          '''
# pts = deque(maxlen=args["buffer"])

# if a video path was not supplied, grab the reference
# to the webcam


camera=cv2.VideoCapture(0)

##############3pos1
green=[]
X=np.arange(20,165)
Y=np.arange(230,340)
green.append(X)
green.append(Y)

############pos2
red=[]
X=np.arange(465,610)
Y=np.arange(230,340)
red.append(X)
red.append(Y)

########pos3

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

count1 = 1               # inside count
count2 = 0               # outside count
count3 = 1
count4 = 0
count5 = 1
count6 = 0
count7 = 1
count8 = 0

count9 = 1               # inside count
count10 = 0               # outside count
count11 = 1
count12 = 0
count13 = 1
count14 = 0
count15 = 1
count16 = 0


while True:

    # grab the current frame
    (grabbed, frame) = camera.read()

    frame=cv2.flip(frame,1)


    pilim = Image.fromarray(frame)
    pilim.paste(d2,box=(-20,250),mask=d2)
    frame = np.array(pilim)

    pilim = Image.fromarray(frame)
    pilim.paste(d3,box=(125,370),mask=d3)
    frame = np.array(pilim)

    pilim = Image.fromarray(frame)
    pilim.paste(d, box=(430, 230), mask=d)
    frame = np.array(pilim)

    pilim = Image.fromarray(frame)
    pilim.paste(d4,box=(300,410),mask=d4)
    frame = np.array(pilim)





    # resize the frame, blur it, and convert it to the HSV
    # color space


    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

   # region = ROI(frame)

    # for each color in dictionary check object in frame
    for key, value in upper.items():
        # construct a mask for the color from dictionary`1, then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask


        kernel = np.ones((9, 9), np.uint8)
        if key=='blue':
            blue_mask = cv2.inRange(hsv, lower[key], upper[key])
            blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
            blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_CLOSE, kernel)

            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            blue_cnts = cv2.findContours(blue_mask.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]
            blue_center = None
            # only proceed if at least one contour was found

            if len(blue_cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                blue_c = max(blue_cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(blue_c)


                M = cv2.moments(blue_c)

                blue_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                if blue_center[0] in green[0] and blue_center[1] in green[1] and count1 == 0:
                    if count2 < 1:

                        HI.play()
                        count2 = count2+1


                else:
                    count1=0
                    count2=0

                if blue_center[0] in red[0] and blue_center[1] in red[1] and count3 == 0:
                    if count4 < 1:

                        snare.play()
                        count4 = count4 + 1

                else:
                    count3 = 0
                    count4 = 0


                if blue_center[0] in white[0] and blue_center[1] in white[1] and count5 == 0:
                    if count6 < 1:

                        KD.play()
                        count6 = count6 + 1

                else:
                    count5 = 0
                    count6 = 0


                if blue_center[0] in black[0] and blue_center[1] in black[1] and count7 == 0:

                    if count8 < 1:

                        bass.play()
                        count8 = count8 + 1


                else:
                    count7 = 0
                    count8 = 0



                # only proceed if the radius meets a minimum size. Correct this value for your obect's size
                if radius > 0.5  :
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)
                    cv2.putText(frame, key + " ball", (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                                colors[key], 2)
        elif key=='red':
            red_mask = cv2.inRange(hsv, lower[key], upper[key])
            red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
            red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)

            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            red_cnts = cv2.findContours(red_mask.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]
            red_center = None
            # only proceed if at least one contour was found

            if len(red_cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                red_c = max(red_cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(red_c)

                M = cv2.moments(red_c)

                red_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                if red_center[0] in green[0] and red_center[1] in green[1] and count9 == 0:
                    if count10 < 1:
                        KD.play()
                        count10 = count10 + 1


                else:
                    count9 = 0
                    count10 = 0

                if red_center[0] in red[0] and red_center[1] in red[1] and count11 == 0:
                    if count12 < 1:
                        snare.play()
                        count12 = count12 + 1

                else:
                    count11 = 0
                    count12 = 0

                if red_center[0] in white[0] and red_center[1] in white[1] and count13 == 0:
                    if count14 < 1:
                        HI.play()
                        count14 = count14 + 1

                else:
                    count13 = 0
                    count14 = 0

                if red_center[0] in black[0] and red_center[1] in black[1] and count15 == 0:

                    if count16 < 1:
                        bass.play()
                        count16 = count16 + 1


                else:
                    count15 = 0
                    count16 = 0

                # only proceed if the radius meets a minimum size. Correct this value for your obect's size
                if radius > 0.5:
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)

                    cv2.putText(frame, key + " ball", (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                                colors[key], 2)
        else:
            pass

    box=[]
    # show the frame to our screen
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
