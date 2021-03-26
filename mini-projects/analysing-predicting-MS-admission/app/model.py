##importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

import pickle
import warnings
warnings.filterwarnings('ignore')



# reading the dataset
df = pd.read_csv("/home/jithendra/Documents/projects/zzz.../graduate_admission_prediction/data/Admission_Predict_Ver1.1.csv")
# keeping a copy for backup
data = df.copy()
# dropping the useless columns
data = data.drop('Serial No.',axis=1)

# splitting into train and test dataset
split = StratifiedShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
for train_index, test_index in split.split(data, data["University Rating"]):
    train = data.loc[train_index]
    test = data.loc[test_index]

# seperating the target variable
X_train = train.drop('Chance of Admit ',axis=1)
y_train = train['Chance of Admit '].copy()
X_test = test.drop('Chance of Admit ',axis=1)
y_test = test['Chance of Admit '].copy()
'''
# Scaling
sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)
'''

# Using Ridge regression 
'''
	Various models were compared in "modelling.ipynb" and Ridge Regressor
	turned out to be the best one on the basis of RMSE scores!
'''
# defining the model and fitting over the train set
final_model = Ridge()
final_model.fit(X_train,y_train)


# predciting the test datasets
final_predictions = final_model.predict(X_test)
final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)

#print(final_model.predict([[320,110,4,4,4,9,0]]))


'''
# defining a function that tcovers the entire flow
def predict_chance_of_admit(config, model):
    
    if type(config) == dict:
        df = pd.DataFrame(config)
    else:
        df = config
    
    scaled_df = sc.transform(df)
    y_pred = model.predict(scaled_df)
    return y_pred


# defining a config with my own parameters! (just to check)
config={
    'GRE Score' : [315,320],
    'TOEFL Score' : [105,110],
    'University Rating' : [4,4],
    'SOP' : [4,3.5],
    'LOR ' : [4,3],
    'CGPA' : [9.5,9],
    'Research' : [1,0]
}

# predicting the new values
predict_chance_of_admit(config, final_model)


# saving the model
with open("model.bin", 'wb') as f_out:
    pickle.dump(final_model, f_out)
    f_out.close()

# loading the model from the saved file
with open('model.bin', 'rb') as f_in:
    model = pickle.load(f_in)
    
print(predict_chance_of_admit(config, model))'''

# saving model
pickle.dump(final_model, open('model.pkl','wb'))

# loading mdel
model = pickle.load(open('model.pkl','rb'))
prediction = model.predict([[320,110,4,4,4,9,0]])
output = round(prediction[0], 2)
print(output)


