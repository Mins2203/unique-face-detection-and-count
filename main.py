import cv2
from ultralytics import YOLO
from tracker import Tracker

model = YOLO("yolov8n.pt")
tracker = Tracker()

cap = cv2.VideoCapture("Video.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    "final_output.mp4",  
    fourcc,
    30,
    (1020, 500)
)

ids = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1020, 500))

    results = model(frame, verbose=False)
    detections = []

    for r in results:
        for box in r.boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = box
            if int(cls) == 0 and conf > 0.5:   
                
                area = (x2 - x1) * (y2 - y1)
                if area > 2000: 
                    detections.append([int(x1), int(y1), int(x2), int(y2)])

    boxes_ids = tracker.update(detections)

    for box_id in boxes_ids:
        x1, y1, x2, y2, id = box_id
        ids.add(id)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame, f'ID {id}',
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f'Total Persons: {len(ids)}',
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        3
    )

    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()

print("Output video saved as final_output.mp4")