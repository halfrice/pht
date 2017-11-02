# Partition
# Write code to partition a linked list around a value x, such that all nodes 
# less than x come before all nodes greater than or equal to x. If x is contained 
# within the list, the values of x only need to be after the elements less than x. 
# The partition element x can appear anywhere in the "right partition"; it does 
# not need to appear between the left and right partitions.
# EXAMPLE
# Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

class Node:
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self,head=None):
    self.head = head

  def add(self,data):
    node = Node(data)
    node.next = self.head
    self.head = node

  def print(self):
    node = self.head
    while node:
      print(node.data,end=' -> ')
      node = node.next
    print(' ')

  def partition(self,num):
    node = self.head
    left = None
    right = None
    while node:
      if node.data < num:
        # left = 
      node = node.next


li = LinkedList()
li.add(1)
li.add(2)
li.add(10)
li.add(5)
li.add(8)
li.add(5)
li.add(3)
li.print()
