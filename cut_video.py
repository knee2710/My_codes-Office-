import cv2
import numpy as np
import sys

if len(sys.argv) == 2:
	pass
elif len(sys.argv) >= 2:
	print "Enter only one video name"
else:
	print "Enter the video name"

fourcc = cv2.cv.CV_FOURCC(*'XVID')
#can change the name of output file here
output_video = cv2.VideoWriter("output.avi", fourcc, 10.0, (1280,720))

read_video = cv2.VideoCapture(sys.argv[1])
 
f = 0

while(read_video.isOpened()):

	ret , frame = read_video.read()

	cv2.imshow("Video", frame)
	key = cv2.waitKey(0) & 0xFF

	if key == ord('c'):
		pass

	elif key == ord('s'):
		print "start cutting the vedio from this frame"
		f = 1

	elif key == ord('e'):
		print "Vedio will be cut till this frame"
		f = 2

	else:
		break

	if f == 1:
		output_video.write(frame)
	elif f == 2:
		read_video.release()

output_video.release()
cv2.destroyAllWindows()