---
layout: post
title: Binary Search Tree Iterator
date: 2015-10-21 03:00:24.000000000 -04:00
categories:
- Binary Search Tree
- Data Structure
author: Jason
---
<p><strong><em>Design an iterator over a binary search tree with the following rules: Elements are visited in ascending order (i.e. an in-order traversal) next() and hasNext() queries run in O(1) time in average.</em></strong><br />


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
