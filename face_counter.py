import cv2
import face_recognition
import numpy as np

video_path = "Video.mp4"
cap = cv2.VideoCapture(video_path)

known_face_encodings = [] 
face_count = 0
frame_no = 0

while True:
    ret, frame = cap.read()
    if frame_no % 5 != 0:
        continue  

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(
        rgb_frame, face_locations
    )

    for face_encoding, (top, right, bottom, left) in zip(
        face_encodings, face_locations
    ):
        matches = face_recognition.compare_faces(
            known_face_encodings,
            face_encoding,
            tolerance=0.6
        )

        if True not in matches:
            known_face_encodings.append(face_encoding)
            face_count += 1

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f'Unique Faces: {face_count}',
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        3
    )

cap.release()
cv2.destroyAllWindows()

print("Total Unique Faces Detected:", face_count)
