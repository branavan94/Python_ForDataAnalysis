# Transcoding Time Prediction 
## 🐣 Introduction
We got a dataset provided by UCI called Online Video Characteristics and Transcoding Time Dataset.
Our goal is to analyze those data, visualize them, and implement a machine learning model that can be used through a Django API.

About the dataset: <a href="https://archive.ics.uci.edu/ml/datasets/Online+Video+Characteristics+and+Transcoding+Time+Dataset" target="_blank">(Get the Data here)</a>

The dataset is composed of two tsv files named "youtube_videos.tsv" 
and "transcoding_mesurment.tsv". The first contains 10 columns of fundamental 
video characteristics for 1.6 million youtube videos. 
It contains :
* YouTube video id 
* duration 
* bitrate (total in Kbits)
* bitrate (video bitrate in Kbits) 
* height (in pixels)
* width (in pixels)
* framrate
* estimated framerate
* codec
* category
* direct video link. 

The second file of our dataset contains 20 columns which include input and output video characteristics along with their transcoding 
time and memory resource requirements while transcoding videos to diffrent but 
valid formats. The second dataset was collected based on experiments on an Intel 
i7-3720QM CPU through randomly picking two rows from the first dataset and using 
these as input and output parameters of a video transcoding application, ffmpeg 4 . 

The second dataset will be used to build a transcoding time prediction model and show the significance of the datasets.

## 🎯 Objectives

## Data Visualization 
The Data visualization part helped us see the target distribution, and analyze our features.
On the next two plots, we can clearly see that the target variable will need to be scaled. 

### Target Variable Distribution
![GitHub Logo](/images/target.png)

### Target Variable Distribution after scaling
![GitHub Logo](/images/target2.png)

Furthermore, we could visualize the correlation between the target variable and some of the features such as umem (total codec allocated memory for transcoding) which actually makes sense since a bigger allocated memory for transcoding would increase in some ways the time for it to be done.
### Correlation Heatmap
![GitHub Logo](/images/heatmap.png)

## Model implementation  
Now that we've analyzed and plot some of our features, we implemented our model which quickly fitted to our data. 
### Xgb Regressor performance
![GitHub Logo](/images/xgbperf.png)<br>
We can compare our actual model with a linear regression which performs well, but not as good as with our Xgb Regressor.
### Comparison with linear Regression
![linear_reg_1](/images/lm.png)
![linear_reg_2](/images/lm2.png)

## API Django
Our goal is to provide a time prediction for each video given by a user. We'll create a Django Api model that can help us implement an endpoint to use any ML model to our actual problem. For that to be possible, we saved our models as pickle files. Ultimately, we load them on server startup. 
### Creation of an Endpoint for ML models
![GitHub Logo](/images/endpoint.png)

### Creation of the Xgb Regressor model
![GitHub Logo](/images/ml_aglo.png) <br>
Now that we have created our class and instance of ML model, we can try to make predictions through our API.
### Prediction request
![GitHub Logo](/images/predict.png)

## Conclusion
Our dataset gives us a way to easily perform transcoding time prediction on videos. Our initial problem was to predict time in order to help distributed and multicore systems overcome the problem of over provisioning resource for each transcoding jobs. But we have to take into account that the dataset isn't representative of the videos globally. Indeed, if we carefully look into it, we see that lots of these data are well balanced for each format. But one problem remains, there are only 4 formats displayed, and youtube video formats can be FLV, AVI, MOV, MP4, MKV, MPEG, 3GP, WMV and SWF. A way to improve our model is to get more data from different format and have a more generalized model.

