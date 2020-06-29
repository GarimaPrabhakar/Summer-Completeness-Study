import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

def basic_stats(name, x):
    print("BASIC STATS:: ", name)
    print("___________________________________")
    print("Mean: ", np.mean(x))
    print("Median: ", np.median(x))

    mode = stats.mode(x)
    print("The modal value is {} with a count of {}".format(mode.mode[0], mode.count[0]))

    print("Range: ", np.ptp(x))
    print("Variance: ", np.var(x))
    print("Range: ", np.std(x))
    print("Standard Deviation: ", stats.sem(x))
    print("___________________________________\n\n")

sns.palplot(sns.diverging_palette(145, 280, s=85, l=25, n=7))
sns.set()

df = pd.read_csv("Sample set from Trifonov Bank.csv")
print(df.columns)

#Fe_H plots
fe_h = df["Fe_H"].to_numpy()
num_bins = 20

basic_stats("FeH", fe_h)

fig, ax = plt.subplots()
n, bins, patches = ax.hist(fe_h, num_bins, rwidth=0.98, edgecolor='black')


ax.set_xlabel('Metallicity (FeH)')
ax.set_ylabel('Count')
ax.set_title(r'Metallicity Distribution of Sample Set')

fig.tight_layout()
plt.show()
plt.savefig("fe_h sample set.png")
plt.close()



#logg plots
logg = df["logg"].to_numpy()

basic_stats("Logg", logg)

num_bins = 20

fig, ax = plt.subplots()
n, bins, patches = ax.hist(logg, num_bins, rwidth=0.98, edgecolor='black')


ax.set_xlabel('logg')
ax.set_ylabel('Count')
ax.set_title(r'logg Distribution of Sample Set')

fig.tight_layout()
plt.show()
plt.savefig("logg sample set.png")
plt.close()



#t_eff plots
teff = df["T_eff [K]"].to_numpy()
num_bins = 20

basic_stats("Effective Temperature", teff)

fig, ax = plt.subplots()
n, bins, patches = ax.hist(teff, num_bins, rwidth=0.98, edgecolor='black')


ax.set_xlabel('Effective Temperature (K)')
ax.set_ylabel('Count')
ax.set_title(r'Effective Temperature Distribution of Sample Set')

fig.tight_layout()
plt.show()
plt.savefig("t_eff sample set.png")
plt.close()




