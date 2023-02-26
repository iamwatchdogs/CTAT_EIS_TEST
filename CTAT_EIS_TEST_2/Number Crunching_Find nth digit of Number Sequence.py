# Problem Statement:
# Description Write a program to find the nth digit of given number sequence 1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,...

# Example: 

# If n = 5, then the 5th digit of the sequence is 5

# If n = 15, then the 15th digit of the sequence is 2(where 2 is a part of 12)


# Input Format:
# Input contains an integer n 




# Output Format:
# Print the nth digit of the given sequence


# Constraints:
# 1<=n<=10^4


# Sample Input :
# 17


# Sample Output :
# 3

def findNthDigit(n):
  digit = base = 1
  while n > 9*base*digit:
    n -= 9*base*digit
    digit += 1
    base *= 10
  q, r = divmod(n-1,digit)
  return int(str(base+q)[r])
  
print(findNthDigit(int(input())))
