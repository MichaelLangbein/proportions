from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2



class LandmarkDetector:

	def __init__(self):
		# initialize dlib's face detector (HOG-based) and then 
		self.detector = dlib.get_frontal_face_detector()
		# create the facial landmark predictor
		self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

	def analyseImage(self, image):
		facesLandmarks = []

		# resize and turn to grayscale
		image = imutils.resize(image, width=500)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# detect faces in the grayscale image
		rects = self.detector(gray, 1)
		for (i, rect) in enumerate(rects):
			# determine the facial landmarks for the face region, then convert the facial landmark (x, y)-coordinates to a NumPy array
			landmarks = self.predictor(gray, rect)
			landmarksNP = face_utils.shape_to_np(landmarks)
			
			facesLandmarks.append(landmarksNP)

		return facesLandmarks


