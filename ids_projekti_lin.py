import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import abline_plot
import pandas as pd
from sklearn.linear_model import LinearRegression

arr_del = pd.read_csv('flights.csv')

fit=smf.ols('ARR_DELAY ~  DISTANCE + DEP_DELAY', arr_del).fit()
print(fit.summary())  
p=fit.params

def biplot(df, x_name, y_name):
    fig, ax = plt.subplots()
    ax.grid(False)
    x = df[x_name]
    y = df[y_name]
    plt.scatter(x,y,c='blue', edgecolors='none',alpha=0.5)
    abline_plot(intercept=p.Intercept, slope=p.DEP_DELAY,ax=plt.gca(),color="brown")
    plt.xlabel("Departure delay")
    plt.ylabel("Arrival delay")
    plt.show()
biplot(arr_del, "DEP_DELAY", "ARR_DELAY")

#qq plot
import pandas as pd
import statsmodels.api as sm
res = fit.resid
fig = sm.qqplot(res)
plt.show()
fit.summary()

    



