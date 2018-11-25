from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def Cross_Validation(data, labels, regr, num_split):
    scores = []
    tss = TimeSeriesSplit(n_splits=num_split)
    for train_index, test_index in tss.split(data):
        if len(data.columns) > 1:
            X_train_split =  data.iloc[train_index, :]
            X_test_split = data.iloc[test_index, :]
        else:
            X_train_split =  data.iloc[train_index]
            X_test_split = data.iloc[test_index]
        y_train_split = labels.iloc[train_index]
        y_test_split = labels.iloc[test_index]
        regr.fit(X_train_split, y_train_split)
        y_pred_split = regr.predict(X_test_split)
        scores.append(MSE(y_test_split, y_pred_split))
    return np.mean(scores)

def R2_Score(y_test, y_pred):
    return r2_score(y_test, y_pred)

def MSE(y_test, y_pred):
    return mean_squared_error(y_test, y_pred)
