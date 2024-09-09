import time
import numpy as np
import matplotlib.pyplot as plt
def binary_search(a,key):
    low=0
    high=len(a)
    while low<high:
        mid=(low+high)//2
        if key<a[mid]:
            high=mid
        elif key>a[mid]:
            low=mid+1
        else:
            return mid
    return-1 
elements=np.array([i*1000 for i in range(1,10)])
plt.xlabel('list length')
plt.ylabel('time complexity')
times=list()
for i in range(1,10):
    start=time.time()
    a=np.random.randint(0,1000*i,1000*i)
    binary_search(a,1)
    end=time.time()
    times.append(end-start)
    print("time taken for binary search in ",i*1000,"elements is", end-start,"s")
plt.plot(elements,times,label="Binary search")
plt.grid()
plt.legend()
plt.show()
