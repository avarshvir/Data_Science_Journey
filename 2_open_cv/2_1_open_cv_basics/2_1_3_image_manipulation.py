import cv2
image = cv2.imread('../images/wall_4.jpg')
img_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('Image2',img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()