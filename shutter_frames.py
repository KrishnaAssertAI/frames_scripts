#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:48:53 2022

@author: dragon
"""


"""
sudo nano shutter_frames.py
"""

import cv2
import os
rtsp = 'rtsp://admin:assert%40123@192.168.1.2:554/h265/main/ch1/main/av_stream'
camera = 'shutter'
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
    file_name = f'/home/nvidia/frames_scripts/frames/{camera}_{i}.jpg'
    if i%(fps*60*2)==0:
        cv2.imwrite(file_name, frame)
        print(f"file saved {file_name}")
    i+=1

cap.release()


