import json

import requests
from flask import Flask
import cognitive_face as CF
import pygame
import pygame.camera
from pygame.locals import *
from flask import send_file

app = Flask(__name__)

pygame.init()
pygame.camera.init()
person_group_id = 'man'


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/face/get_image')
def getImage():
    cam = pygame.camera.Camera("/dev/video0",(1280,720))
    cam.start()
    image = cam.get_image()
    cam.stop()
    pygame.image.save(image, "image1.jpg")
    return send_file("image1.jpg", mimetype='image/jpg')

if __name__ == '__main__':
    app.run(debug=True)