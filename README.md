# Data Science Portfolio

Compilation of notebooks and projects which I created in my learning journey of data analysis and exploration of machine learning concepts.

## Stand-alone projects

### FPGA Neural Network Accelerator
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/tirumalnaidu/opencl-cnn-accelerator)

We designed a Neural Network Accelerator for Darknet Reference Model (which is 2.9 times faster than AlexNet and attains the same top-1 and 
top-5 performance as AlexNet but with 1/10th the parameters) for 
image classification on Imagenet Dataset on Intel Cyclone V Soc FPGA, while working as a part-time undergrad researcher under 
guidance of [Prof. Vinod Kumar Jain](https://sites.google.com/view/dr-vinod-kumar-jain/home?authuser=0). When connected to ARM Cortex A9 processor using OpenCL framework, 
it achieved around 300% faster inference speed than CPU.

Contributor: [Tirumal Naidu](https://www.linkedin.com/in/tirumalnaidu/?originalSubdomain=in)


### AWS SageMaker - Fraud Detection service
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/Side-Projects/tree/main/aws-SageMaker-fraud-detection)

The goal of this project is to underdstand the complete machine learning work flow 
(from data collection, data storing, data preprocessing, model selection, training and finally to model deployement) 
using AWS SageMaker. I built an end to end fraud detection service system using services provided by AWS.
Trained machine learning job and deployed model using SageMaker, created endpoint that can be invoked by Lambda, 
created API with API Gateway in order to send request to flask application.
Deployed the application on AWS Cloud9 environment and finally integrated the application with SNS service to alert client by sending email when fraud is detected.

### Early detection of Autism in toddlers

Studied various approaches to identify autism spectrum disorder(ASD) traits in toddlers.
Designed a system which analyses gaze patterns for early detection of Autism.
The system accurately predicted whether a child has autism 62% of the time.
Studied various pros and cons of using gaze as a measure of Autism screening in toddlers.

## Classification problems

### Heartbeat anomaly detection
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/Side-Projects/tree/main/heart-ECG-anomaly-detection)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/jithendrabsy/Side-Projects/blob/main/heart-ECG-anomaly-detection/AutoEncoder_AnomalyDetection.ipynb)

Detected anomalies in heartbeats using LSTM Auto-encoder. The dataset used contains 5000 time series sequences with 140
timestamps obtained with ECG and corresponds to heartbeats from a
single patient. Trained and evaluated autoencoder, chose a threshold for anomaly
detection and finally classified unseen examples as normal or anomaly.

### Credit card fraud detection
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/Side-Projects/tree/main/mini-projects/credit-card-fraud-detection)

Identified fraudulent credit card transactions in a highly imbalanced dataset using oversampling methods (SMOTE) and ensemble learning model (Random Forest).

### Titanic: Machine Learning from Disaster
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/jithendrabsy/Side-Projects/blob/main/mini-projects/kaggleTitanic/titanic-v2.ipynb)

Titanic: Machine Learning from Disaster is a knowledge competition on Kaggle. 
Like many others, I started practicing machine learning with this.
Various versions of notebooks and approaches can be found in this [github repo](https://github.com/jithendrabsy/Side-Projects/tree/main/mini-projects/kaggleTitanic).

## Quantitative Analysis

### Buy or Sell Stocks? - Dual Moving Average Crossover (DMAC) trading strategy
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/jithendrabsy/Side-Projects/blob/main/buy-or-sell-stocks/MARUTI_DMAC.ipynb)

Predicted when to buy or sell stocks using simple dual moving average crossover strategy. And then backtested it over 5 years of stock.
I used Yahoo! finance data downloader to download the stocks of Maruti Suzuki (MARUTI.NS).
A return of 113% in 5 years estimated by DMAC strategy with short and long windows 13 and 48 respectively. However - It is up to the trader to 
choose the number of days to which the two moving averages are set. This should be done 
after testing and evaluating the system thoroughly in the recommended way, using the trader’s method.

## Regression Problems

### Predicting chance of admission for MS applications
[![kaggle-kernel](https://img.shields.io/badge/Kaggle-kernel-1f425f.svg)](https://www.kaggle.com/saiyan6174/eda-predicting-chance-of-ms-admission#Analysing-&-Predicting-MS-Admission)

It was almost admission season. I’ve got a couple of friends who are preparing for GRE. 
This made me to try What could be their chance of admit and how it may vary with other parameters? In this notebook, 
I used the dataset mentioned in this [paper](https://ieeexplore.ieee.org/document/8862140) and tried to predict the chance 
of admit based on different parameters. Before modeling and predicting, I performed 
Eploratory Data Analysis on the data to get some insights on MS admissions. I used PyCaret for modeling.


## Time Series Problems

### Forecasting Air pollution
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/Side-Projects/tree/main/mini-projects/forecasting-air-pollution)

In this project, I explored various models for forecasting time series. I then compared the performance of the models over two different metrics.
I forecasted the amount of pollution in air based on the historical pollution data. 
I used Beijing pollution public dataset - which contains data from 2010-14, along with extra weather features such as temperature, windspeed, pressure etc.

### Stock data analysis and forecasting
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/Side-Projects/tree/main/mini-projects/forecasting-Stocks)

This is a playground project where I explored time series data of historical stock prices of some publicly listed companies. 
Stock data was collected using Pandas Datareader with the help of Tiingo API.
Experimented with  Long Short Term Memory(LSTM) networks and Facebook's Prophet to forecast the stocks.

### Forecasting Monthly robberies
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/jithendrabsy/Side-Projects/blob/main/mini-projects/forecasting-MonthlyRobberies/forecasting_monthly_robberies_boston.ipynb)

