#место для твоего кода
import pandas as pd
from numpy import nan
import matplotlib.pyplot as plt
df = pd.read_csv('countries of the world.csv')
#print(df.info())
#Hypothesis: Asia имеет наибольшую суммарную площадь

df2 = df.groupby(by = 'Region')['Area (sq. mi.)'].agg(sum)
df2.plot(kind = 'barh',grid = True, figsize = (12,5))

plt.tight_layout()

plt.show()

#Гипотеза Неверна