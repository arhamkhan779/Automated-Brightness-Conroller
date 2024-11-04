import cv2
import numpy as np
import time
import mediapipe as mp

class HandDetector:
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_con,
            min_tracking_confidence=self.track_con
        )
        self.mpDraw = mp.solutions.drawing_utils

    def enhance(self, image):
        if image is not None:
            return cv2.detailEnhance(image, sigma_s=10, sigma_r=0.111)
        return image

    def find_hands(self, frame,draw=True):
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_rgb = self.enhance(img_rgb)
        self.results = self.hands.process(img_rgb)
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                  self.mpDraw.draw_landmarks(frame, hand_landmarks, self.mpHands.HAND_CONNECTIONS)
        return frame
    
    def FindPosition(self,frame,handNO=0,draw=True):
        lmList=[]
        if self.results.multi_hand_landmarks:
          my_hand=self.results.multi_hand_landmarks[handNO]
          for handlms in self.results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
               h,w,c=frame.shape
               cx,cy=int(lm.x*w), int(lm.y*h)
               lmList.append([id,cx,cy])
               if draw:
                 cv2.circle(frame,(cx,cy),7,(255,0,255),cv2.FILLED)
        return lmList

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0

    if not cap.isOpened():
        print(f"Error: Unable to open video file")
        exit()

    detector = HandDetector()  # Move this outside the loop

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video or error occurred.")
            break

        frame = detector.find_hands(frame)
        lmlist=detector.FindPosition(frame)

        if len(lmlist) !=0:
            print(lmlist[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
        pTime = cTime
        cv2.putText(frame, str(int(fps)), (18, 78), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow('Video Playback', frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
