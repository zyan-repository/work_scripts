# *coding:utf-8 *
import os
import cv2
import numpy as np
import matplotlib as plt
from IPython import embed

img_dir = 'D:/data/new_img/coco_dataset/train/'
save_dir = 'D:/data/new_img/train_tran_color/'

# 调试信息
# 黑边图 BYZ_SH_NK_1641266111923_270.jpg
# 花边图 BYZ_SH_NK_1636709651946_270.png
# frame = cv2.imread(img_dir + 'BYZ_SH_NK_1641265876998_180.jpg')
# frame = cv2.imread(img_dir + 'BYZ_SH_NK_1636709651946_270.png')

for img_name in os.listdir(img_dir):
    frame = cv2.imread(img_dir + img_name)
    # 前10行全为黑色认为是黑色填充图
    if frame[:10, :, :].sum() == 0:
        mask = (frame[:, :, 0] < 20) & \
               (frame[:, :, 1] < 20) & \
               (frame[:, :, 2] < 20)
        mask = np.where(mask == False, 0, 255).astype(np.uint8)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        mask = cv2.morphologyEx(
            mask.astype(np.uint8),
            cv2.MORPH_OPEN,
            kernel,
            iterations=6
        )

        border_mask = np.empty([1080, 1080, 3], dtype=np.uint8)
        border_mask[:, :, :] = 255
        for i in range(3):
            border_mask[:, :, i] = mask

        # mask方法,替换黑色区域
        random_mask = np.ones_like(frame)
        for i in range(3):
            random_mask[:, :, i] = np.random.randint(255)
        random_mask = cv2.bitwise_and(border_mask, random_mask)
        frame += random_mask

        cv2.imwrite(save_dir + img_name, frame)
    else:
        pass
        cv2.imwrite(save_dir + img_name, frame)
