from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import urllib  # for reading image from URL
import pygame
from roi_location import ROI
import sys
import pygame,time

pygame.init()
pygame.mixer.init()


HI=pygame.mixer.Sound('samples/HiHats1/hihat23.wav')
snare=pygame.mixer.Sound('samples/SnareDrums1/snaredrum1.wav')
KD=pygame.mixer.Sound('samples/KickDrums1/kickdrum11.wav')
bass=pygame.mixer.Sound('samples/Cymbals2/cymbalcrash1.wav')


# define the lower and upper boundaries of the colors in the HSV color space

colors_lower_bound_range = {'blue': (97, 100, 117), 'red': (166, 84, 141)}
'''
   , }
, 'yellow': (23, 59, 119),'''

# assign new item lower['blue'] = (93, 10, 0)
colors_upper_bound_range = {'blue': (117, 255, 255),'red': (186, 255, 255)}
''',', }
, 'yellow': (54, 255, 255),
'''
# define standard colors for circle around the object

colors_all = {'blue': (255, 0, 0),'red': (0, 0, 255)}
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

while True:

    # grab the current frame
    (grabbed, frame) = camera.read()
    if(grabbed =='false'):
        raise Exception("Camera not fetching")
    frame=cv2.flip(frame,1)

    # resize the frame, blur it, and convert it to the HSV
    # color space


    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    region = ROI(frame)

    # region = ROI.getGreen(frame)
    # print("Region", region)
    # print(type(region))

    # for each color in dictionary check object in frame
    for key, value in colors_upper_bound_range.items():
        # construct a mask for the color from dictionary`1, then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask

        # noise reduction
        kernel = np.ones((9, 9), np.uint8)
        mask = cv2.inRange(hsv, colors_lower_bound_range[key], colors_upper_bound_range[key])
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        # get the surface to dect the color change location
        im2, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]
        # cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        #                         cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        print("Surface change ", cnts)
        print(type(cnts))

        number_of_surface_change_list = len(cnts)

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            # time.sleep(0.5)
            c = max(cnts, key=cv2.contourArea)
            # c , mask = ROI.find_biggest_contour(mask)
            print( " Testing :: c ",c , mask)

            ((x, y), radius) = cv2.minEnclosingCircle(c)
            print(key + 'radius===', radius)
            M = cv2.moments(c)

            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if center[0] in green[0] and center[1] in green[1] and count1 == 0:
                if count2 < 1:

                    HI.play()
                    time.sleep(0.1)
                    count2 = count2+1


            else:
                count1=0
                count2=0

            if center[0] in red[0] and center[1] in red[1] and count3 == 0:
                if count4 < 1:

                    snare.play()
                    time.sleep(0.1)
                    count4 = count4 + 1

            else:
                count3 = 0
                count4 = 0


            if center[0] in white[0] and center[1] in white[1] and count5 == 0:
                if count6 < 1:

                    KD.play()
                    time.sleep(0.1)
                    count6 = count6 + 1

            else:
                count5 = 0
                count6 = 0


            if center[0] in black[0] and center[1] in black[1] and count7 == 0:

                if count8 < 1:

                    bass.play()
                    time.sleep(0.1)
                    count8 = count8 + 1


            else:
                count7 = 0
                count8 = 0



            # only proceed if the radius meets a minimum size. Correct this value for your obect's size
            if radius > 0.5 :
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius), colors_all[key], 2)

                cv2.putText(frame, key + " ball", (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            colors_all[key], 2)



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



