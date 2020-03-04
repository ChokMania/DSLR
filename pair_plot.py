import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_columns(file) :
	col = []
	for x in file:
		if x != "Index":
			col.append(x)
	return col

if __name__ == "__main__":
	sns.set(style="whitegrid", color_codes=True)
	file = pd.read_csv('resources/dataset_train.csv')
	cols = ["Hogwarts House"] + get_columns(file.select_dtypes(include="number"))
	data = file[cols].dropna()
	sns.pairplot(data, hue="Hogwarts House", palette="husl", markers = ".", size=1)
	plt.show()
