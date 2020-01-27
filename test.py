import cv2
import os
import adb
import time

adbkit = adb.adbKit()
while True:
    image_name_list = ['images/btn_close_full1.png','images/btn_close_full2.png','images/btn_close_full3.png']
    for image in image_name_list:
        adbkit.screenshots()
        target_img = cv2.imread("screencap.png")
        find_img = cv2.imread(image)
        find_height, find_width, find_channel = find_img.shape[::]
        result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)
        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
        if max_val>0.9:
            print('match success!')
            pointUpLeft   = max_loc
            pointLowRight = (max_loc[0]+find_width, max_loc[1]+find_height)
            pointCentre   = (max_loc[0]+(find_width/2), max_loc[1]+(find_height/2))
            adbkit.click(pointCentre)
            time.sleep(1)
        os.remove("screencap.png")
    time.sleep(5)
