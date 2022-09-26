#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:47:36 2022

@author: dragon
"""


"""
sudo nano intrusion_1_frames.py
"""

import cv2
import os
from datetime import datetime

rtsp = 'rtsp://admin:assert%40123@192.168.1.2:554/h265/main/ch4/main/av_stream'
camera = 'intrusion_1'
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
cap = cv2.VideoCapture(rtsp, cv2.CAP_FFMPEG)
fps = int(cap.get(cv2.CAP_PROP_FPS))
if 'frames' not in os.listdir('/home/nvidia/frames_scripts/'):
    os.mkdir('/home/nvidia/frames_scripts/frames/')

if not cap.isOpened():
    print('Cannot open RTSP stream')
i = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if i%(fps*60*2)==0:
        now = datetime.now()
        date_time = now.strftime("%m_%d_%Y__%H_%M_%S")
        file_name = f'/home/nvidia/frames_scripts/frames/{camera}_{date_time}.jpg'
        cv2.imwrite(file_name, frame)
        print(f"file saved {file_name}")
    i+=1

cap.release()

