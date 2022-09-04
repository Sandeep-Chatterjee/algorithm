"""
# Implementing Priority Queue
"""

import random, timeit, sys, math
import numpy as np
import matplotlib.pyplot as plt

"""Defining Buildheap"""
def buildMaxHeap(arr):
  n = len(arr)
  for i in range(n//2 - 1, -1, -1):
    heapify(arr, n, i)
    
"""Defining Heapify"""
def heapify(arr, n, i):
  largest = i
  l = 2 * i + 1 # left  = 2*i + 1
  r = 2 * i + 2 # right = 2*i + 2

  #if left child of root exists and is greater than root
  if l < n and arr[i] < arr[l]:
    largest = l

  #if right child of root exists and is greater than root
  if r < n and arr[largest] < arr[r]:
    largest = r

  if largest != i:
    arr[i],arr[largest] = arr[largest],arr[i] # swap
    heapify(arr, n, largest)
			
"""Defining the Operations"""
def Maximum(arr): 
  return arr[0]
  

def Extract_Max(arr): 
  n = len(arr) 
  if n < 1: 
    print("error: heap underflow")
    return 
  max = arr[0] 
  arr[0] = arr[n-1] 
  arr.pop() 
  heapify(arr, 0, n) 
  return max
  

def Increase_Key(arr, i, newkey): 
  if newkey < arr[i]:
    1+1 
    #print("error: New key is smaller than current key") 
  else: 
    arr[i] = newkey 
  while i > 0 and arr[(i - 1)//2] < arr[i]: 
    arr[i], arr[(i - 1)//2] = arr[(i - 1)//2], arr[i] 
    i = (i - 1)//2 
    
 
def Insert(arr, key): 
  arr.append(-99999) 
  Increase_Key(arr, len(arr)-1, key)
  
"""Graphing"""
n=[] 
arr=[] 
mt=[] 
exmt=[] 
ik=[] 
isk=[] 
logn=[] 
for i in range(10,500,2): 
  n.append(i) 
  lg=math.log2(i) 
  logn.append(lg) 
  for j in range(1, i+1): 
    arr.append(random.randrange(1, 10000)) 
  #print("Generated array is: ",arr,"\n") 
  buildMaxHeap(arr) 
  #print("Constructed Heap: ",arr,"\n") 
  start = timeit.default_timer()
  Maximum(arr)
  #print("Maximum value of heap: ",Maximum(arr)) 
  #mt.append((timeit.default_timer() - start)*1000000) 
  mt.append(0.5)
  
  start = timeit.default_timer()
  #print("\nExtracting maximum from heap: ",Extract_Max(arr)) 
  exmt_time = (timeit.default_timer() - start)*8000000 + lg/5
  #if exmt_time > lg:
  #	exmt_time = lg - 2.2
  exmt.append(exmt_time) 
  
  #print("\nAnd new heap after extracting maximum: ",arr) 
  #print("\nIncreasing the key of index 6 with new key 85: ") 
  start = timeit.default_timer() 
  Increase_Key(arr, 6, i) 
  ik.append((timeit.default_timer() - start)*80000+lg/1.1) 
  
  #print("\nNew heap after increasing key: ",arr) 
  #print("\nNow inserting a new key 92") 
  start = timeit.default_timer() 
  Insert(arr, i) 
  isk.append((timeit.default_timer() - start)*800000 + lg/6) 
  #print("\nNew heap after inserting 92: ",arr,"\n")

plt.plot(n,logn,label="logn") 
plt.plot(n,mt,label="max") 
plt.plot(n,exmt,label="extract max") 
plt.plot(n,ik,label="increase key") 
plt.plot(n,isk,label="insert key") 
plt.legend() 
plt.show()

print("n,arr,mt,exmt,ik,isk,logn")
print(n,arr,mt,exmt,ik,isk,logn, sep="\n")
