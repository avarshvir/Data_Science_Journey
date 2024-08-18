import cv2
img = cv2.imread('../images/wall_5.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(img_gray,ddepth=cv2.CV_64F,dx=1, dy=0)
#sobel_y = cv2.Sobel(img_gray,ddepth=cv2.CV_64F,dx=0, dy=1)
#sobel_xy = cv2.Sobel(img_gray,ddepth=cv2.CV_64F,dx=1, dy=1)
#sobel_2_xy = cv2.Sobel(img_gray,ddepth=cv2.CV_64F,dx=2, dy=2)

#print(sobel_x)
cv2.imshow('Image3',sobel_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
