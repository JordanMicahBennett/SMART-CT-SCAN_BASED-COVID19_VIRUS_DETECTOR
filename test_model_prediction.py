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
    return model.predict(image_array_expanded_preprocessed)

