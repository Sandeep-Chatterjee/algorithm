"""
# Merge Sort Algorithm - Divide and Conquer
"""

import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

"""Defining mergesort"""
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        M = arr[mid:]
        mergesort(L)
        mergesort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1
    return arr

"""Function to return array of random numbers of required sizes"""
def rand_arr(n):
  return [random.randrange(100) for i in range(n)]
scale = 2000000

print("\n\tGenerating Random arrays of different sizes...")
for i in range(5,8):
  print("random array of size",i,":",rand_arr(i))
  
def curr_time():
  return timeit.default_timer()*scale
  
"""testing Mergesort"""
print("\n\tRunning MergeSort on few examples")
for i in range(3):
	array = rand_arr(10)
	print("original array : ", array)
	print("sorted array   : ", mergesort(array),'\n')

"""Noting time for execution"""
def running_time(function, a, b, h):
  for i in range(a,b,h):
    start = curr_time()
    function( rand_arr(i) )
    end = curr_time()
    total_time = (end - start)
    print("Time for execution, n = {}: {}".format(i, total_time ))

print("\n\tTesting running time of mergesort on few random arrays...")
running_time(mergesort, 100, 105, 1)

"""Running Mergesort for large values"""

def running_times(function, a, b, h):
  times = []
  
  for i in range(a,b,h):
    start = curr_time()
    function( rand_arr(i) )
    end   = curr_time()
    total_time = (end - start)
    times.append(total_time)
    print("Time for execution, n = {}: {}".format(i, total_time))

  return times


"""Running for multiple random inputs"""
print("\n\tRunning algorithm for large values...")
a = 10
b = 10000
h = 20

# data to be plotted
x = np.arange(a, b, h)
y = x * np.log2(x)
z = running_times(mergesort, a,b,h)
print("ran for {} values from {} to {}".format((b-a)//h, a, b))


"""Plotting this data with nlogn"""
print("\n\tPlotting graph of running time...")
# plotting nlogn
plt.title("nlogn vs mergesort graph")
plt.xlabel("Input Size")
plt.ylabel("Running Times")

# plotting mergesort graph
plt.plot(x, z, color="blue")

#plotting nlogn graph
plt.plot(x, y, color="red")

plt.gca().legend(('mergesort','nlogn'))

#showing the combined plot
plt.show()

print("finished...")
