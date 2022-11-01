import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
gas = pd.read_csv(r"D:\Data set\gas_prices.csv")
print(gas)
#Line graph:
plt.figure(figsize=(8,5))
plt.title('Gas Prices over Time (in USD)', fontdict={'fontweight':'bold','fontsize':20})
plt.plot(gas.Year, gas.USA, label = 'United States', c = 'r', marker = '.')
plt.plot(gas['Year'], gas.Canada,label = 'Canada', c ='b', marker = 'o')
plt.plot(gas['Year'], gas['South Korea'], label = 'South Korea', c ='yellow', marker = '*')
plt.plot(gas['Year'], gas['Australia'], label = 'Australia', c ='green', marker = 's')
#Another way to plot many values!
countries = ['Australia','Canada','USA','South Korea']
for country in gas:
    if country != 'Year':
    if country in countries:
        plt.plot(gas.Year, gas[country], marker='.', label = country)
        print(country)

print(gas.Year[::3])
plt.xticks(gas.Year[::3].tolist()+[2011])
print(gas.Year)
plt.xlabel('Year')
plt.ylabel('US Dollars')
plt.legend()
plt.show()
