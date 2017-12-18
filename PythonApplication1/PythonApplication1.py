# -*- coding: utf-8 -*- 

import numpy as np

import matplotlib.pyplot as plt



if __name__=="__main__":

    persontype = np.dtype({
        'names':['name','age','weight'],
        'formats':['S30','i','f']},align = True)

    a = np.array([('Liming',24,63.9),('Mike',15,67.),('Jan',34,45.8)],dtype = persontype)

    x = np.random.randn(12,20)

    y = np.random.randn(12,20)

    mark = ['s','o','^','v','>','<','d','p','h','8','+','*']

    for i in range(0,12):

        plt.scatter(x[i],y[i],marker = mark[i],color =(np.random.rand(1,3)),s=50,label = str(i+1))

    plt.legend()

    plt.show()

    print (a)

    b=1




