import seaborn as sbn
import matplotlib.pyplot as plt
import pandas as pd
# loading the dataset using the seaborn library
dataset = pd.read_csv('Data.csv')
data = dataset.copy()
d = data.head(15)
print(d)
sbn.displot(d['Money'])
plt.show()
