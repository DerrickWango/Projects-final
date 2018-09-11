
import sqlite3

from sklearn import datasets

import pandas as pd

import numpy as np

iris=datasets.load_iris()

testidx = [0,30,50,60,70,80,75,100]


#training data

train_target=np.delete(iris.target,testidx)

train_data=np.delete(iris.data,testidx,axis=0)

#test data

test_target=iris.target[testidx]

test_data=iris.data[testidx]


#print(test_data)

def classifier():

    data=train_data

    data2=train_target

    for i in data2[0:48]:

        z=np.array(i)

        print(z)

        
classifier()





















    


    

    
