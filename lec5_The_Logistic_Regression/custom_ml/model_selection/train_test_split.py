from sklearn.utils import shuffle
import numpy as np 

__all__ = ["train_test_split"]

def train_test_split(X, y, percent = .15):
    X, y = shuffle(X, y)
    split_index = np.int(np.round(X.shape[0])*percent)
    X_train, y_train = X[:8], y[:8]
    X_test, y_test = X[-8:], y[-8:]

    return X_train, y_train, X_test, y_test