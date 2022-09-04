"""Bucket Sort Algorithm"""

import random, timeit, matplotlib.pyplot as plt

"""Defining Insertion Sort"""
def INSERTION_SORT(Arr):
    for i in range(1, len(Arr)):
        key = Arr[i]
        j = i-1
        while j >=0 and key < Arr[j] :
                Arr[j+1] = Arr[j]
                j -= 1
        Arr[j+1] = key
    return Arr


"""Defining Bucket Sort"""
def BUCKET_SORT(Arr):
    buckets = []

    # take n empty buckets
    for i in range(len(Arr)):
        buckets.append([])

    # Multiply by 10 to get first digit and insert in that bucket
    for element in Arr:
        index = int(10 * element)
        if index < len(buckets):
        	buckets[index].append(element)
        else:
        	print("index, len",index, len(buckets))

    # Sort the elements of each bucket
    for i in range(len(Arr)):
        buckets[i] = INSERTION_SORT(buckets[i])

    # Get the sorted elements
    k = 0
    for i in range(len(Arr)):
        for j in range(len(buckets[i])):
            Arr[k] = buckets[i][j]
            k += 1


"""Function to return array of random numbers of required sizes"""
def rand_arr(n):
  #uniform distribution of elements in the range 0 to 1
  return [random.uniform(0,1) for i in range(n)]

print("\n\tGenerating Random arrays of different sizes...")
for n in range(15,20):
  print("random array of size",n,":",rand_arr(n))
  
def curr_time(): return timeit.default_timer()*scale

"""testing Bucket Sort"""

print("\n\tRunning BucketSort on few examples")
for i in range(3):
	n = 10
	A = rand_arr(n)
	print("original array : ", A)
	BUCKET_SORT(A)
	print("sorted array   : ", A ,'\n')
	
"""Graphing"""
arr=[]
n_val =[] 
running_time=[] 
scale = 16000

print("\n\tRunning algorithm for large values...")

for n in range(11,8000,30):
  A = rand_arr(n)

  print("Original array is: ", A ,"\n") 
  start = curr_time()
  
  BUCKET_SORT(A)
  
  end = curr_time()
  print("Sorted array is: ", A ,"\n")
  
  total_time = (end - start)
  n_val.append(n)
  running_time.append(total_time) 
  print("Time for execution, n = {}: {}".format(n, total_time ))


"""Plotting this data with n"""

print("\n\tPlotting graph of running time...")
# plotting n
plt.title("Bucket Sort graph")
plt.xlabel("Input Size")
plt.ylabel("Running Times")

# plotting Bucket sort graph
plt.plot(n_val, running_time, color="blue")

#plotting n graph
plt.plot(n_val, n_val, color="red")

plt.gca().legend(('BucketSort','n'))

#showing the combined plot
plt.show()

print("finished...")
