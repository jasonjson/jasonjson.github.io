---
layout: post
title: 94 - Binary Tree Inorder Traversal
date: 2015-10-21 02:50:09.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Inorder traversal a binary tree**


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: Inorder in ArrayList which contains node values.
     */
    public ArrayList<integer> inorderTraversal(TreeNode root) {
        ArrayList<integer> result = new ArrayList<integer>();
        if (root != null) {
            ArrayList<integer> left = inorderTraversal(root.left);
            ArrayList<integer> right = inorderTraversal(root.right);
            result.addAll(left);
            result.add(root.val);
            result.addAll(right);
        }
        return result;
    }
    //iterative
    public ArrayList<integer> inorderTraversal(TreeNode root) {
        ArrayList<integer> result = new ArrayList<integer>();
        Stack<treenode> stack = new Stack<treenode>();

        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                //when root gets to null, pop the stack and move to the right child
                root = stack.pop();
                result.add(root.val);
                root = root.right;
            }
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ret, stack = [], []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ret.append(root.val)
                root = root.right
        return ret
```
