# EDA and predicting chance of admission for MS applications

#### Note: Interactive plots were plotted using Plotly but sadly - It is not possible to view plotly charts on github. So, have a look into my kaggle for detailed notebook. 

#### Link -> [Kernel](https://www.kaggle.com/saiyan6174/eda-predicting-chance-of-ms-admission)

It’s almost admission season for 2017 UG Batch. I’ve got a couple of friends who are preparing for GRE. This made me to try What is their chance of admit and how it may vary with other parameters?

While searching for the dataset, I found this [paper](https://ieeexplore.ieee.org/document/8862140) which compared different Regression models for Prediction of Graduate Admissions.

In this notebook, I used the dataset mentioned in the [paper](https://ieeexplore.ieee.org/document/8862140) and tried to predict the chance of admit based on different parameters. Before modeling and predicting, I performed Eploratory Data Analysis on the data to get some insights on MS admissions. In this notebook, I presented Machine Learning based method and tried to fit the data with perfect model to predict the chance of admit. I used PyCaret for modeling.

The dataset contains several parameters which are considered important during the application for Masters Programs. The parameters included are :

- GRE Score ( out of 340 )
- TOEFL Score ( out of 120 )
- University Rating ( out of 5 )
- Statement of Purpose Strength ( out of 5 )
- Letter of Recommendation Strength (out of 5)
- Undergraduate GPA ( out of 10 )
- Research Experience ( either 0 or 1 )
- Chance of Admit ( ranging from 0 to 1 )
