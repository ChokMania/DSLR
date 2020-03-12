import numpy as np
import math

def count(data):
	count = 0
	for i in data:
		if not np.isnan(i):
			count += 1
	return float(count)

def unique(data):
	list_unique = []
	for i in data:
		if i not in list_unique:
			list_unique.append(i)
	return len(list_unique)

def top(data):
	global index
	list_unique = []
	number_unique = []
	for i in data:
		if i not in list_unique:
			list_unique.append(i)
			number_unique.append(1)
		else:
			number_unique[list_unique.index(i)] += 1
	index = number_unique.index(max(number_unique))
	return list_unique[index]

def freq(data):
	list_unique = []
	number_unique = []
	for i in data:
		if i not in list_unique:
			list_unique.append(i)
			number_unique.append(1)
		else:
			number_unique[list_unique.index(i)] += 1
	return number_unique[number_unique.index(max(number_unique))]

def mean(data):
	curr_count = count(data)
	if curr_count == 0:
		return float("NaN")
	total = 0
	for i in data:
		if not np.isnan(i):
			total += i
	return float(total / curr_count)

def std(data):
	curr_count = count(data) - 1
	if curr_count <= 0:
		return float("NaN")
	curr_mean = mean(data)
	curr_sum = 0
	for i in data:
		if not np.isnan(i):
			curr_sum += (i - curr_mean)**2
	return np.sqrt(curr_sum/curr_count)

def mini(data):
	return float(min(data))

def percentile(data, percent):
	if not data.any:
		return (None)
	data = np.sort(data)
	rank = (len(data) - 1) * percent
	low = math.floor(rank)
	high = math.ceil(rank)
	if (low == high):
		return data[int(rank)]
	return data[int(low)] * (high - rank) + data[int(high)] * (rank - low)

def quarter(data):
	tmp_data=[]
	for i in data:
		if not np.isnan(i):
			tmp_data.append(i)
	if (len(tmp_data) == 0):
		return float("NaN")
	return percentile(np.array(tmp_data), 0.25)

def median(data):
	tmp_data=[]
	for i in data:
		if not np.isnan(i):
			tmp_data.append(i)
	if (len(tmp_data) == 0):
		return float("NaN")
	return percentile(np.array(tmp_data), 0.50)

def three_quarters(data):
	tmp_data=[]
	for i in data:
		if not np.isnan(i):
			tmp_data.append(i)
	if (len(tmp_data) == 0):
		return float("NaN")
	return percentile(np.array(tmp_data), 0.75)

def maxi(data):
	return float(max(data))