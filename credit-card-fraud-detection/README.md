# credit-card-fraud-detection

#### Goal:
To identify fraud transactions

#### Dataset:
Found on kaggle - [here](https://www.kaggle.com/mlg-ulb/creditcardfraud)

The dataset contains transactions made by credit cards in September 2013 by european cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.


#### Results:

**Random Forest:**

- Accuracy: 0.9996488887328394
- Precision: 0.9868421052631579
- Recall: 0.7978723404255319
- F2: 0.8296460176991151


**SMOTE + RF:**

- Accuracy: 0.9996137776061234
- Precision: 0.9390243902439024
- Recall: 0.8191489361702128
- F2: 0.8406113537117905

**RF-GridSearch:**

- Accuracy: 0.9996137776061234
- Precision: 0.9736842105263158
- Recall: 0.7872340425531915
- F2: 0.8185840707964602

**SMOTE + RF-GridSearch:**

- Accuracy: 0.9996137776061234
- Precision: 0.9186046511627907
- Recall: 0.8404255319148937
- F2: 0.8549783549783551

**Best Model:**

GridSearched RandomForest CLassifier with SMOTE is giving the best F2 score out of all others
RF-GridSearch + SMOTE -> f2 score is 0.85
