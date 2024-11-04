import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import wmi

# Initialize WMI
c = wmi.WMI(namespace='wmi')

def get_brightness():
    """Retrieve the current brightness level"""
    for instance in c.WmiMonitorBrightness():
        return instance.CurrentBrightness
    return None

def set_brightness(value):
    """Set the brightness level (requires admin rights)"""
    value = max(0, min(value, 100))  # Ensure brightness is between 0 and 100
    for instance in c.WmiMonitorBrightnessMethods():
        instance.WmiSetBrightness(value, 0)  # Second parameter is the timeout in seconds

# Initial brightness values
brightness = 0
brightness_bar = 400
brightness_per = 0

Wcam, Hcam = 808, 600
cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0
cap.set(3, Wcam)
cap.set(4, Hcam)

detector = htm.HandDetector(detection_con=0.7)

while True:
    success, frame = cap.read()
    frame = detector.find_hands(frame)
    lmlist = detector.FindPosition(frame, draw=False)

    if len(lmlist) != 0:
        X1, Y1 = lmlist[4][1], lmlist[4][2]
        X2, Y2 = lmlist[8][1], lmlist[8][2]

        CX, CY = (X1 + X2) // 2, (Y1 + Y2) // 2

        cv2.circle(frame, (X1, Y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(frame, (X2, Y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(frame, (X1, Y1), (X2, Y2), (255, 0, 255), 3)
        cv2.circle(frame, (CX, CY), 10, (255, 0, 255), cv2.FILLED)

        Length = math.hypot(X2 - X1, Y2 - Y1)
        brightness = np.interp(Length, [20, 221], [0, 100])
        brightness_bar = np.interp(Length, [20, 221], [400, 150])
        brightness_per = np.interp(Length, [20, 221], [0, 100])

        # Adjust system brightness
        set_brightness(int(brightness_per))

        if Length < 50:
            cv2.circle(frame, (CX, CY), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(frame, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(frame, (50, int(brightness_bar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime
    cv2.putText(frame, f"{str(int(brightness_per))}%", (18, 78), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow('Video Playback', frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
