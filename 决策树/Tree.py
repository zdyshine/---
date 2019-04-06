# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:48:20 2019

@author: zdy
@time: 2019-4-6
"""

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

# Read in the csv file and put features into list of dict and list of class label
allElectronicsData = open(r'./AllElectronics.csv', 'rt') #修改
reader = csv.reader(allElectronicsData)
headers = next(reader) #获取csv文件头部 

print(headers)

# 数据转换为数值型
# 定义特征列表和label列表
featureList = [] 
labelList = []

for row in reader:
    labelList.append(row[len(row)-1]) # 取列表的最后一项，最后一项是label
    rowDict = {}
    for i in range(1, len(row)-1): # 取第二和倒数第二的特征，第一列的是RID，不需要
#        print(headers[i]) # age income student credit_rating
#        print(row[i]) # 对应的值
        rowDict[headers[i]] = row[i]  # 组成字典
    featureList.append(rowDict)  # 字典写到list中
#
#print(featureList)
#
# Vetorize features
vec = DictVectorizer() # sklearn的自带函数
#print(vec)
dummyX = vec.fit_transform(featureList) .toarray() # 转化为数值列表

#print("dummyX: " + str(dummyX))
#print(vec.get_feature_names())
#
#print("labelList: " + str(labelList))

# vectorize class labels
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
#print("dummyY: " + str(dummyY))
#
# Using decision tree for classification
# clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='entropy') # 系统的决策树函数，使用entropy作为判定
clf = clf.fit(dummyX, dummyY) # 构建决策树
print("clf: " + str(clf))

# Visualize model
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))

newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))

predictedY = clf.predict([newRowX])
print("predictedY: " + str(predictedY))
