import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import beta
from scipy.stats import norm

df = pd.read_csv("C:\\Users\\berna\\Downloads\\supermarketdata\\SuperMarketData.csv")

# df["Rating"].plot(kind="hist", bins=20, edgecolor="black", alpha=0.7)
# plt.xlabel("Rating")
# plt.title("Distribución de Rating")
# plt.show()

print(df.head())

print('Longitud del dataframe: ' + str(len(df)))

ratings = np.array(df["Rating"])

max_rating = max(ratings)
min_rating = min(ratings)
rating_norm = 1/(max_rating - min_rating) * (ratings - min_rating)

a,b,_,_=beta.fit(ratings)
print("alpha y beta:", a,b)

mu_norm = a / (a + b)

var_norm = (a * b) / ((a + b) ** 2 * (a+b+1)) 
desv_norm = np.sqrt(var_norm)

mu = (max_rating - min_rating) * mu_norm + min_rating
var = (max_rating - min_rating) ** 2 * var_norm
sigma = np.sqrt(var)

print("mu normalizada, varianza normalizada:", mu_norm, var_norm)
print("mu, varianza", mu, var)

prob = 1 - norm.cdf(8.5, mu, sigma)
print("Probabilidad de que el promedio de los ratings sea mayor a 8.5:", prob) 