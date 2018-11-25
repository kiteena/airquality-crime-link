from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor


def find_regressor(df, y_values):
    # range of number of estimators was experimentally determined
    param_dist = {"n_estimators": [100, 125, 150, 175, 200, 225, 250, 275, 300],
                  "max_depth": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,None],
                  "min_samples_split":  [2, 4, 6, 8, 10],
                  "bootstrap": [True, False]}
    search_regr=RandomForestRegressor(n_estimators= 100, random_state=42)
    rf_random = RandomizedSearchCV(estimator = search_regr, param_distributions = param_dist, n_iter = 10, cv = 3, verbose=2, random_state=42, n_jobs = -1)
    rf_random.fit(df, y_values)
    return rf_random.best_estimator_


def fit_and_predict(regr, X_train, X_test, y_train, y_test):
    regr.fit(X_train.as_matrix(), y_train)
    return regr.predict(X_test.as_matrix())
