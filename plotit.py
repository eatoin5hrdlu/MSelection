#!C:\cygwin\Python27\python -u
import os
import matplotlib.pyplot as plt
import time
while( os.stat('plot.data').st_size < 200 ) :
    time.sleep(1)
    print("waiting...")
f = open('plot.data','r')

raw = f.read()
list = eval(raw[:-1]+']')
llen = len(list)
plt.plot(list)
plt.axis([0,llen,0,100])
plt.ylabel('Clone Number for Dominant Genotype')
plt.show()
