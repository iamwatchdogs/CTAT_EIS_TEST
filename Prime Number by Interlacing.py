# Problem Statement:
# Write a program to take two integers as input , interlace as per the description and check if the interlaced number is a prime number. Note: interlace a given numbers by combine digits of both numbers together as a single number as 1st digit of 1st number and 1st digit of 2nd number followed by 2nd digit of 1st number and 2nd digit of 2nd number and so on(left to rigit ). for example, Example : 2133 9127 Interlaced : 29113237 Prime Check : Prime Number



# Input Format:
# Two space separated integer values as input


# Output Format:
# %d and %d Interlaced is %d is a Prime Number  (or) %d and %d Interlaced is %d is Not a Prime Number


# Constraints:
# 1 <= N1,N2 <= 10^9


# Sample Input 1:
# 3489 1356


# Sample Output 1:
# 3489 and 1356 Interlaced is 31438596 is Not a Prime Number


# Sample Input 2:
# 1111 10011


# Sample Output 2:
# 1111 and 10011 Interlaced is 111010111 is a Prime Number

def prime(n):
  for i in range(2,int(n**0.5)+1):
    if (n%i==0):
      return 'Not a Prime Number'
  else:
    return 'a Prime Number'
n,m=map(str,input().split())
min1=min(len(n),len(m))
k="".join(y for x in zip(n,m) for y in x)+n[min1:]+m[min1:]
print(n+" and "+m+" Interlaced is "+k+" is "+prime(int(k)))
