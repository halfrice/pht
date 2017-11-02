# Sum Lists
# You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the 1's
# digit is at the end of the list. Write a function that adds the two
# numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

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
      print(node.data,end=' ')
      node = node.next
    print(' ')

  def sum_lists(self,linkedlist):
    node = self.head
    node2 = linkedlist.head
    node_sum = LinkedList()
    carry = 0
    while node and node2:
      su = int(node.data)+int(node2.data)+carry
      if su > 9: 
        su = abs(10-su)
        carry = 1
      else: 
        carry = 0
      node_sum.add(su)
      node = node.next
      node2 = node2.next
    if carry:
      node_sum.add(carry)
    node_sum.print()
    return node_sum

  def sum_lists_reverse(self,linkedlist):
    node = self.head
    node2 = linkedlist.head
    node_sum = LinkedList()
    stack = ''
    stack2 = ''
    carry = 0
    while node and node2:
      stack = str(node.data)+stack
      stack2 = str(node2.data)+stack2
      node = node.next
      node2 = node2.next
    while stack and stack2:
      su = int(stack[0])+int(stack2[0])+carry
      if su > 9:
        su = abs(10-su)
        carry = 1
      else: 
        carry = 0
      node_sum.add(su)
      stack = stack[1:]
      stack2 = stack2[1:]
    if carry:
      node_sum.add(carry)
    node_sum.print()
    return node_sum

n1 = LinkedList()
n1.add(6)
n1.add(1)
n1.add(7)
n1.print()
n2 = LinkedList()
n2.add(2)
n2.add(9)
n2.add(5)
n2.print()
n1.sum_lists(n2)

n3 = LinkedList()
n3.add(7)
n3.add(1)
n3.add(6)
n3.print()
n4 = LinkedList()
n4.add(5)
n4.add(9)
n4.add(2)
n4.print()
n3.sum_lists_reverse(n4)
