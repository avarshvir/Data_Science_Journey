from matplotlib import pyplot as plt
import cv2
img = cv2.imread("..\images\wall_1.jpg")
imgluv = cv2.cvtColor(img,cv2.COLOR_BGR2LUV)
cv2.imshow('Image1',imgluv)
cv2.waitKey(0)
cv2.destroyAllWindows()