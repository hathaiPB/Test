from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2
import matplotlib.pyplot as plt

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

image = cv2.imread("D:\\Work2021\\test\\image_data\\85_1026.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

frame = cv2.resize(edged,(0,0),fx=0.3, fy=0.3)
# cv2.imshow("Measuring_Size_Image", frame)
# cv2.waitKey(0)
plt.imshow(frame)
plt.show()


cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

(cnts, _) = contours.sort_contours(cnts)
pixelsPerMetric = None

# for c in cnts:
# 	if cv2.contourArea(c) < 100:
# 		continue

# 	orig = image.copy()
# 	box = cv2.minAreaRect(c)
# 	box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
# 	box = np.array(box, dtype="int")

# 	box = perspective.order_points(box)
# 	cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 64), 2)

# 	for (x, y) in box:
# 		cv2.circle(orig, (int(x), int(y)), 5, (0, 255, 64), -1)

# 	(tl, tr, br, bl) = box
# 	(tltrX, tltrY) = midpoint(tl, tr)
# 	(blbrX, blbrY) = midpoint(bl, br)

# 	(tlblX, tlblY) = midpoint(tl, bl)
# 	(trbrX, trbrY) = midpoint(tr, br)

# 	cv2.circle(orig, (int(tltrX), int(tltrY)), 0, (0, 255, 64), 0)
# 	cv2.circle(orig, (int(blbrX), int(blbrY)), 0, (0, 255, 64), 0)
# 	cv2.circle(orig, (int(tlblX), int(tlblY)), 0, (0, 255, 64), 0)
# 	cv2.circle(orig, (int(trbrX), int(trbrY)), 0, (0, 255, 64), 0)

# 	cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
# 		(255, 255, 255), 1)
# 	cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
# 		(255, 255, 255), 1)

# 	dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
# 	dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

# 	if pixelsPerMetric is None:
# 		pixelsPerMetric = dB / 1.02362205

# 	dimA = dA / pixelsPerMetric
# 	dimB = dB / pixelsPerMetric

# 	cv2.putText(orig, "{:.2f}cm".format(dimA * 2.54),
# 		(int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
# 		0.65, (255, 255, 255), 2)
# 	cv2.putText(orig, "{:.2f}cm".format(dimB * 2.54),
# 		(int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
# 		0.65, (255, 255, 255), 2)


# 	# show output
# 	frame = cv2.resize(orig,(0,0),fx=0.2, fy=0.2)
# 	cv2.imshow("Measuring_Size_Image", frame)
# 	cv2.waitKey(0)

