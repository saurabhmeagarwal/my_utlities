import cv2
import numpy as np
import os
import sys

for file in sys.argv[1:]:
    image= cv2.imread(file)
    cv2.imshow('Image',image)
    k = cv2.waitKey(0) & 0xFF
    if k == ord('m'):
        path = os.path.join('/home/saurabh/fbImages/gender/male',
                os.path.basename(file)) 
        cv2.imwrite(path,image)
    if k == ord('f'):
        path = os.path.join('/home/saurabh/fbImages/gender/female',
                os.path.basename(file))
    if k == ord('d'):
        path = os.path.join('/home/saurabh/fbImages/reject_image',
                os.path.basename(file))
    


