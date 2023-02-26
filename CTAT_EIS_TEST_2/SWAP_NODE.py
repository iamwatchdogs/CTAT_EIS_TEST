# Problem Statement:
# Given Singly linked list code , Complete the functionSwapK_Node(), such that it will swap the node that are placed in the kth position, with the node where it begins.


# Input Format:
#   Get the integer as a input until newline


# Output Format:
#  Display the list


# Constraints:
#  \n is represent to end of the i/p


# Sample Input :
# 1 2 3 4 5 6 7
# 3


# Sample Output :
# 3 2 6 4 5 1 7


# My code:

class Node:  
  def __init__(self, data, next=None):     
    self.data = data 
    self.next = next
    
class LinkedList:    
  def __init__(self, *args, **kwargs):   
    self.head = Node(None)  
    
  def push(self, data):       
    node = Node(data)      
    node.next = self.head    
    self.head = node    
    
  def printList(self):   
    node = self.head   
    while node.next is not None: 
      print(node.data, end=" ")    
      node = node.next   
      
  def countNodes(self): 
    count = 0       
    node = self.head   
    while node.next is not None:
      count += 1       
      node = node.next      
      return count      
      
  def swapKth(self, k):
    n = self.countNodes()
    if n < k:           
      return
    
    current_node = self.head
    prev_node = None    
    i = 1    
    while current_node and i != k:  
      prev_node = current_node     
      current_node = current_node.next   
      i += 1        
    
    kth_node = current_node  
    prev_kth_node = prev_node 
    while current_node.next:  
      current_node = current_node.next    
    last_node = current_node 
    
    prev_kth_node.next = self.head        
    temp = self.head.next     
    self.head.next = kth_node.next      
    kth_node.next = temp     
    last_node.next = kth_node
    self.head = kth_node

llist = LinkedList()    
l = list(map(int,input().split()))
for i in l[::-1]:  
  llist.push(i)   
k = int(input())
for i in range(-1, len(l), k): 
  if i == -1:
    continue
  llist.swapKth(i)
llist.printList()

# working code
l = list(map(int,input().split()))
k = int(input())
for i in range (len(l),0,-1):
  if (i+1)%k == 0:
    l[0],l[i] = l[i],l[0]
for i in l:
  print(i,end=' ')

# Input:
# 1 2 3 4 5 6 7
# 3

# Expected Output:
# 3 2 6 4 5 1 7

# Actual Output:
# 1 2 3 4 5 6 7
