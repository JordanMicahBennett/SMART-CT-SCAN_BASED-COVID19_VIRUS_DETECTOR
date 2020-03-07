#Original code: https://github.com/JohnChangUK/Pneumonia-Kaggle/blob/master/test_model_prediction.ipynb
#Code modified by Jordan Bennett, and converted from .pynb to .py using https://jupyter.org/try

from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np


###########################
# Routine/fix added by Jordan to update learning rate name from learning_rate to lr, to comply with current keras version at compile time. Fix alters vgg19.h5 file to effect the update.
# Taken by combining solutions below:
#           1) https://stackoverflow.com/a/59700084
#           2) response to (1) by "Qin Heyang"
# Error repaired when trying to load default "vgg19.h5" file: "TypeError: Unexpected keyword argument passed to optimizer: learning_rate"
import h5py
f = h5py.File("vgg19.h5",'r+') 
data_p = f.attrs['training_config']
data_p = data_p.decode().replace("learning_rate","lr").encode()
f.attrs['training_config'] = data_p
f.close()
#end fix


model = load_model('vgg19.h5')



###########################
#Function written by Jordan to simply collate prediction given image path, based on original code https://github.com/JohnChangUK/Pneumonia-Kaggle/blob/master/test_model_prediction.ipynb
def doOnlineInference (imagePath):
    input_image = image.load_img(imagePath, target_size=(224, 224))
    input_image_array = image.img_to_array(input_image)
    image_array_expanded = np.expand_dims(input_image_array, axis = 0)
    image_array_expanded_preprocessed = preprocess_input(image_array_expanded)
    prediction = model.predict(image_array_expanded_preprocessed)
    outputContent = "Normal with (" + str( round( prediction[0][0]*100, 3 )) + "%) confidence.\n\n"
    outputContent += "Coronavirus Pneumonia with ("  + str( round( prediction[0][1]*100, 3 ) ) + "%) confidence.\n\n" 
    outputContent += "Raw neural network output array [normal,pneumonia] ~> [" + str( round( prediction[0][0], 3 )) + "," + str( round( prediction[0][1], 3 )) + "]\n\n\n"
    return outputContent




##########################
# Function added by Jordan to evaluate accuracy of loaded model. Model is evaluated without the need for retraining.
# Thus, this faciliates accuracy evaluation of the saved/loaded (in 2 minutes on gtx 1060/i7 cpu) model without invocation of model-training function **model.fit**, which would take hours on the same machine.

# Evaluate saved model
from keras.preprocessing.image import ImageDataGenerator

test_sample_number = 624 #no of example ct scan images in "xray_dataset/test"

test_dataGen = ImageDataGenerator(rescale=1./255)

test_set = test_dataGen.flow_from_directory('xray_dataset/test',
                                                target_size=(224, 224),
                                                batch_size=32,
                                                class_mode='categorical')

score = model.evaluate_generator(test_set, test_sample_number/32, workers=12)
print ("model accuracy [loss = " + str(score[0]*100) + "%, accuracy = " + str(score[1]*100) +"%]")
#See metrics using: `model.metrics_names` 



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


