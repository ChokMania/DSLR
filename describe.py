import pandas as pd
import argparse
from os import path
import numpy as np
from functions import count, mean, std, minimum, pc25, pc50, pc75, maximum

function = {'0': count, '1': mean, '2': std, '3': minimum, '4': pc25, '5': pc50, '6':pc75, '7':maximum}
printer = {'0': 'count', '1': 'mean', '2': 'std', '3': 'min', '4': '25%', '5': '50%', '6': '75%', '7': 'max'}

def check_file(file):
	try :
		path.exists(file)
		pd.read_csv(file)
	except :
		raise argparse.ArgumentTypeError("invalid file, need a real csv file")
	return file

def create_array(file):
	column = []
	values = [[] for k in range(8)]
	maxColumnLenghts = [0] * len(file.columns[0:,])
	j = 0
	for x in file.columns[0:,]:
		column += [[x]]
		maxColumnLenghts[j] = len("{:s}".format(x))
		j += 1
	for i in range(8) :
		for x in range(len(column)):
			values[i] += ["{:.6f}".format(function[str(i)](test[:,x]))]
			tmp = len(values[i][x])
			if tmp > maxColumnLenghts[x]:
				maxColumnLenghts[x] = tmp
	return column, maxColumnLenghts, values

def display(column, maxColumnLenghts, values):
	print("{:5}".format(""), end="  ")
	j = 0
	for x in file.columns[0:,]:
		print("{:>{:d}s}".format(x, maxColumnLenghts[j]), end="  ")
		j += 1
	for i in range(8) :
		print("\n{:5}".format(printer[str(i)]), end=" ")
		for x in range(len(column)):
			print("{:>{:d}s}".format(values[i][x], maxColumnLenghts[x]), end="  ")

if __name__ == '__main__':
	np.set_printoptions(suppress=True)
	parser = argparse.ArgumentParser(description='Diplay dataset')
	parser.add_argument("file", type=check_file, help="dataset to display, need to be a csv")
	args = parser.parse_args()
	file = pd.read_csv(args.file)
	file = file.select_dtypes(include="number")
	test = np.array(file)
	column, maxColumnLenghts, values = create_array(file)
	display(column, maxColumnLenghts, values)
	print("\n\n\n", file.describe())



