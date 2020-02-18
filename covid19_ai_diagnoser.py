#Original code: https://github.com/JohnChangUK/Pneumonia-Kaggle/blob/master/test_model_prediction.ipynb
#Code modified by Jordan Bennett, and converted from .pynb to .py using https://jupyter.org/try

from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

model = load_model('vgg19.h5',compile=False) #Note by Jordan: compile=False added to resolve "Unexpected keyword passed to optimizer error. This error is caused by tensorflow/keras mismatch, since keras upgrade since original author wrote code.

#function written by Jordan to simply collate prediction given image path, based on original code https://github.com/JohnChangUK/Pneumonia-Kaggle/blob/master/test_model_prediction.ipynb
def doOnlineInference (imagePath):
    input_image = image.load_img(imagePath, target_size=(224, 224))
    input_image_array = image.img_to_array(input_image)
    image_array_expanded = np.expand_dims(input_image_array, axis = 0)
    image_array_expanded_preprocessed = preprocess_input(image_array_expanded)
    prediction = model.predict(image_array_expanded_preprocessed)
    print ( "Normal with (" + str( round( prediction[0][0]*100, 3 )) + ")% confidence." )
    print ( "Coronavirus Pneumonia with ("  + str( round( prediction[0][1]*100, 3 ) ) + ")% confidence." )
    print ( "Raw neural network output array [normal,pneumonia] ~> [" + str( round( prediction[0][0], 3 )) + "," + str( round( prediction[0][1], 3 )) + "]\n\n" )



"""
NORMAL SAMPLES:
doOnlineInference("xray_dataset/val/NORMAL/NORMAL2-IM-1430-0001.jpeg")
doOnlineInference("xray_dataset/val/NORMAL/NORMAL2-IM-1427-0001.jpeg")

PNEUMONIA SAMPLES:
doOnlineInference("xray_dataset/val/PNEUMONIA/person1946_bacteria_4875.jpeg")
doOnlineInference("xray_dataset/val/PNEUMONIA/person1950_bacteria_4881.jpeg")

ACTUAL CORONAVIRUS SAMPLES:
doOnlineInference("coronavirus_positive_WeifangKong_et-al.jpg")
doOnlineInference("coronavirus_positive_day7_of_infection_UPSCALED.jpg")
"""
