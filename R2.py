import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Simulating the data based on the provided snippet
# Note: The actual values will differ, this is just for demonstration based on the structure

df = pd.read_csv('Ratios/Otp_ratio_4.csv', sep=';')
df5 = pd.read_csv('OTP_TEST/Delta.csv', sep=';')

x= df5[['Delta']]
y=df['rateRatio']

model = LinearRegression()
# Create a DataFrame
model.fit(x, y)

#calculate R-squared of regression model
r_squared = model.score(x, y)

#view R-squared value
print(r_squared)