import unittest

class Node:
  def __init__(self, name):
    self.children = []
    self.name = name

  def addChild(self, name):
    self.children.append(Node(name))
    return self

  #O(v+e) time | O(v) space
  def depthFirstSearch(self, array):
    array.append(self.name)
    for child in self.children:
      child.depthFirstSearch(array)
    return array
  
  def depthFirstSearch2(self, array):
    stack = [self]
    array.append(self)
    while len(stack) > 0:
      curr = stack.pop()
      if curr not in array:
        for child in curr.children:
          stack.append(child)
      array.append(curr)
    return array.reverse()

  
  

def dfs (graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
    

test1 = Node("A")
test1.addChild("B").addChild("C")
test1.children[0].addChild("D")

test2 = Node("A")
test2.addChild("B").addChild("C").addChild("D").addChild("E")
test2.children[1].addChild("F")

test3 = Node("A")
test3.addChild("B")
test3.children[0].addChild("C")
test3.children[0].children[0].addChild("D").addChild("E")
test3.children[0].children[0].children[0].addChild("F")

test4 = Node("A")
test4.addChild("B").addChild("C").addChild("D")
test4.children[0].addChild("E").addChild("F")
test4.children[2].addChild("G").addChild("H")
test4.children[0].children[1].addChild("I").addChild("J")
test4.children[2].children[0].addChild("K")

test5 = Node("A")
test5.addChild("B").addChild("C").addChild("D").addChild("L").addChild("M")
test5.children[0].addChild("E").addChild("F").addChild("O")
test5.children[1].addChild("P")
test5.children[2].addChild("G").addChild("H")
test5.children[0].children[0].addChild("Q").addChild("R")
test5.children[0].children[1].addChild("I").addChild("J")
test5.children[2].children[0].addChild("K")
test5.children[4].addChild("S").addChild("T").addChild("U").addChild("V")
test5.children[4].children[0].addChild("W").addChild("X")
test5.children[4].children[0].children[1].addChild("Y").addChild("Z")


class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(test1.depthFirstSearch2([]), ["A", "B", "D", "C"])

	def test_case_2(self):
		self.assertEqual(test2.depthFirstSearch2([]), ["A", "B", "C", "F", "D", "E"])

	def test_case_3(self):
		self.assertEqual(test3.depthFirstSearch2([]), ["A", "B", "C", "D", "F", "E"])

	def test_case_4(self):
		self.assertEqual(test4.depthFirstSearch2([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])

	def test_case_5(self):
		self.assertEqual(test5.depthFirstSearch2([]), ["A", "B", "E", "Q", "R", "F", "I", "J", "O", "C", "P", "D", "G", "K", "H", "L", "M", "S", "W", "X", "Y", "Z", "T", "U", "V"])


if __name__ == "__main__":
	unittest.main()
