import pandas as pd
import statsmodels.api as sm
from sklearn import linear_model

# Read data
df_y = pd.read_csv('Ratios/Otp_ratio_neg_1.csv', sep=';')
df_x = pd.read_csv('OTP_TEST/Delta.csv', sep=';')

# Prepare data for regression
x= df_x[['Delta']]

y=df_y['rateRatio']

# Regression

# Add constant
x_with_constant = sm.add_constant(x)

# Model and predictions
# OTP
regr_OTP = linear_model.LinearRegression()
regr_OTP.fit(x, y)

model_OTP = sm.OLS(y, x_with_constant).fit()
predictions_OTP = model_OTP.predict(x_with_constant)

print_model_OTP= model_OTP.summary()

# Store results in a list

results= [print_model_OTP]
stocks= ['OTP']

# Print results
for i in range(len(stocks)):
    print(f"Results for Stock {stocks[i]}:\n{results[i]}\n")

with open('OTP_TEST_eredmenyek.txt', 'w') as f:
    for i in range(len(stocks)):
        f.write(f"Results for Stock {stocks[i]}:\n{results[i]}\n")