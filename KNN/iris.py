from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier() # 赋值knn算法
 
iris = datasets.load_iris() # 从库里加载数据集
# save data
# f = open("iris.data.csv", 'wb')
# f.write(str(iris))
# f.close()

print (iris)

knn.fit(iris.data, iris.target) # 建模fit为建立模型，并传入参数（数据，label）

predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])
#print ("predictedLabel is :" + predictedLabel)
print (predictedLabel)
