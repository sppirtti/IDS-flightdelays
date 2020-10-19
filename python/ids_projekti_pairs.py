import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import abline_plot
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns


data = pd.read_csv('flights.csv')


sns.pairplot(
    data,
    y_vars=["ARR_DELAY","DISTANCE", "CARRIER_DELAY","WEATHER_DELAY","NAS_DELAY","SECURITY_DELAY","LATE_AIRCRAFT_DELAY"],
    x_vars=["ARR_DELAY","DISTANCE", "CARRIER_DELAY","WEATHER_DELAY","NAS_DELAY","SECURITY_DELAY","LATE_AIRCRAFT_DELAY"],
    
)
plt.show()
