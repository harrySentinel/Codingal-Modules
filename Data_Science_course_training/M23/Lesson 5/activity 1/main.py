import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import KFold

df = pd.read_csv('MARUTI.NS.csv')

user_y = input("What you want to predict?\n1. Open\n2. High\n3. Low\n4. Close\n5. RSI(Buy/Sell)\nInput: ")
user_interval = int(input("Number of interval in which you want data to predict: "))

y = df.loc[user_interval:, user_y]
y.index = np.arange(0, len(y))
x = df.drop(['Date', user_y], axis=1).iloc[:-user_interval, :]

train_accuracy = []
test_accuracy = []
train_rsme = []
test_rsme = []
kfolds = []
kfold_accuracy = []

def accuracy_score(y_train, y_pred_train, y_test, y_pred_test):
    print("Accuracy in Training: ", r2_score(y_train, y_pred_train) * 100)
    train_accuracy.append(r2_score(y_train, y_pred_train) * 100)
    print("Accuracy in Testing: ", r2_score(y_test, y_pred_test) * 100)
    test_accuracy.append(r2_score(y_test, y_pred_test) * 100)

def rsmse(y_train, y_pred_train, y_test, y_pred_test):
    rsmse_test = mean_squared_error(y_test, y_pred_test, squared=False)
    rsmse_train = mean_squared_error(y_train, y_pred_train, squared=False)
    train_rsme.append(rsmse_train)
    test_rsme.append(rsmse_test)
    print("RSME Train: ", rsmse_train)
    print("RSME Test: ", rsmse_test)

def k_fold(algo, kx, ky, cv):
    kf = KFold(n_splits=cv, random_state=None, shuffle=True)
    kfolds.append(cv)
    scores = []
    model = algo
    for train_index, test_index in kf.split(kx):
        X_train = kx.iloc[train_index]
        X_test = kx.iloc[test_index]
        Y_train = ky[train_index]
        Y_test = ky[test_index]
        model.fit(X_train, np.ravel(Y_train))
        Y_pred_train = model.predict(X_train)
        scores.append(r2_score(Y_train, Y_pred_train))
    print("Accuracy: {}".format(np.mean(scores) * 100))
    kfold_accuracy.append(np.mean(scores) * 100)
