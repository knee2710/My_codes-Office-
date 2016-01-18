# ==============================================================================#
#-- Project Name: Caesars : Game start
#-- Task : To recognise the game start and end using background substraction (only works if there is a time difference of 2s or more between two games) 
#-- Version : 1.0
#-- Date : 2016:01:15
#-- Modified : 2016:01:18
#-- Author : Neeraj Komuravalli
# ==============================================================================#

#-------------------
# Package imports
#-------------------
import cv2
import json
import numpy as np

#-------------------
# Takes inputs from user
#-------------------
# video_name = raw_input("Please enter video name: ")
cap = cv2.VideoCapture('chip_june1_table2.mp4')

# json_file = raw_input("Please enter the json file name: ")
roi = json.load(open('chip_june1_table2.json'))


#-------------------
# Declarations
#-------------------
global txt 
txt = "Game not started"
player_data = []
card_detection_vector = []
frame_count = 0
key = 0
waiting = 1

# Background image reading
# background_image = raw_input("Please enter background image name: ")
bck_grnd = cv2.imread('background_june1_table2.png')
bck_grnd_gray = cv2.cvtColor(bck_grnd, cv2.COLOR_BGR2GRAY)

# Function to handle all video related operations using cv2 package
def video_handler(txt):
	global frame_count, key, waiting
	ret, frame = cap.read()
	frame_count = frame_count + 1
	card_presence = []
	card_presence_area = []
	# Code to detect if the card is present in each ROI and give output accordingly
	for i in xrange(1, 6):
		roi_img = frame[roi['rois'][str(i)]['y1']:roi['rois'][str(i)]['y2'],roi['rois'][str(i)]['x1']:roi['rois'][str(i)]['x2']]
		roi_img_gray = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)
		bck_grnd_roi = bck_grnd_gray[roi['rois'][str(i)]['y1']:roi['rois'][str(i)]['y2'],roi['rois'][str(i)]['x1']:roi['rois'][str(i)]['x2']]

		diff_img = cv2.subtract(roi_img_gray, bck_grnd_roi)

		ret, mask_card = cv2.threshold(diff_img, 190, 255, cv2.THRESH_BINARY)
		contours, hierarchy = cv2.findContours(mask_card,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)		

		f = 1
		area_card = 2000
		if i == 5:
			area_card = 1000

		try :
			areas = [cv2.contourArea(c) for c in contours]
			max_index = np.argmax(areas)
			cnt=contours[max_index]
			
			if cv2.contourArea(cnt) >= area_card:
				card_presence.append(1)

			else:
				card_presence.append(0)
			
			card_presence_area.append(cv2.contourArea(cnt))

		except ValueError:
			card_presence.append(0)
			card_presence_area.append(0)
		

	cv2.putText(frame,str(frame_count) + " Players: " + str(sum(card_presence)) + " " + txt,(35,85),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)
	# cv2.putText(frame,str(frame_count) + " " + str(card_presence_area[4]) + " " + txt,(35,85),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)
	# cv2.putText(frame, str(frame_count) + str(card_presence_area) + "\n" + txt, (35,85), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
	cv2.imshow('Video', frame)
	key = cv2.waitKey(waiting) & 0xFF
	waiting = 1
	return card_presence
	


# Main code to check for the conditions in order to decide if the game has started or ended
while(cap.isOpened()):

	card_presence = video_handler(txt)

	if key == 27:
		break

	elif sum(card_presence) >= 2 and (txt == "Game not started" or txt == "Game Ended"):
		refrance_frame_number = frame_count
		refrance_card_pattern = card_presence
		count_same_pattern = 0
		while (frame_count <= (refrance_frame_number + 20)):
			card_presence = video_handler(txt)
			if sum(card_presence) >= 2:
				count_same_pattern = count_same_pattern + 1
		if count_same_pattern >= 17:
			txt = "Game Started"
			print "Game Started : " + str(frame_count)
			waiting = 0

	elif txt == "Game Started" and sum(card_presence) == 0:
		refrance_frame_number = frame_count
		count_same_pattern = 0
		while (frame_count <= (refrance_frame_number + 20)):
			card_presence = video_handler(txt)
			if sum(card_presence) == 0:
				count_same_pattern = count_same_pattern + 1
		if count_same_pattern >= 17:
			txt = "Game Ended"
			print "Game Ended : " + str(frame_count)
			waiting = 0
