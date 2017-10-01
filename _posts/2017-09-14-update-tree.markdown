---
layout: post
title: Update Tree
date: 2017-09-14
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a tree node with n depth. Each node has value either 1 or 0. Find the lowest level node with value 1 and set all the above nodes to 0, Dont change the node in the same level.**

```python
#
# Example:
#
#
       # 1
     # 1   0
    # 0 0 1 1
  # 0 0 0    1 0
       # 0
     # 0  0
    # 0 0 0 0
 # 0 0 0    1 0
#
#
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

class Solution(object):
    def update_tree(self, root):
        """
        :type root: tree node
        """

        level_nodes = level_order_traversal(root)
        found = False
        for current_level in reversed(level_nodes):
            for node in current_level:
                if found:
                    node.val = 0
                elif node.val == 1:
                    found = True
                    break

def level_order_traversal(root):
    level_nodes = []
    current_level = [root]
    while current_level:
        next_level = []
        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level_nodes.append(current_level)
        current_level = next_level
    return level_nodes

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(0)
    node3 = Node(1)
    node4 = Node(0)
    node5 = Node(1)
    node6 = Node(0)
    node7 = Node(1)
    node8 = Node(0)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node2.right = node5
    node5.left = node6
    node6.right = node7
    node5.right = node8

    solution = Solution()
    solution.update_tree(node1)
    import pprint
    pprint.pprint(level_order_traversal(node1))





```
