import cv2 as cv
import numpy as np
img = cv.imread( "messi5.jpg")
lr1 = cv.pyrDown( img)
lr2 = cv.pyrDown( lr1)
lr3 = cv.pyrDown( lr2)
hr2 = cv.pyrUp( lr3)
hr1 = cv.pyrUp( hr2)
cv.imwrite( "lr1.png", lr1)
cv.imwrite( "lr2.png", lr2)
cv.imwrite( "lr3.png", lr3)
cv.imwrite( "hr2.png", hr2)
cv.imwrite( "hr1.png", hr1)
cv.imshow( "lr1", lr1)
cv.imshow( "hr1", hr1)
cv.waitKey(0)
cv.destroyAllWindows()