This is a playground project where I played with ARIMA model for forecasting monthly robberies in Boston.
I manually configures ARIMA, then grid-searched the ARIMA parameters and aslo played with data transformations.

## NLP projects

### Using News headlines to predict stock movements
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/jithendrabsy/Side-Projects/blob/main/mini-projects/nlp-for-stock-movement-prediction/stock-sentiment.ipynb)

Predicted whether Dow Jones Industrial Average (DJIA's) Adj. Close value raises or decreases based on sentiment of top news headlines. The dataset I used 
for this analysis is from [kaggle](https://www.kaggle.com/aaron7sun/stocknews).
I used VADER sentiment analysis package which is a lexicon and rule-based sentiment analysis tool. I calculated polarity and subjectivity of news headlines 
for everyday and used them as features along with the stock features. Then I modeled the data with various classifiers and Linear Discriminant Analysis (LDA) 
classifier gave the better accuracy.

## Computer Vision Projects

### Reading Captchas
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/Side-Projects/tree/main/mini-projects/reading-captcha)

This is a playground computer vision project where I experimented with Lenet using Keras to detect and read the numbers from captcha images. 


## Data Analysis (EDA)

### Analysis of Top Spotify songs from 2010-2019
[![kaggle-kernel](https://img.shields.io/badge/Kaggle-kernel-1f425f.svg)](https://www.kaggle.com/saiyan6174/eda-on-top-spotify-songs)

I explored all the top songs on Spotify from 2010-19 (found a [dataset](https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year) on kaggle). 
This helped me to understand what are the common things between the songs 
that reached the top of Spotify charts at the end of every year. Also, helped in gaining some cool insights.
Listed few cool insights - [here](https://github.com/jithendrabsy/Side-Projects/blob/main/mini-projects/when-music-meets-datascience/analyzing-top-spotify-songs_from-2010-19/insights.md)

### Analysis my personal Spotify streaming history
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/jithendrabsy/Side-Projects/blob/main/mini-projects/when-music-meets-datascience/analyzing-my-music-taste-variation/analyzing-variation-in-my-music-taste.ipynb)

I know that my music taste changed a lot in past few years, So I wanted to see how it changed over time.
I collected my streaming history using Spotipy which is a light weight client to extract many features from Spotify's web API.
I analyzed my spotify streaming history to understand how my music taste is varying over time.
This helped me to find out my top songs, artists, genres and time I am spending on each of them.

### Anslysis of my favorite artist's discography
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/jithendrabsy/Side-Projects/blob/main/mini-projects/when-music-meets-datascience/analyzing-favorite-artists/Tyler-Analysis.ipynb)

I analyzed Tyler, the creator's music discography to see how his music varied for every album. This helped me to find - which album is more energetic, which one is more danceable
and many other cool insights. I repeated the same analysis for "Black Sabbath" too.

### Whatsapp group chat analysis
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/Side-Projects/tree/main/mini-projects/whatsapp-group-chat-analysis)

In this fun project, I decided to try my hands on text data for the 1st time. 
I analysed the text data from a whatsapp group of my friends! I performed some basic cleaning 
and then analysis. Whatsapp has an option export the chat into .txt file! I used that to extract the group chat messages!

## Unsupervised Problems

### Clustering songs based on features
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/Side-Projects/tree/main/mini-projects/when-music-meets-datascience/clustering-songs-based-on-features)

The goal of this to automatically divide a whole playlist of songs into to different playlists of 
different moods/features like - energetic songs and relaxing songs! I extracted the whole discography 
of my favorite arists into a csv file using Spotipy, used KMeans algorithm to cluster all the songs of an artist into two clusters - Relaxing and Energetic 
using 3 features - Energy, Danceability and Loudness. And then I added the clusters back to my spotify library as seperate playlists.

## Recommendation systems

### Simple Content-Based Song Recommender
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/jithendrabsy/Side-Projects/blob/main/mini-projects/when-music-meets-datascience/songs-recommender/recommender.ipynb)
There are several approaches to build such systems and one of them is Content-Based approach. This notebook demonstrates a simple
content-based recommendation for songs.

## Kaggle Kernels

- [Supervised learning with PyCaret](https://www.kaggle.com/saiyan6174/supervised-learning-with-pycaret)
PyCaret is an open source, low-code machine learning library in Python that allows you to go from 
preparing your data to deploying your model within seconds in your choice of notebook environment.
This notebook contains a simple classification problem and a simple regression problem which I used to explore PyCaret library.

- [Implementation of simple GAN](https://www.kaggle.com/saiyan6174/implementing-a-gan)
In this notebook, I implemented a basic GAN using PyTorch. This notebook is based on my blog post - [Understanding Generative Adversarial Networks](https://jithendrabsy.github.io/Understanding-Generative-Adversarial-Networks/). 

- [Eminem lyric analysis + Generation](https://www.kaggle.com/saiyan6174/eminem-lyric-analysis-generation)

- [Mechanisms of Action (MoA) competition - EDA](https://www.kaggle.com/saiyan6174/mechanisms-of-action-moa-eda)

- [EDA & Predicting chance of MS Admission](https://www.kaggle.com/saiyan6174/eda-predicting-chance-of-ms-admission)

- [EDA on Top Spotify songs](https://www.kaggle.com/saiyan6174/eda-on-top-spotify-songs)
