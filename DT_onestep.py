import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from keras.optimizers import SGD
import seaborn as sns
#%matplotlib inline
import warnings
import mprof
# program to compute the time
# of execution of any python code
from datetime import datetime

from requests.packages import target
from sklearn import svm

warnings.filterwarnings('ignore')
# importing the library
# we initialize the variable start to
# store the starting time of execution
# of program
start = datetime.now()

df = pd.read_csv("C:/Users/as097/Desktop/PVC/tsfelWRM_multi.csv")
#print(df.sample(5))
#print(df.Label.value_counts())

df.drop('0_ECDF Percentile Count_0',axis='columns',inplace=True)
#print(df.dtypes)

X = df.drop('Label1',axis='columns')
y = testLabels = df.Label1.astype(np.float32)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3, random_state=15, stratify=y)
#print(y_train.value_counts())
#print(y.value_counts())
#print(y.value_counts())
#print(len(X_train.columns))

from tensorflow_addons import losses
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import confusion_matrix , classification_report

from memory_profiler import profile
# instantiating the decorator

# code for which memory has to
# be monitored

# instantiating the decorator
@profile
# code for which memory has to
# be monitored

###### Decision Tree Classifier with criterion gini index
def DT(X_train, y_train, X_test, y_test):
    # import DecisionTreeClassifier
    from sklearn.tree import DecisionTreeClassifier
    ##### Decision Tree Classifier with with criterion entropy

    # instantiate the DecisionTreeClassifier model with criterion entropy
    clf_en = DecisionTreeClassifier(criterion='entropy', max_depth=3 , random_state=15)

    # fit the model
    clf_en.fit(X_train, y_train)
    y_preds = clf_en.predict(X_test)
    from sklearn.metrics import accuracy_score
    print('Model accuracy score with criterion entropy: {0:0.4f}'. format(accuracy_score(y_test, y_preds)))

    y_pred_train_en = clf_en.predict(X_train)
    print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train_en)))

    # print the scores on training and test set
    print('Training set score: {:.4f}'.format(clf_en.score(X_train, y_train)))
    print('Test set score: {:.4f}'.format(clf_en.score(X_test, y_test)))


    print("Classification Report: \n", classification_report(y_test, y_preds))
    return y_preds

y_preds = DT(X_train, y_train, X_test, y_test)

 # now we have initialized the variable
# end to store the ending time after
# execution of program
end = datetime.now()
# difference of start and end variables
# gives the time of execution of the
# program in between
print("The time of execution of above program is :",
      str(end-start)[5:])

#if __name__ == '__main__':
    #DT(X_train, y_train, X_test, y_test),
# Importing the library
import time
import multiprocessing as mp
import psutil
import numpy as np
def monitor(target):
    worker_process = mp.Process(target=target)
    worker_process.start()
    p = psutil.Process(worker_process.pid)
    # log cpu usage of `worker_process` every 10 ms
    cpu_percents = []
    while worker_process.is_alive():
        cpu_percents.append(p.cpu_percent())
        time.sleep(0.01)
    worker_process.join()
    return cpu_percents

if __name__ ==  '__main__':
    cpu_percents = monitor(target)
    plt.plot(cpu_percents)
    plt.show()