# Problem Statement:
# Given an array of both positive and negative integers, the task is to find the count of subarrays with negative product. 



# For example :

# The input array is -2 , 3 , -4

# then the output is : 4

# Explanation :

# {-2},{-2,3},{3,-4},{-4}




# Input Format:
# First line has the size of the array.

# Second line has the elements of the array.




# Output Format:
# Print the count




# Constraints:
# 1 <= N <= 10^5




# Sample Input :
# 5
# -2 3 -4 -5 10

# Sample Output :
# 8


def negProdSubArr(arr, n): 
  positive = 1 
  negative = 0  
  for i in range(n): 
    arr[i] = 1 if arr[i] > 0 else -1
    if (i > 0):
      arr[i] *= arr[i - 1] 
    if (arr[i] == 1): 
      positive += 1 
    else:    
      negative += 1   
    # print(arr[i],positive,negative)  
    
  return (positive * negative)
  
  
n = int(input())
arr = list(map(int, input().split()))
print(negProdSubArr(arr, n))
