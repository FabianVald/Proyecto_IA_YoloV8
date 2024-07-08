import cv2
import Tracker_Image as TI

def find_available_cameras():
    index = 0
    available_cameras = []
    while index < 10:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if cap.read()[0]:
            available_cameras.append(index)
            cap.release()
        else:
            cap.release()  # Release capture if not successful
        index += 1
    return available_cameras

def Capturer():
    available_cameras = find_available_cameras()
    if available_cameras:
        cap = cv2.VideoCapture(available_cameras[0], cv2.CAP_DSHOW)
        while True:
            ret, frame = cap.read()
            if ret:
                frame,Q = TI.tracker_img(frame)
                # Display the annotated frame
                text = "Cantidad de personas: "+Q
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 0.7
                color = (255, 255, 255)  # Color en formato BGR (en este caso, azul)
                thickness = 2
                cv2.putText(frame, text, (25, 25), font, font_scale, color, thickness)
                cv2.imshow('Video', frame)
            else:
                print("Error: Unable to read frame")
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for 'q' key to exit
                break

        cap.release()  # Release video capture
        cv2.destroyAllWindows()  # Close all OpenCV windows
    else:
        print("No cameras available.")