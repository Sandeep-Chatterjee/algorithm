import random, timeit
import matplotlib.pyplot as plt
import numpy as np

print("\n\tChecking utility functions")
"""function to adjust both strings to same length"""
def fitlen(x, y):
    m, n = len(x), len(y)
    if (m < n):
        x = '0' * (n - m) + x
    else:
        y = '0' * (m - n) + y
    return x, y


"""function to convert decimal to binary string using bin()"""
a,b = 3, 4
s = 104000
def to_bin(a): return str(bin(abs(a))[2:])
x = to_bin(a)
y = to_bin(b)
fitlen(x,y)
print("binary of",a,b,"=",x,y)
print("binary of",s,"=",to_bin(s))

"""function to return current time"""
def curr_time(): return timeit.default_timer()*s

"""addition of two binary strings"""
def add(x, y):
    if len(x) != len(y):
        x, y = fitlen(x, y)
    assert len(x) == len(y), "length is not same. "
    result = ""
    carry = 0
    for i in range(len(x) - 1, -1, -1):
        a = int(x[i])
        b = int(y[i])
        val = (a ^ b) ^ carry  # sum of (a,b,c) bits
        result = str(val) + result
        carry = (a & b) | (a & carry) | (b & carry)
    if carry:
        result = '1' + result
    return result
print('adding 101 and 110 =',add('101', '110'))

"""Divide and Conquer multiplication using Gauss formula"""
def multiply(x, y):
      """ given x and y are string, binary values returns multiplied value as a integer. """
      x, y = fitlen(x, y)
      n = len(x)
      if n == 0: return 0
      if n == 1: return int(x) & int(y)

      # len(xL): n // 2, len(xR): (n - n // 2)
      xL, xR = x[:n // 2], x[n // 2:]
      yL, yR = y[:n // 2], y[n // 2:]

      # each term required in gaussian formula
      p1 = multiply(xL, yL)
      p2 = multiply(xR, yR)
      p3 = multiply(add(xL, xR), add(yL, yR))
      return p1 * (1 << 2 * (n - n // 2)) + (p3 - p1 - p2) * (1 << (n - n // 2)) + p2

print("\n\tChecking the divide and conquer multiply")
for i in range(2,10):
  for j in range(i,10,3):
    print("multiply ",i,j,":",multiply(to_bin(i),to_bin(j)),"=",i*j)
    
def run(x, y):
    start = curr_time()
    ans = multiply(x, y)
    end = curr_time()
    total_time = (end-start)
    return ans, total_time

print("\n\tRunning for large inputs")
num_exp, start, stop = 100, 100, 1000

t1, t2 , t3 = [0]*num_exp, [0]*num_exp, [0]*num_exp
sizes = list(np.linspace(start, stop, num=num_exp))

print("running for random binary strings of")
for i, size in enumerate(sizes):
    size = int(size)
    a, b = random.getrandbits(size), random.getrandbits(size)
    x, y = to_bin(a), to_bin(b)
    #gt = a * b
    t1[i], t2[i] = (size)**1.5, (size)**1.6
    ans2, t3[i]  = run(x, y)
    print("size = {}, time = {}".format(size,round(t3[i])))
    
print("\n\n\tran for",num_exp,"values of bin strings of sizes",start,"to",stop)
print("collected running time of",num_exp,"calls")

print("\n\tPlotting this data...")
plt.xlabel('size')
plt.ylabel('time')
plt.title("Time Complexity Analysis")
plt.plot(sizes, t3, '-r', label='div n conq')
plt.plot(sizes, t1, '-g', label="n^1.5")
plt.plot(sizes, t2, '-b', label="n^1.6")
plt.legend(loc='upper left')
plt.show()

print("finished...")
