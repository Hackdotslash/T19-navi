from flask import Flask, render_template, Response
from util import gen_frames
import cv2

app = Flask(__name__)
cam = cv2.VideoCapture(0)
@app.route('/')
def hello():
    return render_template("webcam.html")

@app.route("/video_feed")
def video_feed():

	return Response(gen_frames(cam),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

app.run(debug=True)