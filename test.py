import numpy as np
import cv2
 
org_img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv2.Canny(img,300,410)

cv2.imshow("orginial image", org_img)
cv2.imshow("edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()