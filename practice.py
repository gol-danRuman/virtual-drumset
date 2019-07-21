import numpy as np
import cv2
from drumset.roi_location import ROI

cap = cv2.VideoCapture(0)


green = 0
red = 0
white = 0
black = 0

def ball_detection(color,x,y):
    res=0
    if color in range (x,y):
        print('ball was here and center =',green)

    elif color > y :
        print('ball is outside')
        res=1
    return res



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    region = ROI(frame)

    rand=np.random.randint(6,11,4)
    ####moving ball#####3

    cv2.circle(frame,(120,green),10 , (0,255,0), -1)     ####### green pos1 #####
    cv2.circle(frame,(500,red),10 , (0,0,255), -1)     ####### red pos2 #####
    cv2.circle(frame,(280,white),10 , (255,255,255), -1)     ####### white  pos3 #####
    cv2.circle(frame,(380,black),10 , (0,0,0), -1)     ####### black pos4 #####

#####postion of moving ball #########
    pos1=ball_detection(green,215, 340)
    pos2=ball_detection(red,200, 326)
    pos3=ball_detection(white,380,450)
    pos4=ball_detection(black,380,450)

########condition of moving ball ###########
    if pos1 ==1:
        green=0
    elif pos2 == 1:
        red=0
    elif pos3 == 1:
        white = 0
    elif pos4==1:
        black = 0

######## how  fast all the ball falls
    white+=rand[0]+5
    red+=rand[1]+5
    black+=rand[2]+5
    green+=rand[3]+5

###### adding randomness to falling balls #####

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()