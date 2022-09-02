import cv2
import imutils
import numpy as np
import os

def drawLines(image, arr):
    """
    Draws lines on image with OpenCV2. To draw shape, ensure the last coord of the array is equals to the first one.
    :param image: image
    :param arr: array of points in format of [[x1, y1], [x2, y2], ...]
    :return: None
    """
    prev = [arr[0][0], arr[0][1]]
    for i in arr:
        cv2.line(image, (prev[0], prev[1]), (i[0], i[1]), (255, 0, 0), 5)
        prev = [i[0], i[1]]

def drawPoints(image, arr):
    """
    Draws points on image with OpenCV2
    :param image: image
    :param arr: array of points in format of [[x1, y1], [x2, y2], ...]
    :return: None
    """
    for i in arr:
        cv2.line(image, (i[0], i[1]), (i[0], i[1]), (0, 0, 255), 5)

def showCompare(im1_path, im2_path, compared):

    if not compared:
        compared = " doesn't"
    else:
        compared = ""
    im1, im2 = cv2.imread(im1_path), cv2.imread(im2_path)
    image = np.concatenate((im1, im2), axis=0)
    image = cv2.putText(image, "These two images%s contain the same person"%compared, (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
    image = imutils.resize(image, width=500)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showPointImage(file_path, arr):
    image = cv2.imread(file_path)
    drawPoints(image, arr)
    image = imutils.resize(image, width=500)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showLineImage(file_path, arr):
    image = cv2.imread(file_path)
    for i in arr:
        drawLines(image, i)
    image = imutils.resize(image, width=500)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showPoseImage(file_path, arr, result_arr):
    image = cv2.imread(file_path)

    for i in arr:
        drawLines(image, i)

    i = 0
    for result in result_arr:
        if result == 0:
            resultString = "still"
        elif result == 1:
            resultString = "rubbing shoulders"
        else:
            resultString = "stretching"

        text_size, _ = cv2.getTextSize("This pose is %s."%resultString, cv2.FONT_HERSHEY_DUPLEX, 1, 2)
        text_w, text_h = text_size

        # Since this is spaghetti, below will explain structure (Above code puts references on the bounds of the text):

        # cv2.rectangle(image, starting_position, ending_position, BGR_color, thickness)
        # - starting position is placed 10 to the left of the left bound and 10 on top of the top bound
        #   where arr[i] is the arr of coord points, arr[i][3] is the bottom left coord and
        #   arr[i][3][0] and arr[i][3][0] being the 2 points of bottom left coord

        # Rest should be self-explanatory. If not, here's slightly more info:
        # text_w is width of the text defined by code above, text_h is same but the height
        # use this to understand cv2.putText "https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/"

        image = cv2.rectangle(image, (arr[i][3][0]-10, arr[i][3][1]+10), (arr[i][3][0]+10+text_w, arr[i][3][1]+30+text_h), (250, 50, 50), -1)
        image = cv2.putText(image, "This pose is %s."%resultString, (arr[i][3][0], arr[i][3][1]+20 + text_h), cv2.FONT_HERSHEY_DUPLEX, 1, (250,250,250), 2, cv2.LINE_4)
        i = i + 1

    image = imutils.resize(image, width=500)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def camCapture(file_path):
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)
        # The "c" key is used to advance the process. Can be changed as long as you know the keycode.
        if cv2.waitKey(1) & 0xFF == ord('c'):
            keepFrame = frame
            cv2.imwrite(file_path, keepFrame)
            break
        frame = cv2.putText(frame, "Press 'C' to capture", (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
        frame = imutils.resize(frame, width=500)
        cv2.imshow('frame', frame)
    vid.release()
    cv2.destroyAllWindows()
