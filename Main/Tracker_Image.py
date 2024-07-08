from collections import defaultdict

import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors


def tracker_img(frame):
    
    #Dictionary to store tracking history with default empty lists
    track_history = defaultdict(lambda: [])

    #Load the YOLO model with segmentation capabilities
    model = YOLO("yolov8n-seg.pt")
    
        # Create an annotator object to draw on the frame
    annotator = Annotator(frame, line_width=1)

    # Perform object tracking on the current frame
    results = model.track(frame, persist=True,classes = 0)

    # Check if tracking IDs and masks are present in the results
    if results[0].boxes.id is not None and results[0].masks is not None:
        # Extract masks and tracking IDs
        masks = results[0].masks.xy
        track_ids = results[0].boxes.id.int().tolist()

        # Annotate each mask with its corresponding tracking ID and color
        for mask, track_id in zip(masks, track_ids):
            annotator.seg_bbox(mask=mask, mask_color=colors(track_id, True), track_label=str(track_id))
        Q = str(len(track_ids))
    else:
        Q = "0"
      
    return frame,Q