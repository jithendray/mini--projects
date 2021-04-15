import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

import warnings
warnings.filterwarnings('ignore')

stocks = pd.read_csv('data/upload_DJIA_table.csv')
news = pd.read_csv('data/Combined_News_DJIA.csv')



news.head(2)

news.shape

stocks.head()

stocks.shape


df = news.merge(stocks, how='inner', on='Date',left_index=True)

df.head(3)

df.shape

# mixing headlines
headlines = []
for row in range(0, len(df.index)):
    headlines.append(' '.join( str(x) for x in df.iloc[row, 2:27]))

# sample headline
headlines[0]

# data cleaning
headlines_clean = []

for i in range(0, len(headlines)):
    headlines_clean.append(re.sub("b[(')]", '', headlines[i])) # removes b'
    headlines_clean[i] = re.sub('b[(")]','',headlines_clean[i]) # removes b"
    headlines_clean[i] = re.sub("\'", '', headlines_clean[i]) # removes \'


headlines_clean[0]


# adding clean_headlines to the df
df['mixed_news'] = headlines_clean

df['mixed_news'][0]

df.head(2)

# subjectivity
def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# polarity
def get_polarity(text):
    return TextBlob(text).sentiment.polarity


# adding subjectivity and polarity to the df
df['Subjectivity'] = df['mixed_news'].apply(get_subjectivity)
df['Polarity'] = df['mixed_news'].apply(get_polarity)


df.head(2)


# sentiment scores
def get_sentiment_scores(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

# each day sentiment scores
compound = []
negative = []
positive = []
neutral = []
SIA = 0

for i in range(0, len(df['mixed_news'])):
    scores = get_sentiment_scores(df['mixed_news'][i])
    compound.append(scores['compound'])
    negative.append(scores['neg'])
    positive.append(scores['pos'])
    neutral.append(scores['neu'])

# sentiment scores in df
df['Compound'] = compound
df['Negative'] = negative
df['Positive'] = positive
df['Neutral'] = neutral

df.head(2)


# columns needed
keep_columns = ['Open','High','Low','Volume','Subjectivity','Polarity','Compound','Negative','Positive','Neutral','Label']

data = df[keep_columns]


data.head()


# prepare data for machine learning
X = np.array(data.drop(['Label'],1))
y = np.array(data['Label'])


# split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)



# logistic regression model
lr = LogisticRegression().fit(X_train, y_train)
lr_predictions = lr.predict(X_test)

# classification report
print(classification_report(y_test, lr_predictions))



# Naive Bayes model
nb = GaussianNB().fit(X_train, y_train)
nb_predictions = nb.predict(X_test)

# classification report
print(classification_report(y_test, nb_predictions))

# Decision Tree model
tree = DecisionTreeClassifier().fit(X_train, y_train)
tree_predictions = tree.predict(X_test)

# classification report
print(classification_report(y_test, tree_predictions))

# Random Forest model
rf = RandomForestClassifier().fit(X_train, y_train)
rf_predictions = rf.predict(X_test)

# classification report
print(classification_report(y_test, rf_predictions))

# LDA model
lda = LinearDiscriminantAnalysis().fit(X_train, y_train)
lda_predictions = lda.predict(X_test)

# classification report
print(classification_report(y_test, lda_predictions))