import requests
import numpy as np
import cv2
while True:
    images=requests.get("http://192.168.43.69:8080/shot.jpg")
    video=np.array(bytearray(images.content),dtype=np.uint8)
    rendor=cv2.imdecode(video,-1)

    cv2.imshow('frame', rendor)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break