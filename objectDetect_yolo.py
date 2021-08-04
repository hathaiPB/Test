import matplotlib.pyplot as plt
import cvlib as _cvlib
import cv2
 
from cvlib.object_detection import draw_bbox
image = cv2.imread('D:\\Work2021\\test\sample-out.jpg')
recbox, label, configuration = _cvlib.detect_common_objects(image)
output_image = draw_bbox(image, recbox, label, configuration)
plt.imshow(output_image)
plt.show()