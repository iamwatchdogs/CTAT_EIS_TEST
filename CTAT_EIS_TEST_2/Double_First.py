# Problem Statement:
# Given Singly linked list code , Complete the function DFirst_unequalsecond(), such that it will check whether the next element is equal to current element if so then it will double the first Node element and remove the next Node for every Node in the list until no equal nodes present in the list.

# Note : If any new function is needed can be added in extra space.




# Input Format:
#  Get the elements until newline


# Output Format:
#  Display the list


# Constraints:
   


# Sample Input :
# 2 2 4 7 7 7 8 8 16 32


# Sample Output :
# 8 14 7 64

def DFirst_unequalsecond(lst):
  i = 0
  while i < len(lst) - 1: 
    if lst[i] == lst[i+1]:
      lst[i] *= 2       
      del lst[i+1]     
      i = max(i-1, 0)
    else:
      i += 1
  return lst

lst = list(map(int, input().split()))
lst = DFirst_unequalsecond(lst)
print(*lst)
