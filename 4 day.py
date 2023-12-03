import csv
import pandas as pd

Bux=[]
Mol=[]
Otp=[]
Richter=[]
ratio=[]

def readFile(file, list):
    with open(file, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        for i in reader:
            list.append(i)

readFile('Numbers/Bux_ratio_number.csv', Bux)
readFile('Numbers/Mol_ratio_number.csv', Mol)
readFile('Numbers/Otp_ratio_number.csv', Otp)
readFile('Numbers/Richter_ratio_number.csv', Richter)
readFile('Ratios/ratio.csv', ratio)

Bux_result=[]
Mol_result=[]
Otp_result=[]
Richter_result=[]

# Aznap
def exchange_rate_ratio(list, result):
    for i in ratio:
        tmp = [element for element in list if element['Dátum'] == i['Date']]
        tmp2 = list[list.index(tmp[0])]
        # value = float(tmp2['Utolsó ár']) / float(tmp[0]['Utolsó ár'])
        result.append([i['Date'], tmp2["Price"]])
    return result

exchange_rate_ratio(Bux, Bux_result)
exchange_rate_ratio(Mol, Mol_result)
exchange_rate_ratio(Otp, Otp_result)
exchange_rate_ratio(Richter, Richter_result)

# Print results
print("MOL: ", Mol_result)
print("OTP: ", Otp_result)
print("RICHTER: ", Richter_result)
print("BUX: ", Bux_result)

# Write results to csv
my_df = pd.DataFrame(Mol_result)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Mol_ratio_0.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Otp_result)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Otp_ratio_0.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Richter_result)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Richter_ratio_0.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Bux_result)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Bux_ratio_0.csv', index=False, header=True, encoding='utf-8', sep=';')

# Plusz egy nap
Bux_result_1=[]
Mol_result_1=[]
Otp_result_1=[]
Richter_result_1=[]

def exchange_rate_ratio(list, result):
    for i in ratio:
        tmp = [element for element in list if element['Dátum'] == i['Date']]
        tmp2 = list[list.index(tmp[0]) +1]
        # value = float(tmp2['Utolsó ár']) / float(tmp[0]['Utolsó ár'])
        result.append([i['Date'], tmp2['Price']])
    return result

exchange_rate_ratio(Bux, Bux_result_1)
exchange_rate_ratio(Mol, Mol_result_1)
exchange_rate_ratio(Otp, Otp_result_1)
exchange_rate_ratio(Richter, Richter_result_1)

# Print results
print("MOL: ", Mol_result_1)
print("OTP: ", Otp_result_1)
print("RICHTER: ", Richter_result_1)
print("BUX: ", Bux_result_1)

# Write results to csv
my_df = pd.DataFrame(Mol_result_1)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Mol_ratio_1.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Otp_result_1)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Otp_ratio_1.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Richter_result_1)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Richter_ratio_1.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Bux_result_1)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Bux_ratio_1.csv', index=False, header=True, encoding='utf-8', sep=';')

# Plusz kettő nap
Bux_result_2=[]
Mol_result_2=[]
Otp_result_2=[]
Richter_result_2=[]

def exchange_rate_ratio(list, result):
    for i in ratio:
        tmp = [element for element in list if element['Dátum'] == i['Date']]
        tmp2 = list[list.index(tmp[0]) +2]
        # value = float(tmp2['Utolsó ár']) / float(tmp[0]['Utolsó ár'])
        result.append([i['Date'], tmp2['Price']])
    return result

exchange_rate_ratio(Bux, Bux_result_2)
exchange_rate_ratio(Mol, Mol_result_2)
exchange_rate_ratio(Otp, Otp_result_2)
exchange_rate_ratio(Richter, Richter_result_2)

# Print results
print("MOL: ", Mol_result_2)
print("OTP: ", Otp_result_2)
print("RICHTER: ", Richter_result_2)
print("BUX: ", Bux_result_2)

# Write results to csv
my_df = pd.DataFrame(Mol_result_2)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Mol_ratio_2.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Otp_result_2)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Otp_ratio_2.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Richter_result_2)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Richter_ratio_2.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Bux_result_2)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Bux_ratio_2.csv', index=False, header=True, encoding='utf-8', sep=';')

# Plusz három nap

Bux_result_3=[]
Mol_result_3=[]
Otp_result_3=[]
Richter_result_3=[]

def exchange_rate_ratio(list, result):
    for i in ratio:
        tmp = [element for element in list if element['Dátum'] == i['Date']]
        tmp2 = list[list.index(tmp[0]) +3]
        # value = float(tmp2['Utolsó ár']) / float(tmp[0]['Utolsó ár'])
        result.append([i['Date'], tmp2['Price']])
    return result

exchange_rate_ratio(Bux, Bux_result_3)
exchange_rate_ratio(Mol, Mol_result_3)
exchange_rate_ratio(Otp, Otp_result_3)
exchange_rate_ratio(Richter, Richter_result_3)

# Print results
print("MOL: ", Mol_result_3)
print("OTP: ", Otp_result_3)
print("RICHTER: ", Richter_result_3)
print("BUX: ", Bux_result_3)

# Write results to csv
my_df = pd.DataFrame(Mol_result_3)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Mol_ratio_3.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Otp_result_3)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Otp_ratio_3.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Richter_result_3)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Richter_ratio_3.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Bux_result_3)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Bux_ratio_3.csv', index=False, header=True, encoding='utf-8', sep=';')

# Plusz négy nap

Bux_result_4=[]
Mol_result_4=[]
Otp_result_4=[]
Richter_result_4=[]
def exchange_rate_ratio(list, result):
    for i in ratio:
        tmp = [element for element in list if element['Dátum'] == i['Date']]
        tmp2 = list[list.index(tmp[0]) +4]
        # value = float(tmp2['Utolsó ár']) / float(tmp[0]['Utolsó ár'])
        result.append([i['Date'], tmp2['Price']])
    return result

exchange_rate_ratio(Bux, Bux_result_4)
exchange_rate_ratio(Mol, Mol_result_4)
exchange_rate_ratio(Otp, Otp_result_4)
exchange_rate_ratio(Richter, Richter_result_4)

# Print results
print("MOL: ", Mol_result_4)
print("OTP: ", Otp_result_4)
print("RICHTER: ", Richter_result_4)
print("BUX: ", Bux_result_4)

# Write results to csv
my_df = pd.DataFrame(Mol_result_4)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Mol_ratio_4.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Otp_result_4)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Otp_ratio_4.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Richter_result_4)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Richter_ratio_4.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Bux_result_4)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Bux_ratio_4.csv', index=False, header=True, encoding='utf-8', sep=';')

# Mínusz egy nap

Bux_result_neg_1=[]
Mol_result_neg_1=[]
Otp_result_neg_1=[]
Richter_result_neg_1=[]
def exchange_rate_ratio(list, result):
    for i in ratio:
        tmp = [element for element in list if element['Dátum'] == i['Date']]
        tmp2 = list[list.index(tmp[0]) -1]
        # value = float(tmp2['Utolsó ár']) / float(tmp[0]['Utolsó ár'])
        result.append([i['Date'], tmp2['Price']])
    return result

exchange_rate_ratio(Bux, Bux_result_neg_1)
exchange_rate_ratio(Mol, Mol_result_neg_1)
exchange_rate_ratio(Otp, Otp_result_neg_1)
exchange_rate_ratio(Richter, Richter_result_neg_1)

# Print results
print("MOL: ", Mol_result_neg_1)
print("OTP: ", Otp_result_neg_1)
print("RICHTER: ", Richter_result_neg_1)
print("BUX: ", Bux_result_neg_1)

# Write results to csv
my_df = pd.DataFrame(Mol_result_neg_1)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Mol_ratio_neg_1.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Otp_result_neg_1)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Otp_ratio_neg_1.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Richter_result_neg_1)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Richter_ratio_neg_1.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Bux_result_neg_1)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Bux_ratio_neg_1.csv', index=False, header=True, encoding='utf-8', sep=';')

# Mínusz kettő nap

Bux_result_neg_2=[]
Mol_result_neg_2=[]
Otp_result_neg_2=[]
Richter_result_neg_2=[]

