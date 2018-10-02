# P1.1
def myFun(s):     # the type of s is string, string is immutable
    s2 = s;
    length = len(s)
    for i in range(0, length):
        # ord(): convert letter to its ASCII
        if 64<ord(s[i])<91 or 96<ord(s[i])<123 :
            continue;
        else:
            s2 = s2.replace(s[i], ' ')        
    s2 = s2.lower()        
    ls = s2.split()
    
    dic = {}
    for ele in ls:
        if ele in dic:
            dic[ele] = dic[ele] + 1
        else:
            dic[ele] = 1
    
    frequency = 0
    word = ""
    for key in dic :
        if dic[key] > frequency :
            frequency = dic[key]
            word = key
    print("The most frequent key is '%s', its frequency is %d." %(word, frequency))
        
    return dic

#P1.2
class Rectangular: 
    def __init__(self, leng, wid) :
        self.length = leng
        self.width = wid
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangular):
    def __init__(self, leng):
        self.length = leng
        self.width = leng 

#P2.1
import math
def ODE(x):
    return x+4-math.exp(x)
def solveODE(x0):   # return an equilibrium point
    step = 0.05
    count = 0
    if abs(ODE(x0)) < 0.1:  # threshold is 0.1
        return x0
    while ODE(x0) > 0 :
        if count > 5000 : 
            return 'can not find an equilibrium point near x0'
        x0 += step
        count += 1
        if(abs(ODE(x0))) < 0.1 :
            return x0
    while ODE(x0) < 0 :
        if count > 5000 : 
            return 'can not find an equilibrium point near x0'
        x0 -= step
        count += 1
        if abs(ODE(x0)) < 0.1 :
            return x0

#P2.2
import numpy as np
def ODE2(x):
    return math.sin(x) * math.exp(x)

def bisection(left, right):
    if np.sign(ODE2(left)) == np.sign(ODE2(right)) :
        return 'no solution in this interval'
    if ODE2(left) > ODE(right) :
        print('stable point:')
    else:
        print('unstable point:')
    mid = (left + right) / 2
    while abs(ODE2(mid)) > 0.01:   # threshold is 0.01
        if np.sign(ODE2(mid)) == np.sign(ODE2(left)) : 
            left = mid
            mid = (left + right) / 2
        else:
            right = mid
            mid = (left + right) / 2
    return mid;

#P2.3
def ODE3(x):
    return x * math.sin(x) - 1
def findAllSolution(left, right):
    dic = {}
    step = 0.1
    x = left
    while x < right :
        if abs(ODE3(x)) < 0.1:   # threshold is 0.1
            if ODE3(x) < ODE3(x-step) :
                value = 'stable'
            else :
                value = 'unstable'
            dic[x] = value
        x += step 
    return dic

#Leecode-P9
def isPalindrome(x):
        if x < 0:
            return False
        
        s = str(x)
        length = len(s)
        if length < 2 :
            return True
        
        mid = length // 2
        for i in range(0, mid):
            if s[i] != s[length-1-i]:
                return False
        return True

def main():
    s = '''This course is designed for those students have no experience or limited experience on Python. \
       This course will cover the basis syntax rules, modules, importing packages (Numpy, pandas), data \
       visualization, and Intro for machine learning on Python. You willneed to implement what you learn \
       from this course to do a finance related project. This course aims to get you familiar with Python \
       language, and can finish a simple project with Python.'''
    ret = myFun(s)
    print(ret)
    
    myRec = Rectangular(10, 20)
    print(myRec.area())
    print(myRec.perimeter())
    mySqu = Square(10)
    print(mySqu.area())
    print(mySqu.perimeter())

    print(solveODE(0))
    print(bisection(2, 4))
    print(findAllSolution(-4, 4))

    print(isPalindrome(x=3883))
    
if __name__ == '__main__':
    main()






