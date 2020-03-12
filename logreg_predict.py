import numpy as np
from tools.utilities import house, house_rev, get_data_visual, sigmoid, create_csv, pie_chart

def predict_house(student, weights):
	results = [[], [], [], []]
	for row in weights:
		if not np.isnan(student[row[1]]) and not np.isnan(student[row[2]]):
			x = np.array([student[row[1]], student[row[2]]])
			theta = np.array([row[3], row[4], row[5]])
			mean = np.array([row[6], row[7]])
			std = np.array([row[8], row[9]])
			x = (x - mean) / std
			x = np.insert(x, 0, 1, axis=0)
			results[house[row[0]] - 1].append(sigmoid(np.dot(x, theta)))
	for i in range(4):
		if (len(results[i]) != 0):
			results[i] = sum(results[i]) / len(results[i])
		else:
			results[i] = 0
	return (house_rev[results.index(max(results)) + 1])

def get_accuracy(y_true, y_pred):
	correct_pred = 0
	length = len(y_true)
	for i in range(length):
		if (y_true[i] == y_pred[i]):
			correct_pred += 1
	return correct_pred / length

def is_valid(df):
	df = df[["Hogwarts House"]]
	if df.isnull().values.any() == True:
		return 0
	return 1

if __name__ == "__main__":
	student_results = []
	df, weights, accuracy, pc = get_data_visual("predicts student's house with our model", 2)
	df.drop(["Index", "Arithmancy", "Potions", "Care of Magical Creatures", "Charms","Flying"], axis=1, inplace=True)
	df = df[["Hogwarts House"] + list(df.select_dtypes(include="number").columns)]
	row_list = [["Index", "Hogwarts House"]]
	for i in range(len(df)):
		tmp = predict_house(df.loc[i, :], weights.to_numpy())
		student_results.append(tmp)
		row_list.append([i, tmp])
	if (accuracy):
		if (is_valid(df)):
			print("Accuracy:", get_accuracy(df["Hogwarts House"].tolist(), student_results))
			if (pc):
				pie_chart(df["Hogwarts House"].to_list(), "Actual data")
		else:
			print("Could not print accuracy because a class is not specified")
	if (pc):
		pie_chart(student_results, "Prediction results")
	create_csv(row_list, "houses.csv")
	print("Weights saved in './houses.csv'")