import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

data = pd.read_csv('Admission_Predict_Ver1.1.csv')
data.drop(['Serial No.'], axis=1, inplace=True)

X = data.drop(['Chance of Admit '], axis=1)
y = data['Chance of Admit ']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)
preds = model.predict(X_test)
print('Score: {}'.format(r2_score(y_test,preds)))

model_file = open('Admission_Prediction.sav','wb')
pickle.dump(model,model_file)