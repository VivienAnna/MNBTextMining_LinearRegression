import csv
import pandas as pd

ratio=[]
Delta=[]

def readFile(file, list):
    with open(file, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        for i in reader:
            list.append(i)


readFile('Ratios/ratio.csv', ratio)

for i in range(len(ratio)):
    Delta.append([ratio[i]['Date'], float(ratio[i]['Positive'])-float(ratio[i]['Negative'])])

my_df = pd.DataFrame(Delta)
my_df.columns = ['Date', 'Delta']
my_df.to_csv('OTP_TEST/Delta.csv', index=False, header=True, encoding='utf-8', sep=';')
