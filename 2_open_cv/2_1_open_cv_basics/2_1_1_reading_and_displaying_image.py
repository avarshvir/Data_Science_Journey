import cv2
#reading image
img = cv2.imread("..\images\wall_1.jpg",flags=0)
#print(img)
#print(img.shape)
#showing image
cv2.imshow('Image1',img)
#cv2.imshow('Image1',img[5:200])
cv2.waitKey(0)
cv2.destroyAllWindows()

