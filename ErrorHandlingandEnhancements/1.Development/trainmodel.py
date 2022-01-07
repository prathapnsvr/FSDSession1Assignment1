import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import sys,os

sys.path.append(r"C:\Users\sn27506\Learnings\FSDSession1Assignment1\ErrorHandlingandEnhancements")

from common_util.config import *
from common_util.features import *

# Load the csv file
df = pd.read_csv(datapath)

# Select independent and dependent variable
X = df[rawfields]
y = df[target]

 #Call Feature engineering function from feature.py
X['log_Peatal_Width'] = process(X['Petal_Width'])


# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testsize, random_state=randomstate)

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(X_train, y_train)

# Make pickle file of our model
pickle.dump(classifier, open(modeloutput, "wb"))

#Load the saved model
model = pickle.load(open(modeloutput, "rb"))

#Predictions
output = model.predict(X_test)