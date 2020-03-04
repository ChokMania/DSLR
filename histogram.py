# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:05:10 2020

@author: julien.dumay
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functions import separation_check

def histogram(data, houses, title, xlabel, ylabel, separation):
	h = data[:separation[0]]
	h = h[~np.isnan(h)]
	plt.hist(h, color='green', alpha=0.5)
	h = data[separation[0]:separation[1]]
	h = h[~np.isnan(h)]
	plt.hist(h, color='blue', alpha=0.5)
	h = data[separation[1]:separation[2]]
	h = h[~np.isnan(h)]
	plt.hist(h, color='yellow', alpha=0.5)
	h = data[separation[2]:]
	h = h[~np.isnan(h)]
	plt.hist(h, color='red', alpha=0.5)
	plt.legend(houses)
	plt.title(title)
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
	test = np.array(file.select_dtypes(include="number"))
	data = test[:,11]
	histogram(data, houses, 'Care of Magical Creatures', 'Marks', 'Number of student', separation)