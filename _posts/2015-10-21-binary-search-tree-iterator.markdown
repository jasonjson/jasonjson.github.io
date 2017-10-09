---
layout: post
title: 173 - Binary Search Tree Iterator
date: 2015-10-21 03:00:24.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Design an iterator over a binary search tree with the following rules: Elements are visited in ascending order (i.e. an in-order traversal) next() and hasNext() queries run in O(1) time in average.**


``` java
public class BSTIterator {
    Stack<treenode> stack = new Stack<treenode>();
    public BSTIterator(TreeNode root) {
        if (root == null) return;
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode curr = stack.pop();
        int result = curr.val;
        if (curr.right != null) {
            curr = curr.right;
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
        }
        return result;
    }
}
```

``` python
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        curr = self.stack.pop()
        val = curr.val
        if curr.right:
            curr = curr.right
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return val
```
