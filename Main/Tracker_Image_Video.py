from collections import defaultdict
import Resizer
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

def video_tracker(path):
    # Dictionary to store tracking history with default empty lists
    track_history = defaultdict(lambda: [])

    # Load the YOLO model with segmentation capabilities
    model = YOLO("yolov8n-seg.pt")

    # Open the video file
    cap = cv2.VideoCapture(path)

    # Retrieve video properties: width, height, and frames per second
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))


    while True:
        # Read a frame from the video
        ret, im0 = cap.read()
        im0 = Resizer.resize_image(im0)
        if not ret: 
            print("Video frame is empty or video processing has been successfully completed.")
            break

        # Create an annotator object to draw on the frame
        annotator = Annotator(im0, line_width=1)

        # Perform object tracking on the current frame
        results = model.track(im0, persist=True,classes = 0)

        # Check if tracking IDs and masks are present in the results
        if results[0].boxes.id is not None and results[0].masks is not None:
            #print(results[0])
            # Extract boxes, masks, confidences, and tracking IDs
            boxes = results[0].boxes
            masks = results[0].masks.xy
            #results[0].plot()
            confidences = results[0].boxes.conf
            track_ids = results[0].boxes.id.int().tolist()

            # Filter detections based on confidence threshold (e.g., 60%)
            indices = [i for i, conf in enumerate(confidences) if conf > 0.3]

            # Annotate each mask with its corresponding tracking ID and color
            for idx in indices:
                annotator.seg_bbox(mask=masks[idx], mask_color=colors(track_ids[idx], True), track_label=str(track_ids[idx]))
            Q = str(len(indices))
        else:
            Q = "0"
        
        # Display the annotated frame
        text = "Cantidad de personas: "+Q
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        color = (255, 255, 255)  # Color en formato BGR (en este caso, azul)
        thickness = 2
        cv2.putText(im0, text, (25, 25), font, font_scale, color, thickness)
        cv2.imshow('Video', im0)
        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video writer and capture objects, and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()