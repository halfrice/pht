from node import Node

class LinkedList:
  def __init__(self,head=None):
    self.head = head

  def is_empty(self):
    return self.head == None

  def add(self,data):
    node = Node(data)
    node.next = self.head
    self.head = node

  def remove(self,data):
    node = self.head
    prev_node = None
    found = False
    while node:
      if node.data == data:
        found = True
      else:
        prev_node = node
        node = node.next
    if not prev_node:
      self.head = node.next
    else:
      prev_node.next = node.next

  def print(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next
    print('\n')




li = LinkedList()
li.add(3)
li.add(8)
li.add(2)
li.add(5)
li.print()
