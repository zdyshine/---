import csv
import random
import math
import operator

# 加载数据集
def loadDataset(filename, split, trainingSet = [], testSet = []):
    with open(filename, 'r') as csvfile: #以，分隔符形式的文件
        lines = csv.reader(csvfile) # 读取所有行
#        print(lines)
        dataset = list(lines) # 转化为list
#        print(dataset)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
#                print(dataset[x][y])
            if random.random() < split: # 划分训练集和验证集
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

# 传入实例和维度，计算距离
def euclideanDistance(instance1, instance2, length): #(测试样例，训练集合，)
    distance = 0
#    print('length',length)
#    print('instance1:',instance1)
#    print('instance2',instance2)
    for x in range(length): # length:维度
        distance += pow((instance1[x]-instance2[x]), 2)
    return math.sqrt(distance)

# 
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1  # 测试集长度
    for x in range(len(trainingSet)): #
        #testinstance #只传入一个测试样例，对所有训练集进行计算对应点的distance
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
        #distances.append(dist)
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])   
        return neighbors  # ???
#    print('neighbors:',neighbors)


def getResponse(neighbors): #对近邻分类，取类别最多的
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    print('sortedVotes:',sortedVotes)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
#    print('len(testSet):',testSet)
    for x in range(len(testSet)):
#        print(testSet[x])
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet)))*100.0


def main():
    #prepare data
    trainingSet = []
    testSet = []
    split = 0.67 # 2/3的训练集
    loadDataset('irisdata.txt', split, trainingSet, testSet)
    print ('Train set: ' + repr(len(trainingSet)))
    print ('Test set: ' + repr(len(testSet)))
    #generate predictions 
    predictions = []
    k = 3
    for x in range(len(testSet)):
        # trainingsettrainingSet[x]
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
#        print('predixtions:',predictions)
#        print ('>predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

if __name__ == '__main__':
    main()































