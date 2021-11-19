import cv2
import numpy as np

img = cv2.imread('car2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,500,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,120)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
    
cv2.imshow('Binary Image',edges)
cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


