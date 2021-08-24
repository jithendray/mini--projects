from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.preprocessing.image import img_to_array
from keras.optimizers import SGD
from utils.nn import LeNet
from utils.captchahelper import preprocess
from utils.cnnhelper import plotHistory
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

datasetPath = "dataset"
numEpochs   = 20

data = []
labels = []

# loop over the input images
for imagePath in paths.list_images(datasetPath):
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = preprocess(image, 28, 28)
    image = img_to_array(image)
    data.append(image)

    # extract the class label from the image path and update the labels list
    label = imagePath.split(os.path.sep)[-2]
    labels.append(label)

# scale the raw pixel intensities to the range [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.25, random_state=42)

lb = LabelBinarizer().fit(y_train)
y_train = lb.transform(y_train)
y_test  = lb.transform(y_test)

# initialize
model = LeNet.build(width=28, height=28, depth=1, classes=9)
opt = SGD(lr=0.01)
model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

# train
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=32, epochs=numEpochs, verbose=1)

# evaluate
predictions = model.predict(X_test, batch_size=32)
print(classification_report(y_test.argmax(axis=1),predictions.argmax(axis=1), target_names=lb.classes_))

# save
model.save("lenet.hdf5")
