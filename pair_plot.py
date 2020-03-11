import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tools.utilities import get_data_visual

if __name__ == "__main__":
	sns.set(style="whitegrid", color_codes=True)
	file = get_data_visual("display a a pair_plot", 0)
	file.drop('Index', axis=1, inplace=True)
	data = file[["Hogwarts House"] + list(file.select_dtypes(include="number").columns)].dropna()
	sns.pairplot(data, hue="Hogwarts House", palette="husl", markers = ".")
	plt.show()
