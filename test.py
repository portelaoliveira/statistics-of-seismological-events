import pandas as pd
import  matplotlib.pyplot as plt

df = pd.read_csv("terremotos_america_sul.csv", usecols=range(1,8), index_col=False)

mag = df[" Magnitude"]
media = mag.mean()
mediana = mag.median()
var = mag.var()

# print(var, media, mediana)

plt.figure(figsize=(12,8))
plt.title("Análise estatistica de terremotos da America do Sul")
plt.plot(mag)
plt.xlabel("Indice")
plt.ylabel("Magnitude")
plt.savefig("mag.png")

plt.figure(figsize=(12,8))
plt.title("Análise estatistica de terremotos da America do Sul")
plt.hist(mag, bins=25)
plt.xlabel("Magnitude")
plt.ylabel("N")
plt.savefig("histograma.png")

plt.figure(figsize=(12,8))
plt.title("Análise estatistica de terremotos da America do Sul")
plt.hist(mag, bins=25, cumulative=True)
plt.xlabel("Magnitude")
plt.ylabel("N")
plt.savefig("histograma_cum.png")

plt.figure(figsize=(12,8))
plt.title("Análise estatistica de terremotos da America do Sul")
plt.boxplot(mag)
plt.ylabel("Magnitude")
plt.savefig("boxplot.png")