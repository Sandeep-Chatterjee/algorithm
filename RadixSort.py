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

