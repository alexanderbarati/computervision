import cv2 as cv

img = cv.imread("Screenshot from 2020-06-16 21-08-07.png")  # reading image from a dic, if the photo is not in
                                                            # the programm file dic, we should enter the dic
print(img.shape)
cv.imshow("img", img)
cv.waitKey(0)  # if you do'nt use this command, the images shows up just for a moment.
cv.destroyWindow("img")  # If you do'nt use this command, the window does not close properly.
cv.destroyAllWindow() # to close properly all the windows
cv.imwrite("test.png", img) # to save the photo

