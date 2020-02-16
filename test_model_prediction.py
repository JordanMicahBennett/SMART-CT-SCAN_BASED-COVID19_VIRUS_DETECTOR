#Original code: https://github.com/JohnChangUK/Pneumonia-Kaggle
#Code converted and mofified from .pynb to .py by Jordan Bennett using https://jupyter.org/try

# In[24]:


from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np


# In[43]:


model = load_model('vgg19.h5',compile=False) #Note by Jordan: compile=False added to resolve "Unexpected keyword passed to optimizer error. This error is caused by tensorflow/keras mismatch, since keras upgrade since original author wrote code.
normal_img = image.load_img('xray_dataset/val/NORMAL/NORMAL2-IM-1430-0001.jpeg', target_size=(224, 224))
pneumonia_img = image.load_img('xray_dataset/val/PNEUMONIA/person1946_bacteria_4875.jpeg', target_size=(224, 224))
normal_img_array = image.img_to_array(normal_img)
pneumonia_img_array = image.img_to_array(pneumonia_img)

# Model.predict requires 4 dimensions
normal = np.expand_dims(normal_img_array, axis = 0)
pneumonia = np.expand_dims(pneumonia_img_array, axis = 0)


# In[52]:


normal_image = preprocess_input(normal)
pneumonia_image = preprocess_input(pneumonia)

predict_normal = model.predict(normal_image)
predict_pneumonia = model.predict(pneumonia_image)
print('The 1st element is NORMAL, the 2nd element is PNEUMONIA')
print('Should have predicted normal: ', predict_normal)
print('Should have predicted pneumonia: ', predict_pneumonia)


#function written by Jordan to simply collate prediction given image path, based on code above
def doOnlineInference (imagePath):
    input_image = image.load_img(imagePath, target_size=(224, 224))
    input_image_array = image.img_to_array(input_image)
    image_array_expanded = np.expand_dims(input_image_array, axis = 0)
    image_array_expanded_preprocessed = preprocess_input(image_array_expanded)
    return model.predict(image_array_expanded_preprocessed)


# In[19]:





# In[ ]:




