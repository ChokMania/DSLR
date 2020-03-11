import matplotlib.pyplot as plt
import numpy as np
from tools.utilities import get_data_visual

houses={
	"Ravenclaw": 1,
	"Slytherin": 2,
	"Gryffindor": 3,
	"Hufflepuff": 4
}

def scatter_plot(data, col_1, col_2):
	col_1 += 2
	col_2 += 2
	plt.figure()
	plt.xlabel(data.columns[col_1])
	plt.ylabel(data.columns[col_2])
	data = data.to_numpy()
	for house in range (1, 5):
		x = []
		y = []
		for row in data:
			if row[1] == house and not np.isnan(row[col_1]) and not np.isnan(row[col_2]):
				x.append(row[col_1])
				y.append(row[col_2])
		plt.scatter(x, y, alpha=0.7, s=9)
	plt.show()

if __name__ == "__main__":
	data = get_data_visual("display a plot", 0)
	data["Hogwarts House"].replace(houses, inplace=True)
	data = data.select_dtypes('number')
	scatter_plot(data, 1, 3)