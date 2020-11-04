import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

if __name__ == "__main__":
	sns.set(style="whitegrid", color_codes=True)
	try:
		data = pd.read_csv("resources/dataset_train.csv")
	except:
		sys.exit("Error")
	data.drop('Index', axis=1, inplace=True)
	data = data[["Hogwarts House"] + list(data.select_dtypes(include="number").columns)].dropna()
	sns.pairplot(data, hue="Hogwarts House", palette="husl", markers=".")
	plt.show()
