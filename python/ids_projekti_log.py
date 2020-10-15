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

data = pd.read_csv('flights.csv')
data=data.fillna(0)
         

fit = smf.glm(formula="ARR_DEL15 ~ DISTANCE + DAY_OF_WEEK", data=data,family=sm.families.Binomial()).fit()
print(fit.summary())

def logistic(x):
    return 1.0 / (1.0 + np.exp(-x))

plt.scatter(data.DISTANCE, data.ARR_DEL15,marker="d")
X=np.linspace(1,5500,100)
plt.plot(X, logistic(X*fit.params.DISTANCE + fit.params.Intercept),color="c")
plt.xlabel("distance")
plt.ylabel("delay over 15min")
plt.show()






