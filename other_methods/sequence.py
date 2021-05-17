"""
Demonstration of the GazeTracking library.
"""


import cv2

import sys
### Add Path For Testing This File Only
sys.path.append("C:\\Users\\Paoyimpae\\Desktop\\FaceEyePassword\\")

from gaze_tracking.gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
now = "M"
before = "M"
sequence = []
check = []
mcount = 0
lcount = 0
rcount = 0

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking() and len(check) >= 20:
        text = "Blinking"
        for i in range(len(check), (len(check)-15)):
            if i == "M":
                mcount += 1
            if i == "L":
                lcount += 1
            if i == "R":
                rcount += 1
        if rcount > mcount and rcount > lcount:
            sequence.append("R")
            check.clear()
        if mcount > rcount and mcount > lcount:
            sequence.append("M")
            check.clear()
        if lcount > mcount and lcount > rcount:
            sequence.append("l")
            check.clear()
    elif gaze.is_right():
        text = "Looking right"
        now = "R"
    elif gaze.is_left():
        text = "Looking left"
        now = "L"
    elif gaze.is_center():
        text = "Looking center"
        now = "M"
    check.append(now)

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)
    print(sequence)
    if cv2.waitKey(1) == 27:
        break
