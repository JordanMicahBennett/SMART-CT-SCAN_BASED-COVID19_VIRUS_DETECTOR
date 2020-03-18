#Original code: https://www.kaggle.com/gbellport/pneumonia-detection-96-recall-91-accuracy/output
#Code modified by Jordan Bennett , and converted from .pynb to .py using https://jupyter.org/try

######################
# Jordan's modifications : 
#1. Model training components removed. (Saved weight loading takes place instead)
#2. Replace pyplot -> plt.imread, with  gray scale cv2.imread(path,0), so that ui's image load process doesn't throw a pyimage10 error
#3. Other pyplot related code removed.
#4. Confusion Matrix Format added, as quick explanation of Confusion Matrix that was already included.
#5. Specificty calculation and relevant label added.


# General libraries
import os
import numpy as np
import random
import cv2



# Deep learning libraries
import keras.backend as K
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization
from keras.layers import Conv2D, SeparableConv2D, MaxPool2D, LeakyReLU, Activation
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
import tensorflow as tf





#################################
#GLOBAL UTILITY
##Serves both Section B: "regular pneumonia..." and Section D: "covid19 pneumonia..." accuracy report sections.



# Hyperparameters
img_dims = 150
batch_size = 32



###########
#Util Component 1: Confusion matrix report/Accuracy measures
from sklearn.metrics import accuracy_score, confusion_matrix

def renderConfusionMetrics ( ___model, _testData, _testLabels, enableTraining, ___train_gen, ___test_gen, __batch_size, __epochs, hdf5_testSaveFileName ):
    preds = ___model.predict(_testData)

    acc = accuracy_score(_testLabels, np.round(preds))*100
    cm = confusion_matrix(_testLabels, np.round(preds))
    tn, fp, fn, tp = cm.ravel()


    print('\nCONFUSION MATRIX FORMAT ------------------\n')
    print("[true positives    false positives]")
    print("[false negatives    true negatives]\n\n")

    print('CONFUSION MATRIX ------------------')
    print(cm)

    print('\nTEST METRICS ----------------------')
    precision = tp/(tp+fp)*100
    recall = tp/(tp+fn)*100
    specificity = tn/(tn+fp)*100 #Jordan_note: added specificity calculation 
    print('Accuracy: {}%'.format(acc))
    print('Precision: {}%'.format(precision))
    print('Recall/Sensitivity: {}%'.format(recall)) #Jordan_note: added sensitivity label
    print('Specificity {}%'.format(specificity)) #Jordan_note: added specificity calculation 
    print('F1-score: {}'.format(2*precision*recall/(precision+recall)))


    if enableTraining:
        checkpoint = ModelCheckpoint(filepath=hdf5_testSaveFileName, save_best_only=True, save_weights_only=True)
        lr_reduce = ReduceLROnPlateau(monitor='val_loss', factor=0.3, patience=2, verbose=2, mode='max')
        early_stop = EarlyStopping(monitor='val_loss', min_delta=0.1, patience=1, mode='min')


        hist = ___model.fit_generator(
                   ___train_gen, steps_per_epoch=___test_gen.samples // __batch_size, 
                   epochs=__epochs, validation_data=___test_gen, 
                   validation_steps=___test_gen.samples // __batch_size, callbacks=[checkpoint, lr_reduce])

        print('\nTRAIN METRIC ----------------------')
        print('Covid19 Train acc: {}'.format(np.round((hist.history['acc'][-1])*100, 2)))


###########
#Util Component 2:model architecture description
def defineModelArchitecture (_img_dims ):
    # Input layer
    inputs = Input(shape=(_img_dims, _img_dims, 3))

    # First conv block
    x = Conv2D(filters=16, kernel_size=(3, 3), activation='relu', padding='same')(inputs)
    x = Conv2D(filters=16, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    # Second conv block
    x = SeparableConv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = SeparableConv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    # Third conv block
    x = SeparableConv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = SeparableConv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    # Fourth conv block
    x = SeparableConv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = SeparableConv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(2, 2))(x)
    x = Dropout(rate=0.2)(x)

    # Fifth conv block
    x = SeparableConv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = SeparableConv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(2, 2))(x)
    x = Dropout(rate=0.2)(x)

    # FC layer
    x = Flatten()(x)
    x = Dense(units=512, activation='relu')(x)
    x = Dropout(rate=0.7)(x)
    x = Dense(units=128, activation='relu')(x)
    x = Dropout(rate=0.5)(x)
    x = Dense(units=64, activation='relu')(x)
    x = Dropout(rate=0.3)(x)

    # Output layer
    output = Dense(units=1, activation='sigmoid')(x)
    
    return inputs, output



