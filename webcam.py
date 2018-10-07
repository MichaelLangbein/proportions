import cv2
import imutils
from facial_landmarks import LandmarkDetector 
import engine as e
import faceFrame as ff


video_capture = cv2.VideoCapture(0)
ld = LandmarkDetector()
face = ff.FaceFrame()


while True:
    ret, frame = video_capture.read()
    frame = imutils.resize(frame, width=500)

    facesLandmarks = ld.analyseImage(frame)
    for faceLandmarks in facesLandmarks:
        face.align(faceLandmarks)
        e.draw(face, frame)


    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()