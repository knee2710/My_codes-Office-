# ==============================================================================#
#-- Project Name: Caesars : ROI Selector
#-- Task : To ask user to select ROI and give cordinates in JSON format as output 
#-- Version : 1.0
#-- Date : 2016:01:8
#-- Author : Neeraj Komuravalli
# ==============================================================================#

#-------------------
# Package imports
#-------------------
import cv2
import os
import json
import shutil

#-------------------------------------------
# Class for selecting a rectangular portion of the image on mouse drag.
#-------------------------------------------
def crop(event, x, y, flags, param):
	global crop_pts, local_roi

	if event == cv2.EVENT_LBUTTONDOWN:
		crop_pts = [(x, y)]

	elif event == cv2.EVENT_LBUTTONUP:
		crop_pts.append((x,y))

		# selects a recatngular portion on mouse click
		cv2.rectangle(img, crop_pts[0], crop_pts[1], (0, 0, 0), 1)
		cv2.imshow('image', img)

#-------------------------------------------
# Class for saving the selected image and storing the cordinates of the region.
#-------------------------------------------
def handler(img, flag):
	cv2.namedWindow("image")
	cv2.setMouseCallback('image', crop)

	while(1):
	
		cv2.imshow('image', img)
		
		key = cv2.waitKey(0) & 0xFF
		# To select ROI again in case of wrong selection
		if key == ord('r'):			
			print "To select the roi of the player " + flag + " again press : " + flag
			break

		# To save the cordinates and the cropped image to a folder
		elif key == ord('s'):
			local_roi = {flag:{"x1":crop_pts[0][0],"y1":crop_pts[0][1], "x2":crop_pts[1][0], "y2":crop_pts[1][1]}}
			roi_json["rois"].update(local_roi)
			print roi_json
			clone = img.copy()
			roi = clone[crop_pts[0][1]:crop_pts[1][1],crop_pts[0][0]:crop_pts[1][0]]
			image_path = "cropped_images/test_crop_"+flag+".jpg"
			cv2.imwrite(image_path,roi)
			print "saved"
			break



#-------------
# Main code.
#-------------
# img = cv2.imread('card.png', 1)
# cv2.namedWindow('image')

# To make a directory to put all the cropped images and in case the directry exists, delete the contents
if os.path.isdir("cropped_images"):
	shutil.rmtree("cropped_images")
os.makedirs("cropped_images")

# Creates a empty JSON to store the cordinaters
roi_json = {"rois":{}}

# Opens a file called cordinates.json to store json in it  
output = open('cordinates.json', 'w')

#  Asks the user the name of the video
video_name = raw_input("Please enter video name: ")
cap = cv2.VideoCapture(video_name)

f = 0
# Gives the instructions
print "Press c to move the frame\nPress f to fix the frame\nPress u to unfix the frame\nPress 1-6 to select respective player\nPress r in case you want to select ROI again\nPress esc key to exit"

while(cap.isOpened()):
	if f == 0:
		rep, img = cap.read()

	cv2.imshow('image', img)
	key = cv2.waitKey(0) & 0xFF

# To look throug the video
	if key == ord('c'):
		pass

# To fix a frame
	elif key == ord('f'):
		print "This frame is fixed"
		f = 1

# To unfix the selected frame
	elif key == ord('u'):
		print "Press c to move the frame"
		f = 0

# To select respective player
	elif key == ord('1'):
		print"Select ROI for player 1"
		previous_image = img
		handler(img,"1")

	elif key == ord('2'):
		print"Select ROI for player 2"
		handler(img,"2")

	elif key == ord('3'):
		print"Select ROI for player 3"
		handler(img,"3")

	elif key == ord('4'):
		print"Select ROI for player 4"
		handler(img,"4")

	elif key == ord('5'):
		print"Select ROI for player 5"
		handler(img,"5")

	elif key == ord('6'):
		print"Select ROI for player 6"
		handler(img,"6")

# To exit
	elif key == 27:
		output_json = json.dumps(roi_json)
		output.write(output_json)
		break

cv2.destroyAllWindows()