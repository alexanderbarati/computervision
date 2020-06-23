import cv2 as cv

img = cv.imread("map.png")  # plot a line

cv.line(img, (100, 50), (400, 20), (255, 0, 0), 3)
'''(image, start_point, end_point, color, thickness)
   (img, (First dot(W, H)), (Second dot(167, 234)), (Color of line(B, G, R))
   , Thickness)'''

cv.rectangle(img, (100, 100), (200, 200), (255, 0, 0), 3)
'''plot a rectangle
    (image, start_point, end_point, color, thickness)
   (img, (First dot up left corner(W, H)), 
   (Second dot down right corner(167, 234)), (Color of line(B, G, R))
   , Thickness)
'''

cv.circle(img, (150, 150), 100, (0, 255, 0), 3)
'''(image, (middle dot), dimiter,(color), thickness) '''

cv.putText(img, "udacity", (120, 150), cv.FONT_HERSHEY_DUPLEX, 0.60, (0, 255, 0), 1)
'''Writing a text(image, text, (start point, font, size, color, thickness)'''


cv.imshow("frame", img)

cv.waitKey(0)

cv.destroyAllWindows()
