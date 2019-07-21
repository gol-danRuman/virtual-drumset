import cv2
img = cv2.imread('hi_hat.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('rotation',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()