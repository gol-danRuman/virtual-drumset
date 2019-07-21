import cv2
drum=cv2.imread('hi_hat_opt-1.jpg')
cv2.imshow('frame',drum)
print(drum.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
a=(178, 174, 3)
