import cv2
from flask import Flask, render_template, Response,request
import dlib
import numpy as np
from yolo_helper import count


def gen_frames(cam,s):  
    while True:
   
        success, frame = cam.read() 
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            count(frame)
            frame = buffer.tobytes()
              
            if s == True:
                print("a")
                # cam.release()
                # break
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def stop_cam(cam):  
    cam.release()