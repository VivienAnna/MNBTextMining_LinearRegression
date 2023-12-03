import pandas as pd
import statsmodels.api as sm
from sklearn import linear_model

# Read data
df = pd.read_csv('Ratios/Bux_ratio_neg_1.csv', sep=';')
df2 = pd.read_csv('Ratios/Mol_ratio_1.csv', sep=';')
df3 = pd.read_csv('Ratios/Otp_ratio_neg_1.csv', sep=';')
df4 = pd.read_csv('Ratios/Richter_ratio_neg_1.csv', sep=';')
df5 = pd.read_csv('Ratios/ratio.csv', sep=';')

# Prepare data for regression
x_RATIO= df5[['Positive','Negative']]
y1_BUX=df['rateRatio']
y2_MOL=df2['rateRatio']
y3_OTP=df3['rateRatio']
y4_RICHTER=df4['rateRatio']

# Regression

# BUX
# Create linear regression object
regr_BUX = linear_model.LinearRegression()
# Train the model using the training sets
regr_BUX.fit(x_RATIO, y1_BUX)

# Add constant
x_with_constant = sm.add_constant(x_RATIO)

# Model and predictions
model_BUX = sm.OLS(y1_BUX, x_with_constant).fit()
predictions_BUX = model_BUX.predict(x_with_constant)

print_model_BUX= model_BUX.summary()

# MOL
regr_MOL = linear_model.LinearRegression()
regr_MOL.fit(x_RATIO, y2_MOL)

model_MOL = sm.OLS(y2_MOL, x_with_constant).fit()
predictions_MOL = model_MOL.predict(x_with_constant)

print_model_MOL= model_MOL.summary()

# OTP
regr_OTP = linear_model.LinearRegression()
regr_OTP.fit(x_RATIO, y3_OTP)

model_OTP = sm.OLS(y3_OTP, x_with_constant).fit()
predictions_OTP = model_OTP.predict(x_with_constant)

print_model_OTP= model_OTP.summary()

# Richter
regr_Richter = linear_model.LinearRegression()
regr_Richter.fit(x_RATIO, y4_RICHTER)

model_Richter = sm.OLS(y4_RICHTER, x_with_constant).fit()
predictions_Richter = model_Richter.predict(x_with_constant)

print_model_Richter= model_Richter.summary()

# Store results in a list

results= [print_model_BUX, print_model_MOL, print_model_OTP, print_model_Richter]
stocks= ['BUX', 'MOL', 'OTP', 'Richter']

# Print results
for i in range(len(stocks)):
    print(f"Results for Stock {stocks[i]}:\n{results[i]}\n")

with open('eredmenyek.txt', 'w') as f:
    for i in range(len(stocks)):
        f.write(f"Results for Stock {stocks[i]}:\n{results[i]}\n")