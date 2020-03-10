import numpy as np

def count(data):
	count = 0
	for i in data:
		if not np.isnan(i):
			count += 1
	return float(count)

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

def quarter(data):
	tmp_data=[]
	for i in data:
		if not np.isnan(i):
			tmp_data.append(i)
	if (len(tmp_data) == 0):
		return float("NaN")
	return np.percentile(np.array(tmp_data), 25)

def median(data):
	tmp_data=[]
	for i in data:
		if not np.isnan(i):
			tmp_data.append(i)
	if (len(tmp_data) == 0):
		return float("NaN")
	return np.percentile(np.array(tmp_data), 50)

def three_quarters(data):
	tmp_data=[]
	for i in data:
		if not np.isnan(i):
			tmp_data.append(i)
	if (len(tmp_data) == 0):
		return float("NaN")
	return np.percentile(np.array(tmp_data), 75)

def maxi(data):
	return float(max(data))