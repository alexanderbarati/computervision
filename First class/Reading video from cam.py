import cv2 as cv
cap = cv.VideoCapture(0) # if you give 0, it uses laptop cam
while True:
    ret, frame = cap.read()
    if frame is None:           #if do'nt use this, after finishing the video for example, programm stuck
        break

    cv.imshow("frame", frame)

    if cv.waitKey(30) == ord('q'):  # with this command when you press "q", the capture stops.
        break

cap.release()   #disconnecting camera.
cv.destroyAllWindows() # close all open windows
