from operator import truediv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")

type_count=df["Type1"]. value_counts(ascending=True)



plt.barh(type_count.index,type_count.values,color="#0edffc",edgecolor="black")
plt.title("# of pokemon by  primary type")
plt.xlabel("count")
plt.xlabel("type")
plt.tight_layout()


plt.show()