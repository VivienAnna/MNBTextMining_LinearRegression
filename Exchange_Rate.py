import csv
import pandas as pd

Bux=[]
Mol=[]
Otp=[]
Richter=[]
ratio=[]

# Read files
def readFile(file, list):
    with open(file, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        for i in reader:
            list.append(i)

readFile('DownloadedFiles/Mol.csv', Mol)
readFile('DownloadedFiles/Otp.csv', Otp)
readFile('DownloadedFiles/Richter.csv', Richter)
readFile('DownloadedFiles/Bux.csv', Bux)
readFile('Ratios/ratio.csv', ratio)

Bux_result=[]
Mol_result=[]
Otp_result=[]
Richter_result=[]

if Bux:
    Bux_result.append([Bux[0]['Dátum'], 1])

for index, current in enumerate(Bux[:-1]):
    if index==0:
        continue
    previous=Bux[index - 1]
    value= float(current['Utolsó ár']) / float(previous['Utolsó ár'])
    Bux_result.append([current['Dátum'], value])
print(Bux_result)
bux_df=pd.DataFrame(Bux_result, columns=['Dátum', 'Price'])
bux_df.to_csv('Numbers/Bux_ratio_number.csv', sep=';', index=False)


if Mol:
    Mol_result.append([Mol[0]['Dátum'], 1])

for index, current in enumerate(Mol[:-1]):
    if index==0:
        continue
    previous=Mol[index - 1]
    value= float(current['Utolsó ár']) / float(previous['Utolsó ár'])
    Mol_result.append([current['Dátum'], value])
print(Mol_result)
mol_df=pd.DataFrame(Mol_result, columns=['Dátum', 'Price'])
mol_df.to_csv('Numbers/Mol_ratio_number.csv', sep=';', index=False)

if Otp:
    Otp_result.append([Otp[0]['Dátum'], 1])

for index, current in enumerate(Otp[:-1]):
    if index==0:
        continue
    previous=Otp[index - 1]
    value= float(current['Utolsó ár']) / float(previous['Utolsó ár'])
    Otp_result.append([current['Dátum'], value])
print(Otp_result)
otp_df=pd.DataFrame(Otp_result, columns=['Dátum', 'Price'])
otp_df.to_csv('Numbers/Otp_ratio_number.csv', sep=';', index=False)

if Richter:
    Richter_result.append([Richter[0]['Dátum'], 1])

for index, current in enumerate(Richter[:-1]):
    if index==0:
        continue
    previous=Richter[index - 1]
    value= float(current['Utolsó ár']) / float(previous['Utolsó ár'])
    Richter_result.append([current['Dátum'], value])
print(Richter_result)
richter_df=pd.DataFrame(Richter_result, columns=['Dátum', 'Price'])
richter_df.to_csv('Numbers/Richter_ratio_number.csv', sep=';', index=False)


