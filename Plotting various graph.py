import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
gas = pd.read_csv(r"D:\Data set\gas_prices.csv")
#print(gas)
#Line graph:
plt.title('Gas Prices over Time (in USD)')
plt.plot(gas.Year, gas.USA, label = 'United States')
plt.plot(gas['Year'], gas.Canada,label = 'Canada')
plt.plot(gas['Year'], gas['South Korea'], label = 'South Korea')
plt.legend()
plt.show()
