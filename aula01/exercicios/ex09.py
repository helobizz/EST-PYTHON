import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Lista": [78, 56, 32, 2, 83, 74, 97, 3, 18, 5],
    "Lista2": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(dados)

# uso de len()
print(len(df["Lista"]))
# uso de sum()
print(sum(df["Lista"]))
# uso de max()
print(max(df["Lista"]))
# uso de min()
print(min(df["Lista"]))
# uso de head()
print(df.head())
# uso de info()
df.info()
# uso de describe()
print(df.describe())
# grafico
plt.bar(
    df["Lista"], df["Lista2"]
)
plt.show()