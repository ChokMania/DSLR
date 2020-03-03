import numpy as np

def count(data):
	i = 0
	for x in data:
		if not np.isnan(x) :
			i += 1
	return i

def mean(data):
	i = 0
	total = 0
	for x in data:
		if not np.isnan(x) :
			i += x
			total += 1
	return i / total

def std(data):
	mean_value = mean(data)
	i = 0
	total = 0
	for x in data:
		if not np.isnan(x) :
			i += (x - mean_value) ** 2
			total += 1
	return (i / (total - 1)) ** 0.5

#https://en.wikipedia.org/wiki/Quartile method 4
def pc25(data):
	data = np.sort(data)
	total = 0
	for x in data:
		if not np.isnan(x) :
			total += 1
	k = (total - 1) * (25 / 100)
	f = np.floor(k)
	c = np.ceil(k)
	if f == c:
		return data[int(k)]
	d0 = data[int(f)] * (c - k)
	d1 = data[int(c)] * (k - f)
	return d0 + d1

def pc50(data):
	data = np.sort(data)
	total = 0
	for x in data:
		if not np.isnan(x) :
			total += 1
	k = (total - 1) * (50 / 100)
	f = np.floor(k)
	c = np.ceil(k)
	if f == c:
		return data[int(k)]
	d0 = data[int(f)] * (c - k)
	d1 = data[int(c)] * (k - f)
	return d0 + d1

def pc75(data):
	data = np.sort(data)
	total = 0
	for x in data:
		if not np.isnan(x) :
			total += 1
	k = (total - 1) * (75 / 100)
	f = np.floor(k)
	c = np.ceil(k)
	if f == c:
		return data[int(k)]
	d0 = data[int(f)] * (c - k)
	d1 = data[int(c)] * (k - f)
	return d0 + d1

def minimum(data):
	min_value = data[0]
	for x in data:
		if not np.isnan(x) and x < min_value:
			min_value = x
	return min_value

def maximum(data):
	max_value = data[0]
	for x in data:
		if not np.isnan(x) and x > max_value:
			max_value = x
	return max_value