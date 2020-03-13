Jordan Micah Bennett, software engineer/creator of ["RobotizeJa"](https://github.com/JordanMicahBennett/ROBOTIZE_JA).

# SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR
The aim is to develop a quick way to detect the nCov 2019 (Coronavirus 2019/2020, also called disease: "Covid-19" stemming from virus: ["SARS-CoV-2"](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/technical-guidance/naming-the-coronavirus-disease-(covid-2019)-and-the-virus-that-causes-it)) strain, with the plan to use artificial neural networks or other machine learning model types.

This project began on January 29, 2020, here: [SMART-CORONA_VIRUS_DETECTOR](https://github.com/JordanMicahBennett/SMART-CORONA_VIRUS_DETECTOR). This CT-scan version began on [Feb 9, 2020.](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/graphs/contributors)

As this is the first known attempt, [commencing on January 29 2020](https://github.com/JordanMicahBennett/SMART-CORONA_VIRUS_DETECTOR/commit/49984b40847eb168800f0874bae7f8a0f2e20991) aimed at collaborating to construct this type of program, please point to open source packages with similar goals. Please email jordanmicahbennett@gmail.com.

* This can also reasonably allow for less experienced medical personnel to make preliminary diagnoses, expanding the diagnosis efforts overall. This effort may contribute towards virus-control progress, together with [other ai based endeavours being developed across the globe, such as use of ai for vaccine development.](https://www.facebook.com/ProgrammingGodJordan/posts/876578989467795)


# CT Scan Test Viability
* **Feb 9, 2020**: I discover similarities between Covid19 and known forms of pneumonia, after which I find a few CT-Images representing positive cases of Covid19 by Chinese authorities, where I decided to perform **_artificial intelligence based_** **CT Image Scan diagnostics**, by using the images as inputs to an artificial intelligence based pneumonia diagnosis method [originally published/made by John Chang in November 2019](https://github.com/JohnChangUK/Pneumonia-Kaggle). This reasoning is seen in my research/discovery process in the [Deep Learning Code section below](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR#deep-learning-codetests--code-discussion--call-for-contribution).
* **Feb 19, 2020**: Scientists reveal a ~98% accuracy in **_human/radiology based_** **CT Scan image based diagnostics**, compared to the popular Dna polymerase chain reaction method by CDC: ["In a series of 51 patients with chest CT and RT-PCR assay performed within 3 days, the sensitivity of CT for COVID-19 infection was ~98% compared to RT-PCR sensitivity of ~71% (p<.001)."](https://pubs.rsna.org/doi/10.1148/radiol.2020200432)
* **Feb 20, 2020**: Great news - Feb 20 news report published, that Chinese are using Ai to help identify the virus with reported ~99% accuracy, [via their own Ai based CT-scan method](http://www.sixthtone.com/news/1005216/scan-reading-ai-systems-are-helping-doctors-diagnose-covid-19). 
  * Unfortunately, unlike [this repository started by myself on Feb 9th](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/), no Chinese publication of ai based algorithms seems to have been made to the public to help facilitate global control of covid19/SarsCov2.
* **Feb 26, 2020**: [Chinese researchers](https://www.medrxiv.org/content/10.1101/2020.02.25.20021568v1) reveal free access to an artificial intelligence based [online Covid19 Detection tool](http://121.40.75.149/znyx-ncov/index#/app/online_try), although still, no code nor patient data revealed. As a result detection may be slow for users without good internet connection.
  * [I still call to have code/data released for enhanced covid19 spread control](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/README.md#covid-19-ai-datacall-on-the-ministry-of-health).
  * One reason why China should reasonably release their code and data, is because their trained algorithm and data, while providing good basis, may also be [susceptible to race based computation issues](https://time.com/5520558/artificial-intelligence-racial-gender-bias/), simply due to the reality that most Covid19 patient/data are those of Chinese/race. 
      * My showcasing of this repository's code, and or my suggested publication of China's ai code may enable further training on data pertaining to race distributions of the target nation where Covid19 screening is applicable/required, [as seen in other work that stresses accounts for diversity.](https://www.cs.cornell.edu/information/news/newsitem10371/rediet-abebes-contributions-correct-ais-diversity-problem-highlighted).

My repository includes a few fixes of [the original repository](https://github.com/JohnChangUK/Pneumonia-Kaggle), including [a simple user interface to facilitate command-free automated covid19 diagnosis](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/README.md#code-setup-graphical-user-interface).

# CT Test Result Time versus Dna Method (Comparison)
* Molecular and Serology Tests: **[~20 minutes](https://www.cdc.gov/coronavirus/2019-ncov/lab/rt-pcr-detection-instructions.html)** for equipment prep alone, for real-time polymerase chain reaction (RT-PCR), and up to **24 hours** before testing is verified. See **bullet point 3, in answer to question "Can someone who has had COVID-19 spread the illness to others?"** on [this CDC website/covid19 FAQ page.](https://www.cdc.gov/coronavirus/2019-ncov/faq.html)
* [CT Image Scan + Artificial Intelligence Diagnosis](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR): ~5 minutes ([for scan](https://www.ielcap.org/library/lung-cancer-screening/faqs)) + A few milliseconds for [Ai diagnosis](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR) = **~6 minutes total** time for diagnosis result including possible image processing. 


# WORLD HEALTH ORGANIZATION (WHO) WARNING
[Coronavirus: Whole world 'must take action', warns WHO](https://www.bbc.com/news/world-asia-china-51299195)  
[Update Jan 31, 2020/WHO declares the new coronavirus outbreak a Public Health Emergency of International Concern](https://www.who.int/news-room/detail/30-01-2020-statement-on-the-second-meeting-of-the-international-health-regulations-(2005)-emergency-committee-regarding-the-outbreak-of-novel-coronavirus-(2019-ncov))
   * WHO's warning should reasonably have come about a week earlier, [as advised about a week ago via Chris Martenson](https://www.youtube.com/watch?v=Nk5P_iRYwTY), who I also refer to below regarding his 115 million nCov case prediction count.
   * **Update February 7, 2020**: [Artificial Intelligence Prediction: In 45 days, ~2.5 billion to be infected, ~52 million of which may die.](https://www.facebook.com/ProgrammingGodJordan/posts/879754635816897). See also [this detailed forbes report](https://www.forbes.com/sites/johnkoetsier/2020/02/05/ai-predicts-coronavirus-could-infect-25b-and-kill-53m-doctors-say-thats-not-credible-and-heres-why/#96189011cd0d).

# WHY?

* The nCov 2019 (Coronavirus Strain 2019/2020) is spreading rapidly, with a [mortality rate between 2% and 4%](https://www.worldometers.info/coronavirus/).  
    * By comparison, the common flu with a **far lower mortality rate of .1%**, [kills 291,000 to 646,000](https://www.medicinenet.com/script/main/art.asp?articlekey=208914) per year.
    * Things get worse; nCov spreads at ~tripple the transmission rate of the common flu. 
       * Common flu RO = 1.28 ([Estimated, transmission rate](https://bmcinfectdis.biomedcentral.com/articles/10.1186/1471-2334-14-480))
       * nCov RO = 2.5 to 3.8 ([Estimated transmission rate](https://www.sciencenews.org/article/how-new-wuhan-coronavirus-stacks-up-against-sars-mers))
            * Recent nCov RO estimate [~4.08](https://www.medrxiv.org/content/10.1101/2020.01.27.20018952v1)!
            * Recent nCov 2019/Covid19 incubation period is [estimated at 24 days](https://www.businessinsider.com/wuhan-coronavirus-symptoms-24-days-after-infection-2020-2), and a Chinese woman was recently [struck down with symptoms after probation period of 15 days according to the sun newspaper!](https://www.thesun.co.uk/news/10965260/coronavirus-uk-live-updates/#liveblog-entry-241604)
* Current diagnosis methods may miss the presence of the virus due to [faulty dna based comparison methods, where multiple negative test results may occur before positive results are gained.](https://www.bbc.co.uk/news/health-51491763) In addition, more doctors (or rather more automated diagnosis methods) can improve identification rates of the virus.
* This ai driven method will reasonably help to **stop** [the exponential growth](http://www.renewamerica.com/columns/cherry/200126) of the nCov strain. 
    * 1 more month of exponential nCov growth = [~ 115 million cases, (of which ~ 23 million are potentially life threatening ones)](https://www.youtube.com/watch?v=Yq3Y9rmlEQE) according to [an epidemiologist/PhD pathologist](https://en.wikipedia.org/wiki/Christopher_Martenson).
    

# DEEP LEARNING CODE/TESTS + CODE DISCUSSION & CALL FOR CONTRIBUTION


**Code**

1. Covid-19/Coronavirus2019/nCov share many similarities with pneumonia. In fact, the [time course evolution of a specific strain of covid-19 pneumonia is studied here.](https://pubs.rsna.org/doi/10.1148/radiol.2020200370)

2. There are already existent pneumonia deep learning platforms, including kaggle contents rife with [deep learning kernels/solutions, pertaining to pneumonia detection](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia).

3. [A pretrained neural network is chosen from google](https://github.com/JohnChangUK/Pneumonia-Kaggle), pertaining to (2). Pretrained model usage [is a way to avoid training on the 2 gigabytes of pneumonia/non-pneumonia training set](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia/download).
    * I added a quick function "doOnlineInference" to [the code](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/test_model_prediction.py). This is a convenient way to invoke diagnosis on input image.

4. A covid-19 positive Ct scan is taken from [figure 1a](http://images.rsna.org/index.html?doi=10.1148/ryct.2020200028&fig=fig1a) of this [recent covid-19 paper](https://pubs.rsna.org/doi/full/10.1148/ryct.2020200028).

5. Another covid-19 positive Ct scan is taken from [figure 1](http://images.rsna.org/index.html?doi=10.1148/ryct.2020200034&fig=fig1) of [this covid-19 paper](https://pubs.rsna.org/doi/full/10.1148/ryct.2020200034).

6. The function from (3) was invoked on (4), and (4) was successfully detected as covid-19 positive, aka high confidence of pneumonia. The function from (3) was also invoked on (5), although that prediction had a very low confidence that the input was normal/non-pneumonia. **All covid19 positive input images be it (4) or (5) induced prediction of high neural network confidence of the presence of covid19 pneumonia**.
    * [Deep learning based upscaling](https://github.com/JordanMicahBennett/EINSTEIN-BLACK-HOLE-PHOTOGRAPH-ENHANCEMENT/blob/master/README.md) was applied to input image 5, which was of low resolution compared to the training data from kaggle. 
    * Upscaling changed the results for input (5) where the model predicted even lower confidence of non-pneumonia i.e. closer to ground truth, but UPSCALING did not change the result for input (4) which was initially high/closer in resolution to the smallest res sample in the kaggle dataset. 
    * This could be a good/preliminary sign that this tool could be used to actively detect novel coronavirus cases from CT scans.

7. **Preliminary Conclusion**
    * This will reasonably work on potential mild-covid-19 pneumonia patients, within ~0 to 4 days of infection, with "repeated pulmonary CTs", where positive findings of pneumonia associated abnormalities are discoverable.
    * This will likely work better for patients after ~5 days of infection of covid-19, as abnormalities become distributed across the lungs, where initial CT scans could better discover the Covid-19 markers.
    * See [the paper's conclusion](https://pubs.rsna.org/doi/10.1148/radiol.2020200370) for the reasoning above.
    
    

# Code setup (basic user interface)
1. Download [entire repository](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/), which contains [my version of the original code](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/covid19_ai_diagnoser.py) from [another repository](https://github.com/JohnChangUK/Pneumonia-Kaggle) by **John Chang**.
2. Download the [saved weights](https://github.com/JohnChangUK/Pneumonia-Kaggle/blob/master/vgg19.h5) from the original repository, and ensure both the code and weights are in same place.
3. Download the [2 gigabytes training/test data from kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia/download).
4. Run doOnlineInference function from [my version of the original code](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/covid19_ai_diagnoser.py) on any of the test data from the 2 gigabytes kaggle directory, or on the single positive covid-19 example [seen in this repository](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/data/ct-scans/covid-19-positive/coronavirus_positive_WeifangKong_et-al.png), that was taken from [figure 1a](http://images.rsna.org/index.html?doi=10.1148/ryct.2020200028&fig=fig1a) of this [recent covid-19 paper](https://pubs.rsna.org/doi/full/10.1148/ryct.2020200028).

# Code setup (graphical user interface)
**Update: February 18, 2020**
1. Except for item (4), follow all instructions from "[Code setup (basic user interface)](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/README.md#code-setup-basic-user-interface)" section above.

2. Run [my user interface](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/covid19_ai_diagnoser_ui.py), which works with [my version of the original code](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/covid19_ai_diagnoser.py) from this repository. One can either double click the [covid19_ai_diagnoser_ui.py](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/covid19_ai_diagnoser_ui.py) file, or open the file with IDLE, and run there.
  * After running, ui looks like this on first run:
  ![Alt Text](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/data/screenshots/Welcome-Screen_SmartAi%20Coronavirus%202019%20(Covid19)%20Diagnosis%20Interface%20by%20Jordan.png?raw=true)

  * Select/Files > Load an image:
  ![Alt Text](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/data/screenshots/Usage1_TriggerLoadImage-Screen_SmartAi%20Coronavirus%202019%20(Covid19)%20Diagnosis%20Interface%20by%20Jordan.png?raw=true)
  
  * Select an image that pertains to a suspected case, although in the Screenshot, non-coronavirus ct scan is selected
  ![Alt Text](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/data/screenshots/Usage2_SelectImage-Screen_SmartAi%20Coronavirus%202019%20(Covid19)%20Diagnosis%20Interface%20by%20Jordan.png?raw=true)
  
  * Notice the log with the results of the neural network's prediction above the large blue arrow, and the image has been loaded for viewing right of small blue arrow:
  ![Alt Text](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/data/screenshots/Usage3_ImageLoaded_PredictionMade-Screen_SmartAi%20Coronavirus%202019%20(Covid19)%20Diagnosis%20Interface%20by%20Jordan.png?raw=true)
  
  * The model is ~96% accurate on the original task of pneumonia/non-pneumonia classification.
      * See [the bottom of the original page.](https://github.com/JohnChangUK/Pneumonia-Kaggle/blob/master/pneumonia.ipynb)

**CT Scan Manual Diagnosis and Explosion in infection reports**

[CT Scan based diagnostic by human radiologists, have outpaced dna testing, and had lent to China's report of ~15,000 cases overnight, contributing to a total of ~60k+ cases.](https://www.auntminnie.com/index.aspx?sec=sup&sub=cto&pag=dis&itemId=128140) 
* By extension, apart from human radiologist detection, perhaps an ai based image detection solution can speed up diagnosis, and help to replace the [faulty dna based comparison phase](https://www.bbc.co.uk/news/health-51491763). I've also requested more CT image data from a scientist involved with [manual diagnosis using CT scan data](https://pubs.rsna.org/doi/pdf/10.1148/radiol.2020200274).



# DATA
1. [Images](http://images.rsna.org/index.html?doi=10.1148/radiol.2020200274&fig=fig4d) from recent covid-19 study: ["Emerging Coronavirus 2019-nCoV Pneumonia"](https://pubs.rsna.org/doi/full/10.1148/radiol.2020200274)

2. [Images](http://images.rsna.org/index.html?doi=10.1148/ryct.2020200034&fig=fig1) from recent covid-19 study: ["Imaging Profile of the COVID-19 Infection: Radiologic Findings and Literature Review"](https://pubs.rsna.org/doi/full/10.1148/ryct.2020200034)

# REAL TIME TRACKING OF NCOV 2019/2020

By extension, [the tool by researchers at John Hopkins University](https://edition.cnn.com/2020/01/29/health/coronavirus-map-real-time-tracking-trnd/index.html) below, is useful for real time tracking of nCov:

![Alt Text](https://github.com/JordanMicahBennett/SMART-CORONA_VIRUS_DETECTOR/blob/master/nCov%20tracking.png?raw=true)

https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6

Note that despite the ~900+ infection-case number reported via China on January 24, by stark contrast, a [medical scientific paper estimated that ~105,000+ infections actually occured at that time](https://www.medrxiv.org/content/10.1101/2020.01.23.20018549v2.full.pdf). 




# COVID-19 AI DATA/CALL ON THE MINISTRY OF HEALTH 

I call on the [Ministry of Health of Jamaica](https://www.moh.gov.jm/) (as well as other countries) to utilize their administrative status to try to acquire more covid19 positive CT scan images (in federated format that excludes patient identity), from China etc, for improving pneumonia based ai systems, [like the one that I had prepared since February 9, 2020](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/README.md), which I found to successfully detect covid19 presence in a small covid-19 positive CT scan sample set found online so far, [in a paper by Yuen et al](https://pubs.rsna.org/doi/full/10.1148/ryct.2020200034) etc.
  * Alternatively, the Chinese artificial intelligence algorithm/solution together with the data could be attained using the same administrative method.
  * In future scenarios, a "**_Division of Artificial Intelligence Based Health Development_**" or sector of artificial intelligence based research should reasonably exist in the Ministry of Health, that could enable Ai solutions to be rapidly researched/developed, to facilitate production of vaccines, and treatment, as seen in a recent example where [MIT developed antibiotics based on Ai research/development](https://www.iflscience.com/health-and-medicine/artificial-intelligence-finds-a-powerful-new-antibiotic-for-the-first-time/).
  
My advice to Ministry of Health (February 17, 2020): https://drive.google.com/file/d/1dWdqlwUTM9ko8UXGyb8hBYOVOqHv-P_S/view?usp=sharing



# Update March 5, 2020:
1. [Jordan added fix to original author's repository](https://github.com/JohnChangUK/Pneumonia-Kaggle/issues/1), to enable correct validation. John Chang had inadvertently misdefined some "test_dataGen.flow_from_director" function parameter as a training dataset input, instead of a test dataset input.

2. [Jordan updated his version of the original code](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/covid19_ai_diagnoser.py), such that a compile issue is repaired, in order to facilitate accuracy evaluation of the saved/loaded (in 2 minutes on gtx 1060/i7 cpu) model without invocation of model-training function **model.fit**, which would take hours on the same machine.
