#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： LiuYuZhao
# datetime： 2022/1/17 16:11

import pyvirtualcam
import numpy as np
from PIL import Image


if __name__ == '__main__':
    with pyvirtualcam.Camera(width=1280, height=1897, fps=20) as cam:

        im = np.array(Image.open('test.jpg'))

        print(f'Using virtual camera: {cam.device}')
        # frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB

        while True:
            # frame[:] = cam.frames_sent % 255  # grayscale animation
            cam.send(im)
            cam.sleep_until_next_frame()