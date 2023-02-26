# Problem Statement:
# Write a program to accept a number and perform a special reversing of the number, i.e. Do reverse only the odd digits alone in the given number. Constraints: Don't use arrays or strings or lists


# Input Format:
# Accept an integer as input  


# Output Format:
# Print the special reversed number


# Constraints:
# 1<=N<=10^18


# Sample Input 1:
# 79312468


# Sample Output 1:
# 13972468


# Sample Input 2:
# 12345


# Sample Output 2:
# 52341

def reverse_odd_digits(num):
  num_str=str(num)
  odd_digits=[]
  for i in range(len(num_str)):
    digit=int(num_str[i])
    if digit%2==1:
      odd_digits.append(digit)
  odd_digits.reverse()
  result_str=""
  for i in range(len(num_str)):
    digit=int(num_str[i]) 
    if digit%2==1:
      result_str+=str(odd_digits.pop(0))
    else:  
      result_str+=str(digit) 
  return int(result_str)
n=input()
print(reverse_odd_digits(n))
