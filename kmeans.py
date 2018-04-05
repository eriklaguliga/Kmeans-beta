import numpy
import math
import matplotlib.pyplot as pl
import random


data_test= numpy.genfromtxt("TestsetTugas2.txt")
data_train = numpy.genfromtxt("TrainsetTugas2.txt")

def eculidian(x1 , x2 , y1 , y2) :
    a = (x1 - y1) ** 2 + (x2 - y2) ** 2
    wew = math.sqrt(a)
    return wew

c1 = []
c2 = []
c1.append(random.randint(1,10))
c1.append(random.randint(1,10))
c2.append(random.randint(1,10))
c2.append(random.randint(1,10))
# print(c1)
stop = False
kelas = []
while stop == False:
    for i in data_test:
        a = eculidian(c1[0],c1[1],i[0],i[1])
        b = eculidian(c2[0],c2[1],i[0],i[1])
        if(a<b):
            kelas.append(1)
        else:
            kelas.append(2)
    clas = numpy.asarray(kelas)
    del kelas[:]
    sementara = numpy.concatenate((data_test,clas[:,None]),axis=1)
    kosong = []
    kosong1 = []
    kosong2 = []
    kosong3 = []
    for i in sementara:
        if(i[2] == 1):
            kosong.append(i[0])
            kosong1.append(i[1])
        else:
            kosong2.append(i[0])
            kosong3.append(i[1])
    ou1 = []
    ou2 = []
    ou1.append(kosong)
    ou1.append(kosong1)
    ou2.append(kosong2)
    ou2.append(kosong2)
    if (ou1 == c1 and ou2 == c2):
        stop = True
    else:
        stop=False
        del c1[:], c2[:]
        c1.append(numpy.mean(kosong))
        c1.append(numpy.mean(kosong1))
        c2.append(numpy.mean(kosong2))
        c2.append(numpy.mean(kosong3))




# kelas = numpy.asarray(kelas)
# print(kelas)
# wow = numpy.concatenate((data_test,kelas[:,None]),axis=1)
# rata = 0
# count = 0
# for i in wow:
#     if(i[2] == 1):
#         count = count+1
#         rata = rata = i[0]
# average = rata/count
# print(average)
# print(data_test)