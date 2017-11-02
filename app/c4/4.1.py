import unittest

class Node:
  def __init__(self, data=None):
    self.data = data
    self.disconnect()

  def disconnect(self):
    self.top = None
    self.left = None
    self.right = None

class BST:
  def __init__(self, root=None):
    self.root = root

  def get_root(self):
    return self.root

  def is_empty(self):
    return self.root == None

  def insert(self, data):
    new_node = Node(data)
    if not self.root:
      self.root = new_node
    else:
      node = self.root
      while node:
        if node.data > data:
          if not node.left:
            node.left = new_node
            new_node.top = node
            break
          node = node.left
        elif node.data <= data:
          if not node.right:
            node.right = new_node
            new_node.top = node
            break
          node = node.right
      return new_node

class Test(unittest.TestCase):
  def setUp(self):
    self.bst = BST()
    self.assertIsInstance(self.bst, BST)

  def test_get_root(self):
    self.assertEqual(self.bst.get_root(), None)

  def test_is_empty(self):
    self.assertTrue(self.bst.is_empty())

if __name__ == '__main__':
  unittest.main()