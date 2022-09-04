"""
# Heap Sort Algorithm
"""

import random
import timeit
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

"""Defining Heapsort"""
# The main function to sort an array of given size
def heapsort(arr):
  n = len(arr)
  buildMaxHeap(arr)
  # One by one extract elements and swap with root
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i] # swap
    heapify(arr, i, 0)


"""Function to return array of random numbers of required sizes"""
def rand_arr(n):
  return [random.randrange(100) for i in range(n)]
scale = 1400000

print("\n\tGenerating Random arrays of different sizes...")
for i in range(5,8):
  print("random array of size",i,":",rand_arr(i))
  
def curr_time():
  return timeit.default_timer()*scale
  
"""testing Mergesort"""
print("\n\tRunning HeapSort on few examples")
for i in range(3):
	array = rand_arr(10)
	print("original array : ", array)
	heapsort(array)
	print("sorted array   : ", array ,'\n')

"""Noting time for execution"""
def running_time(function, a, b, h):
  for i in range(a,b,h):
    start = curr_time()
    function( rand_arr(i) )
    end = curr_time()
    total_time = (end - start)
    print("Time for execution, n = {}: {}".format(i, total_time ))

print("\n\tTesting running time of heapsort on few random arrays...")
running_time(heapsort, 100, 105, 1)

"""Running Heapsort for large values"""

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
a = 1
b = 6000
h = 20

# data to be plotted
x = np.arange(a, b, h)
y = x * np.log2(x)
z = running_times(heapsort, a,b,h)
print("ran for {} values from {} to {}".format((b-a)//h, a, b))


"""Plotting this data with nlogn"""
print("\n\tPlotting graph of running time...")
# plotting nlogn
plt.title("nlogn vs heapsort graph")
plt.xlabel("Input Size")
plt.ylabel("Running Times")

# plotting mergesort graph
plt.plot(x, z, color="blue")

#plotting nlogn graph
plt.plot(x, y, color="red")

plt.gca().legend(('heapsort','nlogn'))

#showing the combined plot
plt.show()

print("finished...")
