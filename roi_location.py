import cv2


class ROI:


    def __init__(self,frame):
        cv2.rectangle(frame, (20, 230), (165, 340), (0, 255, 0), 3)  # roi 1 green

        font1 = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'HT', (20, 200), font1, 0.5, (0, 255, 0), 2)
        ################################################
        cv2.rectangle(frame, (465, 230), (610, 340), (0, 0, 255), 3)  # roi 3 red
        font2 = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'bass', (440, 230), font2, 0.5, (0, 0, 255), 2)
        ################################################
        cv2.rectangle(frame, (150, 370), (300, 470), (255, 255, 255), 3)  # roi 2  white
        font3 = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'KD', (150, 360), font3, 0.5, (255, 255, 255), 2)
        #################################################
        cv2.rectangle(frame, (350, 370), (500, 470), (0, 0, 0), 3)  # roi 4  black
        font4 = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, 'snare', (350, 360), font4, 0.5, (0, 0, 0), 2)
