import cv2
import os

def drawLines(image, arr):
    prev = [arr[0][0], arr[0][1]]
    for i in arr:
        cv2.line(image, (prev[0], prev[1]), (i[0], i[1]), (255, 0, 0), 5)
        prev = [i[0], i[1]]
        #print(str(i[0]) + str(i[1]))

def drawPoints(image, arr):
    for i in arr:
        cv2.line(image, (i[0], i[1]), (i[0], i[1]), (0, 0, 255), 5)

def editShowImage(file_path, arr):
    image = cv2.imread(file_path)
    for i in arr:
        drawLines(image, i)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def camCapture(file_path):
    vid = cv2.VideoCapture(0)

    while(True):
        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)

        # the 'c' button is set as the quitting button
        if cv2.waitKey(1) & 0xFF == ord('c'):
            keepFrame = cv2.flip(frame, 1)
            cv2.imwrite(file_path, keepFrame)
            break

        frame = cv2.putText(frame, "Press 'C' to capture", (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

    vid.release()
    cv2.destroyAllWindows()
