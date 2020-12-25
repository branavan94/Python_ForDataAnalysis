# Transcoding Time Prediction 
## 🐣 Introduction
We are provided a data set coming from the machine learning repository UCI, a center that give us the opportunity to have access to more than a 500 data sets.
Our goal is to analyze those data, visualize it, and implement a machine learning model that can be used through a Django API.

About the dataset: <a href="https://archive.ics.uci.edu/ml/datasets/Online+Video+Characteristics+and+Transcoding+Time+Dataset" target="_blank">(Get the Data here)</a>

The dataset is composed of two tsv files named "youtube_videos.tsv" 
and "transcoding_mesurment.tsv". The first contains 10 columns of fundamental 
video characteristics for 1.6 million youtube videos. 
It contains :
* YouTube video id 
* duration 
* bitrate(total in Kbits)
* bitrate(video bitrate in Kbits) 
* height(in pixle)
* width(in pixles)
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

### Target Variable Distribution
![GitHub Logo](/images/target.png)

### Target Variable Distribution after scaling
![GitHub Logo](/images/target2.png)
### Correlation Heatmap
![GitHub Logo](/images/heatmap.png)

## Model implementation  
### Xgb Regressor performance
![GitHub Logo](/images/xgbperf.png)

## API Django
### Creation of an Endpoint for ML models
![GitHub Logo](/images/endpoint.png)

### Creation of the Xgb Regressor model
![GitHub Logo](/images/ml_aglo.png)

### Prediction request
![GitHub Logo](/images/predict.png)

