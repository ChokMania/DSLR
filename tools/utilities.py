import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import argparse

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
	plt.legend([house, "Not " + house],loc=0)
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
	plt.legend([house, "Not " + house],loc=0)
	plt.plot(x_value, y_value, "g")
	plt.show()

def display_cost(error_history):
	plt.figure()
	plt.plot(range(len(error_history)), error_history)
	plt.ylabel("Cost")
	plt.xlabel("Iteration")
	plt.title("Cost function graph")
	plt.show()

def check_dataset(dataset):
	try :
		pd.read_csv(dataset)
	except :
		raise argparse.ArgumentTypeError("invalid dataset, needs to be a csv file")
	return dataset

def get_data_visual(usage, param):
	parser = argparse.ArgumentParser(description=usage)
	parser.add_argument("dataset", type=check_dataset, help="dataset, needs to be a csv")
	if (param == 2) :
		parser.add_argument("weights", type=check_dataset, help="weights, needs to be a csv")
		parser.add_argument("-a", "--accuracy", action="store_true", help="show accuracy for dataset_train")
		args = parser.parse_args()
		if args.accuracy is True :
			return pd.read_csv(args.dataset), pd.read_csv(args.weights), 1
		return pd.read_csv(args.dataset), pd.read_csv(args.weights), 0
	if (param == 1) :
		parser.add_argument("-v", type=str, choices=["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"], help="display data of one house in a separate windows")
		args = parser.parse_args()
		if args.v is not None :
			return pd.read_csv(args.dataset), args.v
		return pd.read_csv(args.dataset), 0
	args = parser.parse_args()
	return pd.read_csv(args.dataset)

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