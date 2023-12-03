import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

Delta=pd.read_csv('../OTP_TEST/Delta.csv', sep=';')
OTP=pd.read_csv('../Ratios/Otp_ratio_neg_1.csv', sep=';')

merged_data = pd.merge(Delta, OTP, on='Date')

x=merged_data[['Delta']]
y=merged_data[['rateRatio']]

model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Delta', y='rateRatio', data=merged_data,color='#9fbdd9', label='Valós adatok' )
plt.plot(merged_data['Delta'], y_pred, color='red', label='Lineáris regresszió')
plt.xlabel('Δ=(Positive-Negative)')
plt.ylabel('OTP Rate')
# plt.title('Egy magyarázóváltozós modell az OTP árfoyamának előrejelzésére')
plt.legend()
plt.show()

