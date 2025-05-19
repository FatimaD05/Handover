import cv2
from HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7, maxHands=2)

gestureText = ""

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)

        # 📏 Pinch (index + pouce) = Scale
        length, info, _ = detector.findDistance(lmList[4][0:2], lmList[8][0:2])
        scale = round(np.interp(length, [30, 200], [0.5, 2.0]), 2)

        if 0.5 <= scale <= 2:
            with open("scale.txt", "w") as f:
                f.write(str(scale))
            gestureText = f"Scaling: {scale}"
        else:
            with open("scale.txt", "w") as f:
                f.write("NULL")

        # 🔁 Poing fermé = Rotation
        if fingers == [0, 0, 0, 0, 0]:
            with open("rotate.txt", "w") as f:
                f.write("5")
            gestureText = "Rotating"
        else:
            with open("rotate.txt", "w") as f:
                f.write("")

        # ➡️ Index seul levé = Pan (déplacement)
        if fingers == [0, 1, 0, 0, 0]:
            cx, cy = lmList[8][0], lmList[8][1]
            x = round(np.interp(cx, [100, 540], [-1, 1]), 2)
            z = round(np.interp(cy, [100, 380], [-1, 1]), 2)
            with open("pan.txt", "w") as f:
                f.write(f"{x} {z}")
            gestureText = f"Pan to x:{x} z:{z}"
        else:
            with open("pan.txt", "w") as f:
                f.write("NULL")

    else:
        with open("scale.txt", "w") as f:
            f.write("NULL")
        with open("rotate.txt", "w") as f:
            f.write("")
        with open("pan.txt", "w") as f:
            f.write("NULL")
        gestureText = "No hand detected"

    # 🟪 Affiche le texte du geste
    img = cv2.flip(img, 1)
    cv2.putText(img, gestureText, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
