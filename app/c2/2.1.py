# Remove Dups
# Write code to remove duplicate from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?

class Node:
  def __init__(self,data=None,test=None,next=None):
    self.data = data
    self.test = test
    self.next = next

class LinkedList:
  def __init__(self,head=None):
    self.head = head

  def add(self,data,test=None):
    node = Node(data,test)
    node.next = self.head
    self.head = node

  def print(self):
    node = self.head
    while node:
      t = str(node.test) if node.test else ''
      print(node.data+t,end=' ')
      node = node.next
    print(' ')

  def print_backwards(self):
    s = ''
    node = self.head
    while node:
      s = node.data+' '+s
      node = node.next
    print(s)

  def remove_dups(self,data):
    node = self.head
    prev_node = None
    found_node = None

    # find the node to keep, store it and move to the next node
    while not found_node:
      if node.data == data:
        found_node = node 
      prev = node
      node = node.next

    # find and skip over any duplicate nodes until a non-dup is found
    found_dup = False
    while node:
      if node.data == data:
        found_dup = True
      elif node.data != data and found_dup: 
        prev.next = node
        found_dup = False
      else:
        prev = node
      node = node.next

li = LinkedList()
li.add('w')
li.add('t')
li.add('f',1)
li.add('f',2)
li.add('b',3)
li.add('o',3)
li.add('b',3)
li.add('f',4)
li.add('f',5)
li.add('x')
li.print()
li.remove_dups('f')
li.print()

