Knapsack Problem


"""Defining 0/1 Knapsack Algorithm"""

def knapSack_01(W, wt, val, n):
	K = []
	for i in range(n + 1):
		K.append([0 for w in range(W + 1)])
			
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i - 1] <= w:
				K[i][w] = max(val[i - 1] 
				        + K[i - 1][w - wt[i - 1]], K[i - 1][w])
			else:
				K[i][w] = K[i - 1][w]

	res = K[n][W]
	print(res)
	
	w = W
	for i in range(n, 0, -1):
		if res <= 0:
			break
		if res == K[i - 1][w]:
			continue
		else:
			print(wt[i - 1], end=' ')
			res = res - val[i - 1]
			w = w - wt[i - 1]
	print('')
	return res

# Driver code
val = [ 60, 100, 120 ]
wt = [ 10, 20, 30 ]
W = 50
n = len(val)
	
knapSack_01(W, wt, val, n)

Output:
220
30 20

"""Calling 0/1 Knapsack Function"""

# testing the knapsack code
val = [50,100,150,200]
wt  = [ 8, 16, 32, 40]
n = len(val)
MaxW = 64
 
knapSack_01(MaxW, wt, val, n)

output :
350
40 16 8
	
"""Second Test Case"""
val = [53,100,120]
wt = [10,20,30]
MaxW = 50
n = len(val)

knapSack_01(MaxW, wt, val, n)

output :
220
30 20 

'''Defining Fractional Knapsack'''

def knapSack_frac(weights, values, MaxWt):
	p_w_r = []            #price_weight_ratio
	
	for weight, value in zip(weights, values):
		p_w_r.append(value/weight)
		
	ans = 0
	remaining_wt = MaxWt
	print("fully included: ",end='')
	
	for pair in sorted(zip(weights, values, p_w_r),
                 key=lambda x: x[2], reverse = True):

		if remaining_wt == 0:
			break
			
		if pair[0] <= remaining_wt:
		    print(pair[0],end=' ')
		    ans += pair[1]
		    remaining_wt -= pair[0]
			
		elif pair[0] > remaining_wt:
		    print("\nfractionally included :",pair[0])
		    ratio = pair[0]/remaining_wt
		    ans  += pair[1] / ratio
		    remaining_wt = 0
	
	print("total profit:",ans)
	return ans

"""Calling Fractional Knapsack Function"""
# testing the knapsack code
weights = [15, 10, 40, 15, 30]
values  = [45, 36, 17, 28, 19]
capacity = 100
ans = knapSack_frac(weights, values, capacity)
print(ans)

Output :
fully included: 10 15 15 30 
fractionally included : 40
total profit: 140.75

'''Second Test'''
weights = [30]
values  = [100]
capacity = 10
ans = knapSack_frac(weights, values, capacity)
print(ans)

Output : 
fully included: 
fractionally included : 30
total profit: 33.333333333333336