def exchange_rate_ratio(list, result):
    for i in ratio:
        tmp = [element for element in list if element['Dátum'] == i['Date']]
        tmp2 = list[list.index(tmp[0]) -2]
        # value = float(tmp2['Utolsó ár']) / float(tmp[0]['Utolsó ár'])
        result.append([i['Date'], tmp2['Price']])
    return result

exchange_rate_ratio(Bux, Bux_result_neg_2)
exchange_rate_ratio(Mol, Mol_result_neg_2)
exchange_rate_ratio(Otp, Otp_result_neg_2)
exchange_rate_ratio(Richter, Richter_result_neg_2)

# Print results
print("MOL: ", Mol_result_neg_2)
print("OTP: ", Otp_result_neg_2)
print("RICHTER: ", Richter_result_neg_2)
print("BUX: ", Bux_result_neg_2)

# Write results to csv
my_df = pd.DataFrame(Mol_result_neg_2)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Mol_ratio_neg_2.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Otp_result_neg_2)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Otp_ratio_neg_2.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Richter_result_neg_2)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Richter_ratio_neg_2.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Bux_result_neg_2)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Bux_ratio_neg_2.csv', index=False, header=True, encoding='utf-8', sep=';')

# Mínusz három nap

Bux_result_neg_3=[]
Mol_result_neg_3=[]
Otp_result_neg_3=[]
Richter_result_neg_3=[]

def exchange_rate_ratio(list, result):
    for i in ratio:
        tmp = [element for element in list if element['Dátum'] == i['Date']]
        tmp2 = list[list.index(tmp[0]) -3]
        # value = float(tmp2['Utolsó ár']) / float(tmp[0]['Utolsó ár'])
        result.append([i['Date'], tmp2['Price']])
    return result

exchange_rate_ratio(Bux, Bux_result_neg_3)
exchange_rate_ratio(Mol, Mol_result_neg_3)
exchange_rate_ratio(Otp, Otp_result_neg_3)
exchange_rate_ratio(Richter, Richter_result_neg_3)

# Print results
print("MOL: ", Mol_result_neg_3)
print("OTP: ", Otp_result_neg_3)
print("RICHTER: ", Richter_result_neg_3)
print("BUX: ", Bux_result_neg_3)

# Write results to csv
my_df = pd.DataFrame(Mol_result_neg_3)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Mol_ratio_neg_3.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Otp_result_neg_3)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Otp_ratio_neg_3.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Richter_result_neg_3)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Richter_ratio_neg_3.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Bux_result_neg_3)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Bux_ratio_neg_3.csv', index=False, header=True, encoding='utf-8', sep=';')

# Mínusz négy nap

Bux_result_neg_4=[]
Mol_result_neg_4=[]
Otp_result_neg_4=[]
Richter_result_neg_4=[]

def exchange_rate_ratio(list, result):
    for i in ratio:
        tmp = [element for element in list if element['Dátum'] == i['Date']]
        tmp2 = list[list.index(tmp[0]) -4]
        # value = float(tmp2['Utolsó ár']) / float(tmp[0]['Utolsó ár'])
        result.append([i['Date'], tmp2['Price']])
    return result

exchange_rate_ratio(Bux, Bux_result_neg_4)
exchange_rate_ratio(Mol, Mol_result_neg_4)
exchange_rate_ratio(Otp, Otp_result_neg_4)
exchange_rate_ratio(Richter, Richter_result_neg_4)

# Print results
print("MOL: ", Mol_result_neg_4)
print("OTP: ", Otp_result_neg_4)
print("RICHTER: ", Richter_result_neg_4)
print("BUX: ", Bux_result_neg_4)

# Write results to csv
my_df = pd.DataFrame(Mol_result_neg_4)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Mol_ratio_neg_4.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Otp_result_neg_4)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Otp_ratio_neg_4.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Richter_result_neg_4)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Richter_ratio_neg_4.csv', index=False, header=True, encoding='utf-8', sep=';')

my_df = pd.DataFrame(Bux_result_neg_4)
my_df.columns = ['Date', 'rateRatio']
my_df.to_csv('Ratios/Bux_ratio_neg_4.csv', index=False, header=True, encoding='utf-8', sep=';')
