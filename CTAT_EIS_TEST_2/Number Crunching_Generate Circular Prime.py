# Number Crunching_Generate Circular Prime





# Problem Statement:
# Write a program to generate circular prime numbers between the given range

# Example: circular numbers between 10  and 100 are 11 13 17 31 71 73 79 97




# Input Format:
# Input contains two integer


# Output Format:
# Print the circular prime numbers separated by space




# Constraints:
 


# Sample Input :
# 100 1000


# Sample Output :
# 113 131 197 199 311 337 373 719 733 919 971 991

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def rotate(n):
    s = str(n)
    return int(s[1:] + s[0])

def is_circular_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s)):
            return False
        s = str(rotate(s))
    return True


start, end = map(int, input().split())


circular_primes = []
for n in range(start, end+1):
    if is_circular_prime(n):
        circular_primes.append(n)
print(*circular_primes)

# Correct Answer:
def is_prime(n):
  if n < 2:     
    return False
  for i in range(2, int(n**0.5)+1):      
    if n % i == 0:   
      return False  
  return True
  
def rotate(n):
  s = str(n)
  return s[1:]+s[0]

def is_circular_prime(n):  
  s = str(n)
  for i in range(len(s)):   
    if not is_prime(int(s)):
      return False     
    s = str(rotate(s))
  return True

start, end = map(int, input().split())
circular_primes = []
for n in range(start, end+1): 
  if is_circular_prime(n):
    circular_primes.append(n)
print(*circular_primes)
