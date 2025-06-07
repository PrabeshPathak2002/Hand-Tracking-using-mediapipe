import cv2
import mediapipe as mp
import time

class HandTracking:
    def __init__(self, camera_index=0, mode=False, max_num_hands=1, min_detection_confidence=0.3, min_tracking_confidence=0.3):
        self.mode = mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.cap = cv2.VideoCapture(camera_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)   
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_num_hands,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.pTime = 0
        self.results = None

    def process_frame(self):
        success, img = self.cap.read()
        if not success:
            return None

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1 / (cTime - self.pTime) if (cTime - self.pTime) != 0 else 0
        self.pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        return img

    def findPosition(self, img, handNo=0, draw=True, landmark_ids=None):
        """
        Returns a list of (id, x, y) for specified landmark_ids.
        If landmark_ids is None, returns all landmarks.
        """
        lmList = []
        if self.results and self.results.multi_hand_landmarks:
            if handNo < len(self.results.multi_hand_landmarks):
                myHand = self.results.multi_hand_landmarks[handNo]
                h, w, c = img.shape
                for id, lm in enumerate(myHand.landmark):
                    if (landmark_ids is None) or (id in landmark_ids):
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append((id, cx, cy))
                        if draw:
                            cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return lmList

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()


def main():
    hand_tracker = HandTracking(camera_index=0, max_num_hands=2)
    try:
        while True:
            img = hand_tracker.process_frame()
            if img is None:
                break

            lmList = hand_tracker.findPosition(img, handNo=0, draw=True, landmark_ids=[4, 8])
            if lmList:
                # Use lmList[0][1], lmList[0][2] as the x, y position for your snake
                print("Index finger tip position:", lmList[0][1], lmList[0][2])

            cv2.imshow("Image", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        hand_tracker.release()


if __name__ == "__main__":
    main()