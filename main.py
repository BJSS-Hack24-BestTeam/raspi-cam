# import the necessary packages
import time
import cognitive_face as CF
import json
import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
person_group_id = 'man'
cam = pygame.camera.Camera("/dev/video0",(1280,720))
cam.start()
print(pygame.camera.list_cameras())
image = cam.get_image()
pygame.image.save(image, "image1.jpg")

KEY = '030d5c89e600472bba1d148dddcff568'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)


r = CF.face.detect('image1.jpg')
faceid = r[0]['faceId']
print(faceid)

result = CF.face.identify([faceid], person_group_id)
print(result)

