from numpy import ravel
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split


def train_ada_boost(X, y, estimators=3, random_seed=0) -> tuple:
    
    X_test, X_train, y_test, y_train = train_test_split(X, y, random_state=random_seed) 

    adaboost_clf = AdaBoostClassifier(n_estimators=estimators, random_state=random_seed).fit(X_test, ravel(y_test))
    
    return (adaboost_clf, X_train, y_train)
