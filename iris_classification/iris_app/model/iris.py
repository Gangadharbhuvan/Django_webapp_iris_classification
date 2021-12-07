import pandas
import pickle
import numpy
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


#Load Dataset
from  sklearn import  datasets
dataset = datasets.load_iris()


x=dataset.data
y=dataset.target

from sklearn.model_selection import train_test_split
X_train, X_validation, Y_train, Y_validation =train_test_split(x,y,test_size=.3)

scoring = 'accuracy'

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVC', SVC()))

# Evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

print("\n")
svc = SVC()
svc.fit(X_train, Y_train)
predictions = svc.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

# Dump the trained model (we can retrieve the dumped model whenever we wantz)
pickle.dump(svc,open("model.pkl","wb"))
print('Model dump SUCCESSFULL')



################################3333
# # # Python version
# # import sys
# # import scipy
# # import numpy
# # import matplotlib
# # import pandas
# # import sklearn
# #
# # #load libraries
# # import pandas
# # # from pandas.tools.plotting import scatter_matrix
# # import matplotlib.pyplot as plt
# # from sklearn import model_selection
# # from sklearn.metrics import classification_report
# # from sklearn.metrics import confusion_matrix
# # from sklearn.metrics import accuracy_score
# # from sklearn.linear_model import LogisticRegression
# # from sklearn.tree import DecisionTreeClassifier
# # from sklearn.neighbors import KNeighborsClassifier
# # from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# # from sklearn.naive_bayes import GaussianNB
# # from sklearn.svm import SVC
# #
# # # Load Dataset
# # from  sklearn import  datasets
# # dataset = datasets.load_iris()
# #
# #
# # x=dataset.data
# # y=dataset.target
# #
# # from sklearn.model_selection import train_test_split
# # X_train, X_validation, Y_train, Y_validation =train_test_split(x,y,test_size=.3)
# #
# #
# #
# # # Test options and evaluation metric
# # seed = 7
# # scoring = 'accuracy'
# #
# # #spot check algorithms
# #
# # models = []
# # models.append(('LR', LogisticRegression() ))
# # models.append(('LDA', LinearDiscriminantAnalysis() ))
# # models.append(('KNN',KNeighborsClassifier() ))
# # models.append(('CART', DecisionTreeClassifier() ))
# # models.append(('NB',GaussianNB() ))
# # models.append(('SVM', SVC() ))
# #
# # #evaluate each model in turn
# # results = []
# # names = []
# # for name, model in models:
# #     kfold = model_selection.KFold(n_splits=10)
# #     cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
# #     #print(cv_results)
# #     results.append(cv_results)
# #     names.append(name)
# #     msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
# #     print(msg)
# #
# # #compare algorithms
# #     fig = plt.figure()
# #     fig.suptitle('Algorithm Comparison')
# #     ax = fig.add_subplot(111)
# #     plt.boxplot(results)
# #     ax.set_xticklabels(names)
# #     plt.show()
# # #
# # # #make predicitions on validation dataset
# # #
# # #     knn = KNeighborsClassifier()
# # #     knn.fit(X_train, Y_train)
# # #     predictions = knn.predict(X_validation)
# # #     print(accuracy_score(Y_validation, predictions))
# # #     print(confusion_matrix(Y_validation, predictions))
# # #     print(classification_report(Y_validation, predictions))


# import pandas
# import pickle
# import numpy
# from pandas.plotting import scatter_matrix
# import matplotlib.pyplot as plt
# from sklearn import model_selection
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import accuracy_score
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import SVC

# # url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
# # names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# # dataset = pandas.read_csv(url , names=names)
# # print()

# #Load Dataset
# from  sklearn import  datasets
# dataset = datasets.load_iris()


# x=dataset.data
# y=dataset.target

# from sklearn.model_selection import train_test_split
# X_train, X_validation, Y_train, Y_validation =train_test_split(x,y,test_size=.3)

# # # # print(dataset.describe())
# # # numpyarray = numpy.asarray(dataset)
# # # X = numpyarray[:,0:4]
# # # Y = numpyarray[:,4]
# # # validation_size = 0.20
# # # seed = 7
# #
# # from sklearn.model_selection import train_test_split
# # X_train, X_validation, Y_train, Y_validation =train_test_split(x,y,test_size=.3)

# # X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# # Test options and evaluation metric
# scoring = 'accuracy'

# # Spot Check Algorithms
# models = []
# models.append(('LR', LogisticRegression()))
# models.append(('LDA', LinearDiscriminantAnalysis()))
# models.append(('KNN', KNeighborsClassifier()))
# models.append(('CART', DecisionTreeClassifier()))
# models.append(('NB', GaussianNB()))
# models.append(('SVC', SVC()))

# # Evaluate each model in turn
# results = []
# names = []
# for name, model in models:
# 	kfold = model_selection.KFold(n_splits=10)
# 	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
# 	results.append(cv_results)
# 	names.append(name)
# 	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
# 	print(msg)

# print("\n")
# svc = SVC()
# svc.fit(X_train, Y_train)
# predictions = svc.predict(X_validation)
# print(accuracy_score(Y_validation, predictions))
# print(confusion_matrix(Y_validation, predictions))
# print(classification_report(Y_validation, predictions))

# # Dump the trained model (we can retrieve the dumped model whenever we wantz)
# pickle.dump(svc,open("model.pkl","wb"))
# print('Model dump SUCCESSFULL')
