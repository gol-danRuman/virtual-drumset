import cv2
import numpy as np
from roi_location import ROI
from PIL import Image
# create an overlay image. You can use any image
#background = np.ones((100, 100, 3), dtype='uint8') * 255
# drum=cv2.imread('hi_hat_opt-1.jpg')
# Open the camera
d = Image.open('/home/aamosh/PycharmProjects/untitled/images/hiset.png').convert('RGBA')
d = d.resize((200,200), Image.ANTIALIAS)
cap = cv2.VideoCapture(0)
# Set initial value of weights
alpha = 0.4
while True:
    # read the frame
    ret, frame = cap.read()
    pilim = Image.fromarray(frame)
    pilim.paste(d, box=(50, 300), mask=d)
    frame = np.array(pilim)
    cv2.flip(frame,1)
    X=ROI(frame)

    # Select the region in the frame where we want to add the image and add the images using cv2.addWeighted()
    #added_image = cv2.addWeighted(frame[150:250, 150:250, :], alpha, background[0:100, 0:100, :], 1 - alpha, 0)
    # added_image = cv2.addWeighted(frame[240:418, 50:224, :], alpha, drum[0:178, 0:174, :], 1 - alpha, 0)
    #
    # # Change the region with the result
    # frame[240:418, 50:224] = added_image
    # For displaying current value of alpha(weights)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'alpha:{}'.format(alpha), (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('a', frame)
    k = cv2.waitKey(10)
    # Press q to break
    if k == ord('q'):
        break
    # press a to increase alpha by 0.1
    if k == ord('a'):
        alpha += 0.1
        if alpha >= 1.0:
            alpha = 1.0
    # press d to decrease alpha by 0.1
    elif k == ord('d'):
        alpha -= 0.1
        if alpha <= 0.0:
            alpha = 0.0
# Release the camera and destroy all windows         
cap.release()
cv2.destroyAllWindows()