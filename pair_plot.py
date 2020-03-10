import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
	sns.set(style="whitegrid", color_codes=True)
	file = pd.read_csv('resources/dataset_train.csv')
	file.drop('Index', axis=1, inplace=True)
	data = file[["Hogwarts House"] + list(file.select_dtypes(include="number").columns)].dropna()
	sns.pairplot(data, hue="Hogwarts House", palette="husl", markers = ".")
	plt.show()
