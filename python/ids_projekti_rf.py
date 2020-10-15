import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import abline_plot
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import abline_plot
import pandas as pd
from sklearn.model_selection import train_test_split
import math
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


data = pd.read_csv('flights.csv')
data=data.fillna(0)  
train, test = train_test_split(data, test_size=0.2 ,random_state=2)

trainy = train.ARR_DEL15
testy = test.ARR_DEL15


trainx = train.DAY_OF_WEEK.values
testx = test.DAY_OF_WEEK.values
trainx1 = train.DISTANCE.values
testx1 = test.DISTANCE.values


trainx = np.vstack((trainx, trainx1)).T
testx = np.vstack((testx, testx1)).T


trainx = trainx[:10000]
trainy = trainy[:10000]
testx = testx[:10000]
testy=testy[:10000]


rf = RandomForestClassifier()
rf = rf.fit(trainx, trainy)
rf.score(trainx, trainy)

predict = rf.predict(testx)
acc = metrics.accuracy_score(testy, predict)
print(acc)#0.6706


def raf(forest_size):
    rf = RandomForestClassifier(n_estimators=forest_size)
    rf = rf.fit(trainx, trainy)
    predict = rf.predict(testx)
    acc = metrics.accuracy_score(testy, predict)
    return acc

rf_nt_models = []
for i in range(1,20):
    forest_size = i*10
    accuracy = raf(forest_size)
    model = {'size': forest_size, 'accuracy': accuracy}
    rf_nt_models.append(model)
    
nt_rf = pd.DataFrame.from_dict(rf_nt_models)
plt.plot(nt_rf['size'].values, nt_rf['accuracy'].values, 'k')
plt.xlabel("Amount of decision trees")
plt.ylabel("Accuracy")
plt.axis([0, 210, 0.0, 1.0])
plt.show()


