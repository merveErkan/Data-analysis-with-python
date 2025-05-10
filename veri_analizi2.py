import pandas as pd
import matplotlib.pyplot as plt

# 1. Veriyi yükle
df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")

# 2. Sütun adlarını sadeleştir
df.columns = ["Index", "Height", "Weight"]

# 3. İlk 5 satırı yazdır
print("İlk 5 satır:\n", df.head())

# 4. Boyu kategorilere ayır (Short - Medium - Tall)
bins = [0, 65, 70, 75]
labels = ["Short", "Medium", "Tall"]
df["HeightGroup"] = pd.cut(df["Height"], bins=bins, labels=labels)

# 5. Her boy grubunun ortalama kilosunu yazdır
print("\nBoy gruplarına göre ortalama kilo:")
print(df.groupby("HeightGroup")["Weight"].mean())

# 6. Hem kişi sayısı hem ortalama kilo
summary = df.groupby("HeightGroup").agg(
    Count=("Weight", "count"),
    AverageWeight=("Weight", "mean")
)

print("\nBoy Grubu Özeti:")
print(summary)

# 7. Grafik: Boy grubuna göre ortalama kilo
summary["AverageWeight"].plot(kind="bar", color="skyblue")

# 8. Grafik detayları
plt.title("Boy Gruplarına Göre Ortalama Kilo")
plt.xlabel("Boy Grubu")
plt.ylabel("Ortalama Kilo (lb)")
plt.grid(True)
plt.tight_layout()
plt.show()
