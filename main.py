# based on 
# https://www.tutorialspoint.com/detection-of-a-specific-color-blue-here-using-opencv-with-python
# https://www.life2coding.com/how-to-create-a-rgb-color-picker-for-images-using-opencv-python/

import argparse
import cv2 
import imutils
import numpy as np

def set_highlighted_image_color(event, x, y, flags, param):
	global highlighted_image
	if event == cv2.EVENT_LBUTTONDOWN:
		# get clicked colour and define range
		color = img[y, x]
		print("RGB Value at ({},{}):{} ".format(x,y,color))
		lower_range = np.array(color) - np.array(extra)
		upper_range = np.array(color) + np.array(extra)
		
		# compute mask and colour it
		mask = cv2.inRange(img, lower_range, upper_range)
		mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
		highlight = np.zeros_like(mask)
		highlight[:] = (255, 0, 255)
		highlight = cv2.bitwise_and(highlight, mask)

		# highlight original image and show
		highlighted_image = cv2.bitwise_or(highlight, img)

# parse arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--image', '-i', help='the image to highlight colour in')
args = vars(parser.parse_args())

# read image
img = cv2.imread(args['image'])
highlighted_image = img

# tolerance for colour detection 
extra = [20, 20, 20]

# create window and watch our for mouse clicks
cv2.namedWindow('image')
cv2.setMouseCallback('image', set_highlighted_image_color)

# run until user hits Esc 
while(True):
	# show images
	cv2.imshow('image', highlighted_image)
	if cv2.waitKey(10) & 0xFF == 27:
		break
cv2.destroyAllWindows()
