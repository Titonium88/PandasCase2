#место для твоего кода
import pandas as pd
from numpy import nan
import matplotlib.pyplot as plt
df = pd.read_csv('countries of the world.csv')
#print(df.info())
#Hypothesis1: Asia имеет наибольшую суммарную площадь
'''
df2 = df.groupby(by = 'Region')['Area (sq. mi.)'].agg(sum)
df2.plot(kind = 'barh',grid = True, figsize = (12,5))
'''
#Гипотеза Неверна
#Hypothesis2:чем больше Arable % тем больше Birthrate

def float_converter(x):
    if type(x) == str:
        x = x.replace(",",".")
    return float(x)

df = df.fillna(-1)


df['Arable (%)'] = df['Arable (%)'].apply(float_converter)
df['Birthrate'] = df['Birthrate'].apply(float_converter) 

df.plot(x = 'Arable (%)', y ='Birthrate', kind = "scatter")

#График не показал связи


plt.tight_layout()

plt.show()