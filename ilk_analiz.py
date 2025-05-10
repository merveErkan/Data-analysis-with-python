import pandas as pd
import matplotlib.pyplot as plt

# Veriyi oku
df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")

# Sütun adlarını düzelt
df.columns = ["Index", "Height", "Weight"]

# Ortalama boy ve kilo
print("Ortalama Boy:", df["Height"].mean())
print("Ortalama Kilo:", df["Weight"].mean())

# Grafik çiz
plt.figure(figsize=(8, 5))
plt.scatter(df["Height"], df["Weight"], color="skyblue", edgecolor="black")
plt.title("Height vs Weight")
plt.xlabel("Height (inches)")
plt.ylabel("Weight (pounds)")
plt.grid(True)
plt.show()
