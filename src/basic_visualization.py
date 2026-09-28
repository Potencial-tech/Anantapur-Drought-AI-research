import pandas as pd
import matplotlib.pyplot as plt

gw = pd.read_csv("data/cgwb_anantapur_groundwater_distribution_2022_2023.csv")
fusion = pd.read_csv("data/exploratory_multimodal_surface_stress.csv")

print(gw)
print(fusion)

plt.figure(figsize=(8,5))
plt.plot(fusion["year"], fusion["exploratory_surface_stress_index"], marker="o")
plt.xlabel("Year")
plt.ylabel("Exploratory surface-stress index")
plt.title("Exploratory multimodal surface-stress index")
plt.tight_layout()
plt.show()
