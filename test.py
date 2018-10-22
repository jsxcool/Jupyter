import csv
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz

class Hypothesis:
	def __init__(self, pclass, sex, age, sibsp):
		self.pclass = pclass
		self.sex = sex
		self.age = age
		self.sibsp = sibsp
	def __repr__(self):
		return '(%d, %d, %f, %d)' %(self.pclass, self.sex, self.age, self.sibsp)

X = []
Y = []
dic1 = {'1st':1, '2nd':2, '3rd':3}
dic2 = {'male':1, 'female':0}

with open('Titanic.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		if reader.line_num == 1:
			continue;
		if row[5] == 'NA':
			row[5] = 0
		#Hypothesis(dic1[row[1]], dic2[row[4]], float(row[5]), int(row[6]))
		X.append([dic1[row[1]], dic2[row[4]], float(row[5]), int(row[6])])
		Y.append(int(row[2]))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
#print(X_test)
clf = tree.DecisionTreeClassifier()    # only spport float/int
clf = clf.fit(X_test, Y_test)
#print(clf.predict([[1,0,29,0]]))
dot_data = tree.export_graphviz(clf, out_file = None,
								feature_names = ['pclass', 'sex', 'age', 'sibsp'],
								class_names = ['survived', 'dead'],
								filled = True, rounded = True,
								special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("titan")



