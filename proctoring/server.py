from flask import Flask, render_template, Response,request
from util import gen_frames
import cv2

app = Flask(__name__)
cam = cv2.VideoCapture(0)
@app.route('/')

def hello():
    return render_template("webcam.html")

@app.route("/video_feed",methods = ['GET'])
def video_feed():
    
    s =request.args.get('content')
    
    print(type(s))
    
    return Response(gen_frames(cam,s),
        mimetype = "multipart/x-mixed-replace; boundary=frame")
@app.route("/stop",methods = ['GET'])
def printout():
    content=''
    content +=request.args.get('content')
    with open("Output.txt", "w") as text_file:
        text_file.write(content)
    print(type(content))
    return ('', 204)
app.run(debug=True)