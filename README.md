Jordan Micah Bennett, software engineer/creator of ["RobotizeJa"](https://github.com/JordanMicahBennett/ROBOTIZE_JA).

# SMART-SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR
The aim is to develop a quick way to detect the nCov 2019 (Coronavirus 2019/2020, also called "Covid-19") strain, with the plan to use artificial neural networks or other machine learning model types.

This project began on January 29, 2020, here: [SMART-CORONA_VIRUS_DETECTOR](https://github.com/JordanMicahBennett/SMART-CORONA_VIRUS_DETECTOR).

As this is the first known attempt, [commencing on January 29 2020](https://github.com/JordanMicahBennett/SMART-CORONA_VIRUS_DETECTOR/commit/49984b40847eb168800f0874bae7f8a0f2e20991) aimed collaborating to construct this type of program, please point to open source packages with similar goals. Please email jordanmicahbennett@gmail.com.


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
* Current diagnosis methods may miss the presence of the virus due to [faulty dna based comparison methods, where multiple negative test results may occur before positive results are gained.](https://www.bbc.co.uk/news/health-51491763) In addition, more doctors (or rather more automated diagnosis methods) can improve identification rates of the virus.
* This ai driven method will reasonably help to **stop** [the exponential growth](http://www.renewamerica.com/columns/cherry/200126) of the nCov strain. 
    * 1 more month of exponential nCov growth = [~ 115 million cases, (of which ~ 23 million are potentially life threatening ones)](https://www.youtube.com/watch?v=Yq3Y9rmlEQE) according to [an epidemiologist/PhD pathologist](https://en.wikipedia.org/wiki/Christopher_Martenson).
    

# DEEP LEARING CODE/TESTS + CODE DISCUSSION & CALL FOR CONTRIBUTION


**Code**

1. Covid-19/Coronavirus2019/nCov share many similarities with pnuemonia. In fact, the [time course evolution of a specific strain of covid-19 pnuemonia is studied here.](https://pubs.rsna.org/doi/10.1148/radiol.2020200370)

2. There are already existent pneumonia deep learning platforms, including kaggle contets rife with [deep learning kernels/solutions, pertaining to pnuemonia detection](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia).

3. [A pretrained neural network is chosen from google](https://github.com/JohnChangUK/Pneumonia-Kaggle), pertaining to (2). Pretrained model usage [is a way to avoid training on the 2 gigabytes of pneumonia/non-pneumonia training set](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia/download).
    * I added a quick function "doOnlineInference" to [the code](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/test_model_prediction.py). This is a convenient way to invoke diagnosis on input image.

4. A covid-19 positive Ct scan is taken from [figure 1a](http://images.rsna.org/index.html?doi=10.1148/ryct.2020200028&fig=fig1a) of this [recent covid-19 paper](https://pubs.rsna.org/doi/full/10.1148/ryct.2020200028).

5. Another covid-19 positive Ct scan is taken from [figure 1](http://images.rsna.org/index.html?doi=10.1148/ryct.2020200034&fig=fig1) of [this covid-19 paper](https://pubs.rsna.org/doi/full/10.1148/ryct.2020200034).

6. The function from (3) was invoked on (4), and (4) was successfully detected as covid-19 positive, aka high confidence of pnuemonia. The function from (3) was also invoked on (5), although that prediction had a very low confidence that the input was normal/non-pneumonia. 
    * [Deep learning based upscaling](https://github.com/JordanMicahBennett/EINSTEIN-BLACK-HOLE-PHOTOGRAPH-ENHANCEMENT/blob/master/README.md) was applied to input image 5, which was of low resolution compared to the training data from kaggle. 
    * Upscaling changed the results for input (5) where the model predicted even lower confidence of non-pnuemonia i.e. closer to ground truth, but UPSCALING did not change the result for input (4) which was initially high/closer in resolution to the smallest res sample in the kaggle dataset. 
    * This could be a good/preliminary sign that this tool could be used to actively detect novel coronavirus cases from CT scans.

7. **Preliminary Conclusion**
    * This will reasonably work on potential mild-covid-19 pneumonia patients, within ~0 to 4 days of infection, with "repeated pulmonary CTs, where positive findings of pneumonia associated abnormalities are discoverable.
    * This will likely work better for patients after ~5 days of infection of covid-19, as abnormailities become distributed accross the lungs, where initial CT scans could better discover the Covid-19 markers.
    * See [the paper's conclusion](https://pubs.rsna.org/doi/10.1148/radiol.2020200370) for the reasoning above.
    
    

**Code setup**
1. Download [my version of the code](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/test_model_prediction.py) from this repository.
2. Download the [saved weights](https://github.com/JohnChangUK/Pneumonia-Kaggle/blob/master/vgg19.h5) from the original repository, and ensure both the code and weights are in same place.
3. Download the [2 gigabytes training/test data from kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia/download).
4. Run doOnlineInference function on any of the test data from the 2 gigabytes kaggle directory, or on the single positive covid-19 example [seen in this repository](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/data/ct-scans/covid-19-positive/coronavirus_positive_WeifangKong_et-al.png), that was taken from [figure 1a](http://images.rsna.org/index.html?doi=10.1148/ryct.2020200028&fig=fig1a) of this [recent covid-19 paper](https://pubs.rsna.org/doi/full/10.1148/ryct.2020200028).


**CT Scan Manual Diagnosis and Explosion in infection reports**

[CT Scan based diagnostic by human radiologists, have outpaced dna testing, and had lent to China's report of ~15,000 cases overnight.](https://www.auntminnie.com/index.aspx?sec=sup&sub=cto&pag=dis&itemId=128140) 
* By extension, apart from human radiologist detection, perhaps an ai based image detection solution can speed up diagnosis, and help to replace the [faulty dna based comparison phase](https://www.bbc.co.uk/news/health-51491763). I've also requested more CT image data from a scientist involved with [manual diagnosis using CT scan data](https://pubs.rsna.org/doi/pdf/10.1148/radiol.2020200274).



# DATA
1. [Images](http://images.rsna.org/index.html?doi=10.1148/radiol.2020200274&fig=fig4d) from recent covid-19 study: ["Imaging Profile of the COVID-19 Infection: Radiologic Findings and Literature Review"](https://pubs.rsna.org/doi/full/10.1148/radiol.2020200274)

2. [Images](http://images.rsna.org/index.html?doi=10.1148/ryct.2020200034&fig=fig1) from recent covid-19 study: ["Imaging Profile of the COVID-19 Infection: Radiologic Findings and Literature Review"](https://pubs.rsna.org/doi/full/10.1148/ryct.2020200034)

# REAL TIME TRACKING OF NCOV 2019/2020

By extension, [the tool by researchers at John Hopkins University](https://edition.cnn.com/2020/01/29/health/coronavirus-map-real-time-tracking-trnd/index.html) below, is useful for real time tracking of nCov:

![Alt Text](https://github.com/JordanMicahBennett/SMART-CORONA_VIRUS_DETECTOR/blob/master/nCov%20tracking.png?raw=true)

https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6

Note that despite the ~900+ infection-case number reported via China on January 24, by stark contrast, a [medical scientific paper estimated that ~105,000+ infections actually occured at that time](https://www.medrxiv.org/content/10.1101/2020.01.23.20018549v2.full.pdf). All sources thus far ought to be scrutinized, as is typical in scientfic endeavour.

