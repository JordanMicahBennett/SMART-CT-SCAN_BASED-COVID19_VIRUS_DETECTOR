#Code Written By Jordan Bennett

import covid19_ai_diagnoser_optimal_model_architecture


model = covid19_ai_diagnoser_optimal_model_architecture.model



###########################
#Function written by Jordan to simply collate prediction given image path, based on original code https://github.com/JohnChangUK/Pneumonia-Kaggle/blob/master/test_model_prediction.ipynb
def doOnlineInference (imagePath):
    test_data = []
    img = covid19_ai_diagnoser_optimal_model_architecture.plt.imread(imagePath)
    img = covid19_ai_diagnoser_optimal_model_architecture.cv2.resize(img, (covid19_ai_diagnoser_optimal_model_architecture.img_dims, covid19_ai_diagnoser_optimal_model_architecture.img_dims))
    img = covid19_ai_diagnoser_optimal_model_architecture.np.dstack([img, img, img])
    img = img.astype('float32') / 255
    test_data.append(img)
    prediction = model.predict(covid19_ai_diagnoser_optimal_model_architecture.np.array(test_data))
    _prediction = round( prediction[0][0]*100, 3 )
    if ( _prediction > 50 ):
        _prediction = "Pneumonia detected";
    elif ( _prediction < 50 ):
        _prediction = "Normal lungs detected";  
    outputContent = _prediction + "\n"
    outputContent += "Raw Neural Network Output : " + str(prediction[0][0]) + "\n\n"
    recordInferenceEvent (imagePath, outputContent)
    return outputContent


#Record each inference in a text file 
import datetime
def recordInferenceEvent ( imagePath, outputContent ):
    currentDate = datetime.datetime.now()
    with open("inference_record.txt", "a") as text_file:
        text_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        text_file.write("DATE/TIME : " + str(currentDate.month) + " " + str(currentDate.day) + ", " + str(currentDate.year) + "..." + str(currentDate.hour) + ":" + str(currentDate.minute) + ":" + str(currentDate.second) + "\n\n") 
        text_file.write("IMAGE : " + imagePath + "\n\n")
        text_file.write("RESULT : \n" + outputContent + "\n\n\n\n")


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


