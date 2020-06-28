import numpy as np
import pandas as pd
import random

# test comment
df = pd.read_csv("Trifonov bank.csv")

df_Gstars = pd.DataFrame()
df_sample = pd.DataFrame()

for i in range(len(df.index)):
    if "G" in str(df["Sp. Type"].iloc[i]):
        df_Gstars = df_Gstars.append(df.iloc[i])

df_Gstars.to_csv("G-Type Stars in Trifonov Bank.csv")

sample_list = [random.randint(0, len(df_Gstars.index)) for x in range(50)]

df_sample = pd.concat([pd.DataFrame([df_Gstars.iloc[i]]) for i in sample_list],
          ignore_index=True)

print(df_sample)

df_sample.to_csv("Sample set from Trifonov Bank.csv")


