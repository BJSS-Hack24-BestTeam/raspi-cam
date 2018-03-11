import json

import requests
from flask import Flask
import cognitive_face as CF
import pygame
import pygame.camera
from pygame.locals import *
from flask import send_file, request, Response
#import picamera

app = Flask(__name__)

pygame.init()
pygame.camera.init()
person_group_id = 'man'

#def getpic(filename):
#    with picamera.PiCamera() as camera:
#        camera.resolution = (1024, 768)
#        camera.framerate = 30
#        time.sleep(1)
#        camera.capture_sequence([
#            filename,
#             ]) 

def getpic(filename):
    cam = pygame.camera.Camera("/dev/video0",(1280,720))
    cam.start()
    image = cam.get_image()
    cam.stop()
    pygame.image.save(image, filename)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/display/get_image')
def getImage():
    getpic("image1.jpg")
    return send_file("image1.jpg", mimetype='image/jpg')

@app.route('/display/check_face')
def checkFace():
    getpic("image2.jpg")

    url = 'http://51.143.186.87:5000/identify'
    payload = {'file': open('image2.jpg', 'rb')}
    r = requests.post(url, files=payload)
    if r.status_code == 200:
        return r.text
    else:
        return Response(status=404)



if __name__ == '__main__':
    app.run(debug=True)