# Return Kth to Last
# Implement an algorithm to find the kth to last element of a singly linked list.

class Node:
  def __init__(self,data=None,next=None):
   self.data = data
   self.next = next

  def __str__(self):
    return str(self.data)

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
      print(node,end=' ')
      node = node.next
    print(' ')

  def print_backwards(self):
    s = ''
    node = self.head
    while node:
      s = node.data+' '+s
      node = node.next
    print(s) 

  def kth_to_last(self,k):
    node = self.head
    count = 1
    while node and count < k:
      node = node.next
      count += 1
    print(node.data)

li = LinkedList()
li.add('w')
li.add('t')
li.add('f')
li.add('f')
li.add('f')
li.add('x')
li.print()
li.kth_to_last(5)

