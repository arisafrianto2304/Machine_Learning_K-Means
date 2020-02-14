# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:58:04 2018

@author: windowss
"""

import numpy, math, random
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

#untuk membaca file TestsetTugas2.txt
text_file = open("TestsetTugas2.txt", "r")
lines = text_file.readlines()

data_test = []
for i in range (0 , len(lines)):
    data_test.append([float(x) for x in lines[i].split()])
data_test = numpy.array(data_test)

#untuk membaca file TrainsetTugas2.txt
text_file = open("TrainsetTugas2.txt", "r")
lines = text_file.readlines()


data_train = []
for i in range (0 , len(lines)):
    data_train.append([float(x) for x in lines[i].split()])
    
data_train = numpy.array(data_train)
k1 = random.choice(data_train)
k2 = random.choice(data_train)
k3 = random.choice(data_train)
k4 = random.choice(data_train)
k5 = random.choice(data_train)
label = [0 for i in range (len(data_train))]

#
for i in range (10) :
    for j in range (len(data_train)) :
        jarak1 = math.sqrt(math.pow((data_train[j][0]-k1[0]),2)+math.pow((data_train[j][1]-k1[1]),2))
        jarak2 = math.sqrt(math.pow((data_train[j][0]-k2[0]),2)+math.pow((data_train[j][1]-k2[1]),2))
        jarak3 = math.sqrt(math.pow((data_train[j][0]-k3[0]),2)+math.pow((data_train[j][1]-k3[1]),2))
        jarak4 = math.sqrt(math.pow((data_train[j][0]-k4[0]),2)+math.pow((data_train[j][1]-k4[1]),2))
        jarak5 = math.sqrt(math.pow((data_train[j][0]-k5[0]),2)+math.pow((data_train[j][1]-k5[1]),2))
        if jarak1 < jarak2 and jarak1 < jarak3 and jarak1 < jarak4 and jarak1 < jarak5 :
            label[j] = 1
        elif jarak2 < jarak1 and jarak2 < jarak3 and jarak2 < jarak4 and jarak2 < jarak5 :
            label[j] = 2
        elif jarak3 < jarak1 and jarak3 < jarak2 and jarak3 < jarak4 and jarak3 < jarak5 :
            label[j] = 3
        elif jarak4 < jarak1 and jarak4 < jarak2 and jarak4 < jarak3 and jarak4 < jarak5 :
            label[j] = 4
        elif jarak5 < jarak1 and jarak5 < jarak2 and jarak5 < jarak3 and jarak5 < jarak4 :
            label[j] = 5
    a = [0.0,0.0]
    b = [0.0,0.0]
    c = [0.0,0.0]
    d = [0.0,0.0]
    e = [0.0,0.0]
    jml1 = 0
    jml2 = 0
    jml3 = 0
    jml4 = 0
    jml5 = 0
    for j in range(len(data_train)) :
        if label[j] == 1 :
            a[0] += data_train[j][0]
            a[1] += data_train[j][1]
            jml1 += 1
        elif label[j] == 2 :
            b[0] += data_train[j][0]
            b[1] += data_train[j][1]
            jml2 += 1
        elif label[j] == 3 :
            c[0] += data_train[j][0]
            c[1] += data_train[j][1]
            jml3 += 1
        elif label[j] == 4 :
            d[0] += data_train[j][0]
            d[1] += data_train[j][1]
            jml4 += 1
        elif label[j] == 5 :
            e[0] += data_train[j][0]
            e[1] += data_train[j][1]
            jml5 += 1
    
    a[0] = a[0]/jml1
    a[1] = a[1]/jml1
    b[0] = b[0]/jml2
    b[1] = b[1]/jml2
    c[0] = c[0]/jml3
    c[1] = c[1]/jml3
    d[0] = d[0]/jml4
    d[1] = d[1]/jml4
    e[0] = e[0]/jml5
    e[1] = e[1]/jml5

    k1 = [a[0],a[1]]
    k2 = [b[0],b[1]]
    k3 = [c[0],c[1]]
    k4 = [d[0],d[1]]
    k5 = [e[0],e[1]]

print(k1,k2,k3,k4,k5)
plt.scatter(data_train[:,0],data_train[:,1],c=label)
plt.scatter(k1[0],k1[1],c='b')
plt.scatter(k2[0],k2[1],c='b')
plt.scatter(k3[0],k3[1],c='b')
plt.scatter(k4[0],k4[1],c='b')
plt.scatter(k5[0],k5[1],c='b')
plt.title('Data Train')
plt.show()

label1 = [0 for i in range (len(data_test))]
for i in range (10) :
    for j in range (len(data_test)) :
        jarak1 = math.sqrt(math.pow((data_test[j][0]-k1[0]),2)+math.pow((data_test[j][1]-k1[1]),2))
        jarak2 = math.sqrt(math.pow((data_test[j][0]-k2[0]),2)+math.pow((data_test[j][1]-k2[1]),2))
        jarak3 = math.sqrt(math.pow((data_test[j][0]-k3[0]),2)+math.pow((data_test[j][1]-k3[1]),2))
        jarak4 = math.sqrt(math.pow((data_test[j][0]-k4[0]),2)+math.pow((data_test[j][1]-k4[1]),2))
        jarak5 = math.sqrt(math.pow((data_test[j][0]-k5[0]),2)+math.pow((data_test[j][1]-k5[1]),2))
        if jarak1 < jarak2 and jarak1 < jarak3 and jarak1 < jarak4 and jarak1 < jarak5 :
            label1[j] = 1
        elif jarak2 < jarak1 and jarak2 < jarak3 and jarak2 < jarak4 and jarak2 < jarak5 :
            label1[j] = 2
        elif jarak3 < jarak1 and jarak3 < jarak2 and jarak3 < jarak4 and jarak3 < jarak5 :
            label1[j] = 3
        elif jarak4 < jarak1 and jarak4 < jarak2 and jarak4 < jarak3 and jarak4 < jarak5 :
            label1[j] = 4
        elif jarak5 < jarak1 and jarak5 < jarak2 and jarak5 < jarak3 and jarak5 < jarak4 :
            label1[j] = 5

plt.scatter(data_test[:,0],data_test[:,1],c=label1)
plt.title('Data Test')
plt.show()
