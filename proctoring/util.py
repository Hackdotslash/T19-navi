import cv2

import dlib
import numpy as np
import threading
from yolo_helper import count


def gen_frames(cam):  
    while True:
   
        success, frame = cam.read() 
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            count(frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

