# Problem Statement:
# Given collection of strings found the common words among each string and print those words in a lexicographically decreasigly sorted.


# Input Format:
# First line contains an integer 'N'- number of strings. 

# The next N lines will have respective input strings.


# Output Format:
# Print the common words among the strings line by line as lexicographically decreasigly sorted.




# Constraints:
# The maximum length of any string can be 400.

# Input strings are made up of lower case characters.

# 1 <= N <= 20




# Sample Input :
# 5
# i hope there is no snow tomorrow how does this work do you have a pen
# how long will it take i did not know there was milk in the refrigerator do you have a pencil
# i always wondered what was in there how many cars are there do you have a notebook
# i know there is truth to what you are saying how much money do you have do you have a bank account
# how old are you i never knew there is a way out how was your exam do you have a bike

# Sample Output :
# you
# there
# i
# how
# have
# do
# a

n = int(input())
res = set(input().split())

for i in range(n-1):
  line = set(input().split())
  res = res & line

for i in sorted(res, reverse=True):
  print(i)
