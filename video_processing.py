import cv2
import os

cascase_path = '/Users/farooqueazam/Documents/farooque-anugrah-ds/haarcascade_fullbody.xml'
classifier = cv2.CascadeClassifier(cascase_path)

path = r'/Users/farooqueazam/Downloads/pexels_videos_2758322.mp4'  # 0 for webcam, path to video file
video = cv2.VideoCapture(path)

while True:
    status, image = video.read()
    if not status:
        print('Could not read frame')
        break
    
    # Resize the image for faster processing
    image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)
    
    # Detect people in the image
    detection = classifier.detectMultiScale(image,
                                            scaleFactor=1,
                                            minNeighbors=3,
                                            minSize=(20, 20))
    
    # Draw rectangles around detected bodies
    if len(detection) > 0:
        print(f'Found {len(detection)} people')
        for (x, y, w, h) in detection:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('video', image)
    
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture object and close all windows
video.release()
cv2.destroyAllWindows()
