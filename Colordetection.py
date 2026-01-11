import cv2
import numpy as np

# ===============================
# INISIALISASI KAMERA
# ===============================
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# ===============================
# RANGE WARNA (HSV)
# ===============================
color_ranges = {
    "RED": [
        (np.array([0, 120, 70]), np.array([10, 255, 255])),
        (np.array([170, 120, 70]), np.array([180, 255, 255]))
    ],
    "GREEN": [
        (np.array([36, 100, 100]), np.array([86, 255, 255]))
    ],
    "BLUE": [
        (np.array([94, 80, 2]), np.array([126, 255, 255]))
    ],
    "YELLOW": [
        (np.array([15, 100, 100]), np.array([35, 255, 255]))
    ]
}

# Warna bounding box (BGR)
box_colors = {
    "RED": (0, 0, 255),
    "GREEN": (0, 255, 0),
    "BLUE": (255, 0, 0),
    "YELLOW": (0, 255, 255)
}

# ===============================
# LOOP UTAMA
# ===============================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    for color_name, ranges in color_ranges.items():
        mask = None

        for lower, upper in ranges:
            temp_mask = cv2.inRange(hsv, lower, upper)
            mask = temp_mask if mask is None else mask + temp_mask

        # Noise removal
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 800:
                continue

            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(frame, (x, y), (x + w, y + h), box_colors[color_name], 2)
            cv2.putText(
                frame,
                f"{color_name}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                box_colors[color_name],
                2,
                cv2.LINE_AA
            )

    cv2.imshow("🎨 Color Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ===============================
# CLEANUP
# ===============================
cap.release()
cv2.destroyAllWindows()
