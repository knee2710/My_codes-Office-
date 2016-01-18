import cv2
import os
import json

# class for selecting a rectangular portion of the image on mouse click
def crop(event, x, y, flags, param):
	global crop_pts, local_roi

	if event == cv2.EVENT_LBUTTONDOWN:
		crop_pts = [(x, y)]

	elif event == cv2.EVENT_LBUTTONUP:
		crop_pts.append((x,y))
		# selects a recatngular portion on mouse click
		cv2.rectangle(img, crop_pts[0], crop_pts[1], (0, 255, 0), 2)
		cv2.imshow('image', img)

		# local_roi = {"1":{"x1":crop_pts[0][0],"y1":crop_pts[0][1], "x2":crop_pts[1][0], "y2":crop_pts[1][1]}} --
		# print local_roi
		#generating json
		# roi_json["rois"].update(local_roi) --
		# del roi_json["rois"]["0"]
		# print roi_json --
		# print crop_pts


def handler(img, flag):

	cv2.namedWindow("image")
	cv2.setMouseCallback('image', crop)

	while(1):
		cv2.imshow('image', img)
		
		key = cv2.waitKey(0) & 0xFF

		if key == 27:			
			break

		if key == ord('s'):
			local_roi = {flag:{"x1":crop_pts[0][0],"y1":crop_pts[0][1], "x2":crop_pts[1][0], "y2":crop_pts[1][1]}}
			roi_json["rois"].update(local_roi)
			print roi_json
			clone = img.copy()
			roi = clone[crop_pts[0][1]:crop_pts[1][1],crop_pts[0][0]:crop_pts[1][0]]
			image_path = "cropped_images/test_crop_"+flag+".jpg"
			cv2.imwrite(image_path,roi)
			cv2.imshow('ROI', roi)
			cv2.waitKey(0)
			print "saved"


		


# main code
img = cv2.imread('card.png', 1)
cv2.namedWindow('image')

os.makedirs("cropped_images")

roi_json = {"rois":{"0":{"x1":460, "y1":75, "x2":715, "y2":320}}}

output = open('cordinates.json', 'w')

# cv2.setMouseCallback('image', crop)

while(1):
	cv2.imshow('image', img)
	key = cv2.waitKey(0) & 0xFF

	if key == ord('q'):
		print"q is pressed"
		handler(img,"1")

	elif key == ord('w'):
		print"w is pressed"
		handler(img,"2")

	elif key == ord('e'):
		print"e is pressed"
		handler(img,"3")

	elif key == ord('r'):
		print"r is pressed"
		handler(img,"4")

	elif key == ord('t'):
		print"e is pressed"
		handler(img,"5")

	elif key == ord('y'):
		print"y is pressed"
		handler(img,"6")

	elif key == ord('s'):
		del roi_json["rois"]["0"]
		output_json = json.dumps(roi_json)
		output.write(output_json)
		break

cv2.destroyAllWindows()