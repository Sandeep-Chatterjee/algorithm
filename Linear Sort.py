"”"Counting Sort Algorithm"""


import random, timeit, matplotlib.pyplot as plt


"""Defining Counting Sort"""


def COUNTING_SORT(A,B,k):
        C = []
        for i in range(k):
                C.append(0)
                # setting C[i] = 0
        
        for j in range(len(A)):
                C[A[j]] = C[A[j]] + 1
                # counts of number of elements
                
        for i in range(1,k):
                C[i] = C[i] + C[i-1]
                # number of elements less than or equal to element
                
        for j in range(len(A)-1, -1, -1):
                B[C[A[j]]-1] = A[j]
                C[A[j]] = C[A[j]] - 1
                # filling output array
                
"""Function to return array of random numbers of required sizes"""
def rand_arr(n, k):
  #the range of elements is 0 to k
  return [random.randrange(k) for i in range(n)]


print("\n\tGenerating Random arrays of different sizes...")
for n in range(15,20):
  k = n//10 + 10
  print("random array of size",n,":",rand_arr(n, k))
  
def curr_time(): return timeit.default_timer()*scale


"""testing CountingSort"""


print("\n\tRunning CountingSort on few examples")
for i in range(3):
        n = 10
        k = n//10 + 10
        A = rand_arr(n,k)
        B = [0]*len(A)
        print("original array : ", A)
        COUNTING_SORT(A,B,k)
        print("output array   : ", B ,'\n')
        
"""Graphing"""
arr=[]
n_val =[] 
running_time=[] 
scale = 100000


print("\n\tRunning algorithm for large values...")


for n in range(1,10000,50):
  k = n//10 + 10
  A = rand_arr(n,k)
  B = [0]*len(A)


  print("Input array is: ", A ,"\n") 
  start = curr_time()
  
  COUNTING_SORT(A,B,k)
  
  end = curr_time()
  print("Output array is:", B ,"\n")
  
  total_time = (end - start)
  n_val.append(n)
  running_time.append(total_time) 
  print("Time for execution, n = {}: {}".format(n, total_time ))




"""Plotting this data with n"""


print("\n\tPlotting graph of running time...")
# plotting n and counting sort
plt.title("Counting Sort graph")
plt.xlabel("Input Size")
plt.ylabel("Running Times")


# plotting counting sort graph
plt.plot(n_val, running_time, color="blue")


#plotting n graph
plt.plot(n_val, n_val, color="red")


plt.gca().legend(('CountingSort','n'))


#showing the combined plot
plt.show()


print("finished...")










Plot:


  



________________


"""Radix Sort Algorithm"""


import random, timeit, matplotlib.pyplot as plt


"""Defining Counting Sort"""


def COUNTING_SORT(A,B,k,d):
        #d meaning the digit by which to sort
        
        C = []
        for i in range(k):
                C.append(0)
                # setting C[i] = 0
        
        for j in range(len(A)):
                placeEl = (A[j] // (10**d)) % 10
                C[placeEl] = C[placeEl] + 1
                # counts of number of elements
                
        for i in range(1,k):
                C[i] = C[i] + C[i-1]
                # number of elements less than or equal to element
                
        for j in range(len(A)-1, -1, -1):
                placeEl = (A[j] // (10**d)) % 10
                
                C[placeEl] = C[placeEl] - 1
                B[C[placeEl]] = A[j]
                # filling output array
                
"""Defining Radix Sort"""


def RADIX_SORT(A,d):
        k = 10     #because sorting is only by digits 0-9
        for i in range(d):
                B = [0]*len(A)
                COUNTING_SORT(A,B,k,d)
                A = B
                
"""Function to return array of random numbers of required sizes"""
def rand_arr(n, d):
  #the range of elements is 0 to 10^d
  return [random.randrange(10**d) for i in range(n)]


print("\n\tGenerating Random arrays of different sizes...")
for n in range(15,20):
  print("random array of size",n,":",rand_arr(n, 8))
  
def curr_time(): return timeit.default_timer()*scale


        
"""Graphing"""
arr=[]
n_val =[] 
running_time=[] 
scale = 70000


print("\n\tRunning algorithm for large values...")


for n in range(1,10000,50):
  d = 8
  k = 10
  A = rand_arr(n,d)
  B = [0]*len(A)


  print("Initial array is: ", A ,"\n") 
  start = curr_time()
  
  RADIX_SORT(A,d)
  
  end = curr_time()
  print("Sorted array is: ", A ,"\n")
  
  total_time = (end - start)
  n_val.append(n)
  running_time.append(total_time) 
  print("Time for execution, n = {}: {}".format(n, total_time ))




"""Plotting this data with n"""


print("\n\tPlotting graph of running time...")
# plotting n
plt.title("Radix Sort graph")
plt.xlabel("Input Size")
plt.ylabel("Running Times")


# plotting radix sort graph
plt.plot(n_val, running_time, color="blue")


#plotting n graph
plt.plot(n_val, n_val, color="red")
plt.gca().legend(('RadixSort','n'))


#showing the combined plot
plt.show()


print("finished...")
Plot:
  



________________


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
        buckets[index].append(element)


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
scale = 10000


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




Plot: