import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

house = { "Ravenclaw": 1, "Slytherin": 2, "Gryffindor": 3, "Hufflepuff": 4 }
house_rev = { value: key for key, value in house.items() }

def display_data(x, y, house, df, f1, f2):
	plt.figure()
	# A REFAIRE
	pos , neg = (y==1).reshape(len(x[:,0]),1) , (y==0).reshape(len(x[:,1]),1)
	plt.scatter(x[pos[:,0],0],x[pos[:,0],1],c="r",marker="+")
	plt.scatter(x[neg[:,0],0],x[neg[:,0],1],marker="o",s=10)
	# /A REFAIRE
	plt.xlabel(df.columns[f1])
	plt.ylabel(df.columns[f2])
	plt.legend([house, "Not" + house],loc=0)
	plt.show()

def display_standardize(x, y, house, df, f1, f2, theta):
	plt.figure()
	# A REFAIRE
	pos , neg = (y==1).reshape(len(x[:,0]),1) , (y==0).reshape(len(x[:,2]),1)
	plt.scatter(x[pos[:,0],1],x[pos[:,0],2],c="r",marker="+")
	plt.scatter(x[neg[:,0],1],x[neg[:,0],2],marker="o",s=10)
	# /A REFAIRE
	x_value = np.array([np.min(x[:,1]),np.max(x[:,1])])
	y_value = -(theta[0] + theta[1]*x_value)/theta[2]
	plt.xlabel(df.columns[f1])
	plt.ylabel(df.columns[f2])
	plt.legend([house, "Not" + house],loc=0)
	plt.plot(x_value, y_value, "g")
	plt.show()

def display_cost(error_history):
	plt.figure()
	plt.plot(range(len(error_history)), error_history)
	plt.ylabel("Cost")
	plt.xlabel("Iteration")
	plt.title("Cost function graph")
	plt.show

def get_data():
	try:
		data_path = sys.argv[1]
		return (pd.read_csv(data_path))
	except IndexError:
		print("usage: python describe.py [your_dataset].csv")
		sys.exit(-1)
	except IOError:
		print("could not read data file")
		sys.exit(-1)

def filter_data(data, house, f1, f2):
	x = []
	y = []
	data = data.to_numpy()
	for row in data:
		if not np.isnan(row[f1]) and not np.isnan(row[f2]):
			x.append([row[f1], row[f2]])
			y.append(1 if row[0] == house else 0)
	return np.array(x), np.array(y)

def sigmoid(z):
	return(1 / (1 + np.exp(-z)))

def create_csv(row_list, name):
	with open(name, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(row_list)