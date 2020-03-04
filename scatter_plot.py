import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions import separation_check


def scatter_plot(data1, data2, legend, xlabel, ylabel, separation):
	plt.scatter(data1[:separation[0]], data2[:separation[0]], color='green', alpha=0.5)
	plt.scatter(data1[separation[0]:separation[1]], data2[separation[0]:separation[1]], color='blue', alpha=0.5)
	plt.scatter(data1[separation[1]:separation[2]], data2[separation[1]:separation[2]], color='yellow', alpha=0.5)
	plt.scatter(data1[separation[2]:], data2[separation[2]:], color='red', alpha=0.5)
	plt.legend(legend)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.show()

if __name__ == '__main__':
	houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
	file = pd.read_csv("resources/dataset_train.csv")
	file = file.sort_values(by=['Hogwarts House'])
	separation = [0] * 4
	j = 0
	for i in houses :
		separation[j] += separation_check(i, file, separation[j - 1 if j > 0 else j ])
		j += 1
	file = file.select_dtypes(include="number")
	test = np.array(file)
	data1 = test[:, 2]
	data2 = test[:, 4]
	scatter_plot(data1, data2, houses, file.columns[2], file.columns[4], separation)
