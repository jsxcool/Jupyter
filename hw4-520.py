import csv
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

def f(x):
	Max = x.max()
	secondLarget = -1000000   # just a very small number
	for ele in x:
		if ele>secondLarget and ele!=Max:
			secondLarget = ele
	return Series([x.max(), x.min(), secondLarget] ,index=['max', 'min', 'secondLarget'])

def replaceInf(arr, num):
    row = arr.shape[0]
    column = arr.shape[1]
    for i in range(0, row):
        for j in range(0, column):
            if arr[i][j] == np.inf:
                arr[i][j] = num

def replace2(arr):
    row = arr.shape[0]
    column = arr.shape[1]
    for i in range(0, row):
        for j in range(0, column):
            if arr[i][j] > 0:
                arr[i][j] = 1
            if arr[i][j] < 0:
                arr[i][j] = -1

def columnMean(arr, weight):
    row = arr.shape[0]
    column = arr.shape[1]
    ret = np.zeros(column)
    for j in range(0,column):
        for i in range(0,row):
            ret[j] += weight[i]*arr[i][j]
    return ret

def fuseTwoArray(x1, x2):
    x1r = x1.reshape(4,25)
    x2r = x2.reshape(4,25)
    return np.concatenate((x1r,x2r), axis=0)


#1.1
data1 = pd.read_csv('/home/jiang/Downloads/AAPL BS.csv')
data2 = pd.read_csv('/home/jiang/Downloads/AAPL Ratings.csv')
#1.2
data1 = data1.drop(['aqepsq', 'gdwlamq'], axis = 1)  #axis=1 means column
mean = data1['dlttq'].mean()
data1 = data1.replace({'dlttq':0}, mean)
data1['intanq'] = data1['intanq'].interpolate()
print('#1.2\n', data1['intanq'], '\n')
#1.3 ```````````````````````````````````````````````
data1['niq'][data1['niq'] > 15000] = 15000
data1['citotalq'][data1['citotalq'] > 15000] = 15000
#1.4
temp = data1.iloc[:,[13,14,15,17,18]]  #[’acoq’, ’actq’, ’apq’, ’chq’,’citotalq’]
print('#1.4\n',temp.apply(f), '\n')
#1.5
print('#1.5\n',temp.corr(), '\n')
#1.6
Matched = pd.merge(data1, data2, on='datadate', how='inner')  # only merge corresponding element
print('#1.6\n',Matched)
#1.7
splticrmToRate = {
    'AAA': 0, 'AA+': 1, 'AA': 2, 'AA-': 3, 'A+': 4, 'A': 5, 'A-': 6,
    'BBB+': 7, 'BBB': 8, 'BBB-': 9, 'BB+': 10, 'BB ': 11
    }
Matched['Rate'] = Matched['splticrm'].map(splticrmToRate)
print('#1.7\n',Matched)
#1.8 1.9
sampler = np.random.randint(0, len(Matched), size = 2*len(Matched))
final = Matched.take(sampler)
final.to_csv('HW4.csv')


#2.1
a = np.array([[1, 2],[4,0]])
b = 1/a
replaceInf(b, 2**8)
print('#2.1\n', b, '\n')
#2.2
c = np.array([[1, 2],[-4,0]])
replace2(c)
print('#2.2\n',c, '\n')
#2.3
data_matrix = np.array([[1,2,3],[-4,0,3]])
weight = np.array([0.2,0.8])
print('#2.3\n',columnMean(data_matrix, weight), '\n')
#2.4
x1 = np.random.rand(100,)
x2 = np.random.rand(100,)
print('#2.4\n',fuseTwoArray(x1,x2), '\n')


#leetcode 561
def arrayPairSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        nums.sort()
        Sum = 0 
        i = 0
        while i < length:
            Sum += nums[i]
            i += 2
        return Sum

nums = [1,4,3,2]
print('leetcode\n',arrayPairSum(nums), '\n')



