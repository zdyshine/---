# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:46:07 2019

@author: jxufe
"""

import csv
import random
import math
import operator
import codecs

def Load_data(filename, split, trainset = [], testset = []):
    with codecs.open(filename,'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
#        print(dataset)
#        dataset = float(dataset)  # float() argument must be a string or a number, not 'list'
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y]) # 元素全部转成float型,后面计算需要
            if random.random() < split:
                trainset.append(dataset[x])
            else:
                testset.append(dataset[x])
#                
#    print(trainset)
#    print(testset)
def compuetdistance(instance1, instance2, length):
    distance = 0
#    print('length',length)
#    print('instance1:',instance1)
#    print('instance2',instance2)
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]), 2)
    return math.sqrt(distance)
             
def getNeighbors(trainSet, testinstance, k):
    distance = []
    length = len(testinstance)-1
    for x in range(len(trainSet)):
        dis = compuetdistance(testinstance, trainSet[x], length)
        distance.append((trainSet[x], dis))
    distance.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distance[x][0])
    return neighbors # 有改动

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
         
def getAccurary(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet)))*100.0
   
def main():
    trainset = []
    testset = []
    split = 0.67
    file = './irisdata.txt'
    Load_data(file,  split, trainset, testset) #加载数据集，转化为float型，并划分训练集个验证集
    
    predictions = []
    k = 3
    for x in range(len(testset)):
        neighbors = getNeighbors(trainset, testset[x], k) #获取前k个最近实例
        result = getResponse(neighbors) # 进行投票得到测试类别
        predictions.append(result) 
    accuracy = getAccurary(testset,predictions)
    print('Accuracy: ' + repr(accuracy) + '%')


if __name__ == '__main__':
    main()