import tools
import numpy as np

def standardize(x):
	mean = np.mean(x, axis=0)
	std = np.std(x, axis=0)
	return (x - mean) / std, mean, std

def cost_function(x, y, theta):
	m = len(x)
	h0 = tools.sigmoid(np.dot(x, theta))
	return (-(1/m) * sum(y * np.log(h0) + (1 - y) * np.log(1 - h0)))[0]

def d_cost_function(x, y, theta):
	m = len(x)
	h0 = tools.sigmoid(np.dot(x, theta))
	grad = 1/m * np.dot(x.transpose(), (h0 - y))
	return grad

def train_theta(x, y, theta, lr, epoch):
	error_history = []
	for i in range(epoch):
		theta -= lr * d_cost_function(x, y, theta)
		error_history.append(cost_function(x, y, theta))
	return theta, error_history

def compute_point(x, theta):
	return (-(theta[0] + theta[1] * x) / theta[2])

def get_accuracy(x, y, theta):
	length = len(x)
	correct = 0
	for i in range(length):
		prediction = 1 if tools.sigmoid(x[i].dot(theta)) >= 0.5 else 0
		correct = correct + 1 if y[i] == prediction else correct
	return (correct / length) * 100

if __name__ == "__main__":
	df = tools.get_data()
	df.drop(["Index", "Arithmancy", "Potions", "Charms", "Care of Magical Creatures", "Flying"], axis=1, inplace=True)
	df = df[["Hogwarts House"] + list(df.select_dtypes(include="number").columns)]
	row_list = [["House", "Feature1", "Feature2", "Theta1", "Theta2", "Theta3", "Mean", "Std", "Accuracy"]]
	for i in range(1, 5) :
		print(tools.house_rev[i])
		for f1 in range(1, len(df.columns) - 1) :
			for f2 in range(f1 + 1, len(df.columns) - 1) :
				x, y = tools.filter_data(df, tools.house_rev[i], f1, f2)
				#print(df.columns[f1], " vs ",df.columns[f2])
				#tools.display_data(x, y, tools.house_rev[1], df, f1, f2)
				x, mean, std = standardize(x)
				col, row = x.shape[0], x.shape[1]
				x = np.insert(x, 0, 1, axis=1)
				y = y.reshape(col, 1)
				theta = np.zeros((row + 1, 1))
				theta, error_history = train_theta(x, y, theta, 1, 400)
				#tools.display_standardize(x, y, tools.house_rev[1], df, f1, f2, t)
				#tools.display_cost(error_history)
				ac = get_accuracy(x, y, theta)
				#print("Accuracy: {}".format(ac))
				#if ac >= 97 :
				row_list.append([tools.house_rev[i], df.columns[f1], df.columns[f2], theta[0], theta[1], theta[2], mean, std, ac])
	tools.create_csv(row_list, "weight.csv")