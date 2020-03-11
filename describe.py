import sys
import pandas as pd
import numpy as np
from tools.compute_metrics import count, mean, std, mini, quarter, median, three_quarters, maxi
from tools.utilities import get_data_visual

select_fnc = {
	0: count,
	1: mean,
	2: std,
	3: mini,
	4: quarter,
	5: median,
	6: three_quarters,
	7: maxi
}

rows = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]

def describe(data):
	data_len = len(data[0])
	i = 0
	metrics = np.ndarray(shape=(8, data_len), dtype=float)
	while i != 8:
		j = 0
		while j != data_len:
			metrics[i][j] = select_fnc[i](data[:,j])
			j += 1
		i += 1
	for i in range(len(metrics[:,0]) - 1):
		for j in range(len(metrics[0]) - 1):
			metrics[i][j] = np.format_float_positional(np.float(metrics[i][j]), unique=False, precision=6)
	return metrics

def get_width(column_name, data_column):
	max_size = len(column_name)
	for field in data_column:
		max_size = max(len("%.6f"%field), max_size)
	return max_size

def clean_print(columns, data):
	print("{:<5s}".format(' '), end='')
	for i in range(len(columns)):
		width = get_width(columns[i], data[:,i])
		print("{:>{:d}s}".format(columns[i], width + 2), end='')

	for i in range(len(data[:,0])):
		print("\n{:<5s}".format(rows[i]), end='')
		for j in range(len(data[0])):
			width = get_width(columns[j], data[:,j])
			print("{:>{:d}.6f}".format(data[i][j], width + 2), end='')
	print()

if __name__ == "__main__":
	np.set_printoptions(suppress=True)
	data = get_data_visual("describe of datset (like pandas)", 0)
	data = data.select_dtypes('number')
	metrics = describe(data.to_numpy())
	clean_print(data.columns, metrics)