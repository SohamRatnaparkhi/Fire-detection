import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image

import time

from fire_alarms import *

# Load the saved model
model = tf.keras.models.load_model(r'E:\Fire_and_Smoke_Detector\MODEL\Fire_detection_model.h5')
print("\n-------------------\nModel Loaded succesfully\n-------------------\n")
video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()

    # TODO: Convert the captured frame into RGB
    im = Image.fromarray(frame, 'RGB')

    # TODO: Resizing into 224x224 because we trained the model with this image size.
    im = im.resize((224, 224))

    # Todo: Normalization
    img_array = image.img_to_array(im)

    # ? print(img_array.shape) 3 dims but model 4 dim
    img_array = np.expand_dims(img_array, axis=0) / 255 # Normalization of image
    probabilities = model.predict(img_array)[0]
    # print(probabilities, probabilities.shape)
    # TODO: Making prediction
    prediction = np.argmax(probabilities)

    # ? if prediction is 0, which means there is fire in the frame.
    if prediction == 0:
        # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        # time.sleep(2)
        print("\n-------------------\n🔥 FIRE DETECTED! 🔥\n-------------------")

        # * 1 Send email
        print("\n\nEMAIL-Sending!")
        email_sender()
        print("--------------\nEMAIL-SENT!")

        # * 2 Message
        print("--------------\nsending message")

        # * 3 Play alarm
        print("--------------\nPLAYING ALARM")
        alarm_sound()

    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
