import matplotlib.pyplot as plt
import numpy as np
import describe
from tools.utilities import get_data_visual

houses={
	"Ravenclaw": 1,
	"Slytherin": 2,
	"Gryffindor": 3,
	"Hufflepuff": 4
}

def plot_hist(data, col):
	plt.figure()
	plt.title(data.columns[col])
	data = data.to_numpy()
	for i in range(1, 5):
		curr_house = []	
		for row in data:
			if row[1] == i and not np.isnan(row[col]):
				curr_house.append(row[col])
		plt.hist(curr_house, alpha=0.5)
	plt.show()

if __name__ == "__main__":
	np.set_printoptions(suppress=True)
	data = describe.get_data_visual("display an histogram", 0)
	data["Hogwarts House"].replace(houses, inplace=True)
	data = data.select_dtypes('number')
	metrics = describe.describe(data.to_numpy())
	metrics = metrics.tolist()
	col = metrics[2].index(min(metrics[2]))
	plot_hist(data, col)