###########
#Util Component 3: Data processor
#Note: This process does not use validation path, because validation path in the original competion reasonably had too little data (8 samples) to create any insight.
# the "directoryProcessArray" param from "reportFileDistributions" function corresponds to the hard-coded sub-directories of train and test, excluding val.
def process_data(___inputPath, img_dims, batch_size):
    # Data generation objects
    train_datagen = ImageDataGenerator(rescale=1./255, zoom_range=0.3, vertical_flip=True)
    test_val_datagen = ImageDataGenerator(rescale=1./255)
    
    # This is fed to the network in the specified batch sizes and image dimensions
    train_gen = train_datagen.flow_from_directory(
    directory=___inputPath+'train', 
    target_size=(img_dims, img_dims), 
    batch_size=batch_size, 
    class_mode='binary', 
    shuffle=True)

    test_gen = test_val_datagen.flow_from_directory(
    directory=___inputPath+'test', 
    target_size=(img_dims, img_dims), 
    batch_size=batch_size, 
    class_mode='binary', 
    shuffle=True)
    
    # I will be making predictions off of the test set in one batch size
    # This is useful to be able to get the confusion matrix
    test_data = []
    test_labels = []

    for cond in ['/NORMAL/', '/PNEUMONIA/']:
        for img in (os.listdir(___inputPath + 'test' + cond)):
            img = cv2.imread(___inputPath+'test'+cond+img,0) #Replace plt.imread, with  gray scale cv2.imread(path,0), so that ui's image load process doesn't throw a pyimage10 error
            img = cv2.resize(img, (img_dims, img_dims))
            img = np.dstack([img, img, img])
            img = img.astype('float32') / 255
            if cond=='/NORMAL/':
                label = 0
            elif cond=='/PNEUMONIA/':
                label = 1
            test_data.append(img)
            test_labels.append(label)
        
    test_data = np.array(test_data)
    test_labels = np.array(test_labels)
    
    return train_gen, test_gen, test_data, test_labels
    


###########
#Util Component 4: Report file distributions
#directoryProcessArray eg, = ['train', 'val', 'test'], in the case that training val and test folders exist in sub-dir for processing.
def reportFileDistributions (___inputPath, directoryProcessArray):
    for _set in directoryProcessArray:
        n_normal = len(os.listdir(___inputPath + _set + '/NORMAL'))
        n_infect = len(os.listdir(___inputPath + _set + '/PNEUMONIA'))
        print('Set: {}, normal images: {}, regular pneumonia images: {}'.format(_set, n_normal, n_infect))















########################################################################
# disabling warnings
import logging
logging.getLogger('tensorflow').disabled = True #Jordan_note: Disable red warning lines seen at model architecture creation.

# Setting seeds for reproducibility
seed = 232
np.random.seed(seed)
tf.set_random_seed(seed)












########################################################################
#SECTION A: MODEL ARCHITECTURE REGULAR PNEUMONIA DETECTOR

inputs, output = defineModelArchitecture ( img_dims )

# Creating model and compiling
model_pneumoniaDetector = Model(inputs=inputs, outputs=output)
model_pneumoniaDetector.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_pneumoniaDetector.load_weights('best_weights_kaggle_user_pneumonia2_0.hdf5')

########################################################################
#SECTION B: REGULAR PNEUMONIA VS NORMAL LUNG ACCURACY REPORT [LOADED MODEL/WEIGHTS]
print('\n\n#######REGULAR PNEUMONIA VS NORMAL LUNG TEST REPORT [LOADED MODEL/WEIGHTS]')
# Lets first look at some of our X-ray images and how each dataset is distributed:

input_path_b = 'xray_dataset/'

# Report file distributions
reportFileDistributions (input_path_b, ['train', 'val', 'test'] )

# Getting the data
train_gen, test_gen, test_data_b, test_labels_b = process_data(input_path_b, img_dims, batch_size)

# Reporting on accuracies
renderConfusionMetrics ( model_pneumoniaDetector, test_data_b, test_labels_b, False, None, None, None, None, None )













########################################################################
#SECTION C: MODEL ARCHITECTURE COVID19 DETECTOR

inputs, output = defineModelArchitecture ( img_dims )


# Creating model and compiling
model_covid19PneumoniaDetector = Model(inputs=inputs, outputs=output)
model_covid19PneumoniaDetector.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_covid19PneumoniaDetector.load_weights('best_weights_kaggle_user_pneumonia2_0.hdf5')


###################################################################
#SECTION D: COVID19 PNEUMONIA VS NORMAL LUNG ACCURACY REPORT [LOADED MODEL/WEIGHTS]
print('\n\n#######UNTRAINED COVID19 PNEUMONIA VS NORMAL LUNG TEST REPORT [LOADED MODEL/WEIGHTS]')
      
#Jordan_note establish custom_path for covid 19 test data
input_path_d = 'xray_dataset_covid19/'


# Report file distributions
reportFileDistributions (input_path_d, ['train', 'test'])

# Getting the data
train_gen_d, test_gen_d, test_data_d, test_labels_d = process_data(input_path_d, img_dims, batch_size)

# Reporting on accuracies
renderConfusionMetrics ( model_covid19PneumoniaDetector, test_data_d, test_labels_d, False, train_gen_d, test_gen_d, batch_size, 10, 'covid19_weights_v2.hdf5' )

