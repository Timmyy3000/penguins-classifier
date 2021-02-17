
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv('penguins_cleaned.csv')

df = data.copy()

target = 'species'
encode = ['sex', 'island']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]

target_mapper = { 'Adelie' : 0, 'Chinstrap' : 1, 'Gentoo' : 2}
def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

#Separating X and Y

X = df.drop('species', axis=1)
Y = df['species']

#Build  a forest model
clf = RandomForestClassifier()
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
clf.fit(x_train, y_train)

acc = clf.score(x_test, y_test) * 100;

print(acc)

pickle.dump(clf, open('penguins_clf.pkl', 'wb'))

