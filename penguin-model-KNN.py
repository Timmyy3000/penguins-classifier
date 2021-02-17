import streamlit as st
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('penguins_cleaned.csv')
isTrained = False


# Machine Learning part

le = preprocessing.LabelEncoder()
y_raw = data[["species"]].values

Y = le.fit_transform(y_raw)

island_values = data[['island']].values
island_encoded = pd.DataFrame(le.fit_transform(island_values))

sex_values = data[['sex']].values
sex_encoded = pd.DataFrame(le.fit_transform(sex_values))

X = pd.concat([pd.DataFrame(data[["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]].values), island_encoded, sex_encoded], axis=1)
print(X)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
classifier = KNeighborsClassifier(n_neighbors=9)


classifier.fit(x_train, y_train)
acc = classifier.score(x_test, y_test) * 100
print(acc)

#prediction = classifier.predict(input)





