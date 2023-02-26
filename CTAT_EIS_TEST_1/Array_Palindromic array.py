# Problem Statement:
# Description Given a binary array arr, the task is to find the minimum number moves/swaps required to make the array palindromic



# For example:

# Input: arr[] = {1, 0, 0, 0, 0}

# Output: 1

# Explanation:

# The 0 at index 4 can be replaced by 1.




# Input Format:
# The input contains the size and the array values.




# Output Format:
# Print the number of flips required to make the array palindrome.

# If it is not possible to make the array palindromic then print "Not possible to make palindromic array"

 


# Constraints:
# 1 <= N <= 10^6


# Sample Input :
# 10
# 1 0 1 0 1 1 1 1 0 0


# Sample Output :
# 1

def min_swaps(s):
  n = len(s) 
  i = 0   
  j = n - 1  
  count = 0 
  while (i <= j):    
    if (s[i] == s[j]):   
      i += 1   
      j -= 1  
      continue
    else:     
      i += 1   
      j -= 1 
      count += 1
  return count//2
  
def can_be_a_palindromic_array (l):
  n = len(l)
  if n%2 == 0:
    return sum(l)%2 == 0
  else:
    return sum(l)%2 == 1

n = int(input())
l = list(map(int,input().split()))
res = min_swaps(l)
print(res if can_be_a_palindromic_array(l) else 'Not possible to make palindromic array')
