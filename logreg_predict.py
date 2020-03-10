import numpy as np
import pandas as pd
import sys
import csv

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

def predict_house(student, data, result):
	pass

if __name__ == "__main__":
	house = { "Ravenclaw": 1, "Slytherin": 2, "Gryffindor": 3, "Hufflepuff": 4 }
	house_rev = { value: key for key, value in house.items() }
	result = [0] * 4
	df = get_data()
	df.drop('Index', axis=1, inplace=True)
	df.drop('Arithmancy', axis=1, inplace=True)
	df.drop("Potions", axis=1, inplace=True)
	df.drop("Care of Magical Creatures", axis=1, inplace=True)
	df.drop("Charms", axis=1, inplace=True)
	df.drop("Flying", axis=1, inplace=True)
	df = df[["Hogwarts House"] + list(df.select_dtypes(include="number").columns)]
	weight = pd.read_csv("weights.csv")
	print(weight)
	for row in df:
		print (df)