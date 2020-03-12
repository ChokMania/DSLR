import numpy as np
from tools.compute_metrics import count, unique, top, freq, mean, std, mini, quarter, median, three_quarters, maxi
from tools.utilities import get_data_visual

select_fnc = {
	0: count,
	1: unique,
	2: top,
	3: freq,
	4: mean,
	5: std,
	6: mini,
	7: quarter,
	8: median,
	9: three_quarters,
	10: maxi
}

rows = ["count", "unique", "top", "freq", "mean", "std", "min", "25%", "50%", "75%", "max"]

def describe(data):
	data_len = len(data[0])
	i = 0
	metrics = np.ndarray(shape=(11, data_len), dtype=float)
	while i != 11:
		j = 0
		while j != data_len:
			metrics[i][j] = select_fnc[i](data[:,j])
			j += 1
		i += 1
	return metrics

def get_width(column_name, data_column):
	max_size = len(column_name)
	for field in data_column:
		max_size = max(len("%.6f"%field), max_size)
	return max_size

def clean_print(columns, data):
	print("{:<6s}".format(' '), end='')
	for i in range(len(columns)):
		width = get_width(columns[i], data[:,i])
		print("{:>{:d}s}".format(columns[i], width + 2), end='')

	for i in range(len(data[:,0])):
		print("\n{:<6s}".format(rows[i]), end='')
		for j in range(len(data[0])):
			width = get_width(columns[j], data[:,j])
			print("{:>{:d}.6f}".format(data[i][j], width + 2), end='')
	print()

if __name__ == "__main__":
	np.set_printoptions(suppress=True)
	data = get_data_visual("describe of datset (like pandas)", 0)
	data = data.select_dtypes('number')
	include =['object', 'float', 'int'] 
	metrics = describe(data.to_numpy())
	clean_print(data.columns, metrics)