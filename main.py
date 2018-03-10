# import the necessary packages
import picamera 
import time
import cognitive_face as CF
import json

KEY = '030d5c89e600472bba1d148dddcff568'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)


with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.framerate = 30
    time.sleep(2)
    camera.capture_sequence([
        'image1.jpg',
        ]) 
    r = CF.face.detect('image1.jpg')
    _json = json.dumps(r)
    print(_json)

