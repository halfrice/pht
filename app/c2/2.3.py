# Delete Middle Node
# Implement an algorithm to delete a node in the middle (i.e., any node but 
# the first and last node, not necessarily the exact middle) of a singly
# linked list, give only access to that node.
# EXAMPLE
# Input: the node c from the linked list a -> b -> c -> d -> e -> f
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f

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

  def remove(self,data):
    node = self.head
    prev = None
    while node:
      if node.data == data and prev:
        prev.next = node.next
      elif node.data == data and not prev:
        self.head = node.next
      prev = node
      node = node.next

  def print(self):
    node = self.head
    while node:
      print(node.data,end=' ')
      node = node.next
    print(' ')

  def print_backwards(self):
    stack = ''
    node = self.head
    while node:
      stack = node.data+' '+stack
      node = node.next
    print(stack)

  def merge(self,l2):
    node = self.head
    node2 = l2.head
    while node:
      print(node,node2)
      target = node.next
      target2 = node2.next

      node2.next = node.next
      node.next = node2
      node = target
      node2 = target2


l1 = LinkedList()
l1.add('w')
l1.add('t')
l1.add('f')
l1.add('x')

# l2 = LinkedList()
# l2.add('l')
# l2.add('m')
# l2.add('a')
# l2.add('o')

l1.print()
l1.remove('w')
l1.print()
l1.remove('x')
l1.print()
# l2.print()

# l1.merge(l2)
# l1.print()
# l1.print_backwards()

