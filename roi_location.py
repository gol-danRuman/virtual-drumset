import cv2
import numpy as np

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


    def getGreen(frame):
        return cv2.rectangle(frame, (20, 230), (165, 340), (0, 255, 0), 3)

    # def find_biggest_contour(image):
    #     # Copy
    #     image = image.copy()
    #     # input, gives all the contours, contour approximation compresses horizontal,
    #     # vertical, and diagonal segments and leaves only their end points. For example,
    #     # an up-right rectangular contour is encoded with 4 points.
    #     # Optional output vector, containing information about the image topology.
    #     # It has as many elements as the number of contours.
    #     # we dont need it
    #     _, contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     # Isolate largest contour
    #     contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    #     biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    #
    #     mask = np.zeros(image.shape, np.uint8)
    #     cv2.drawContours(mask, [biggest_contour], -1, 255, -1)
    #     return biggest_contour, mask