import unittest

# Palindrome

class Node:
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)

  def __eq__(self,other):
    return self.data == other.data

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

  def palindrome(self):
    node = self.head
    queue = ''
    stack = ''
    while node:
      queue += node.data
      stack = node.data+stack
      node = node.next
    print(queue,stack, queue == stack)

# li = LinkedList()
# li.add('r')
# li.add('a')
# li.add('c')
# li.add('e')
# li.add('c')
# li.add('a')
# li.add('r')
# li.print()
# li.palindrome()

# l2 = LinkedList()
# l2.add('S')
# l2.add('u')
# l2.add('r')
# l2.add('u')
# l2.add('u')
# l2.add('r')
# l2.add('u')
# l2.add('s')
# l2.print()
# l2.palindrome()

class Test(unittest.TestCase):
  def setUp(self):
    self.li = LinkedList()

  def test_add_s(self):
    self.li.add('s')
    self.li.add('u')
    self.li.add('u')
    self.li.add('s')
    self.li.print()
    # self.assertEqual(self.li, 's')


  # def test_palindrome_racecar(self):
  #   self.assertEqual(self.li.palindrome(), True)

if __name__ == '__main__':
  unittest.main()