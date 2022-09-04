"""Counting Sort Algorithm"""

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
# plotting n
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

