---
layout: post
title: 144 - Binary Tree Preorder Traversal
date: 2015-10-21 02:49:50.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, return the preorder traversal of its nodes' values.**


``` java
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root != null) {
            List<Integer> left = preorderTraversal(root.left);
            List<Integer> right = preorderTraversal(root.right);
            result.add(root.val);
            result.addAll(left);
            result.addAll(right);
        }
        return result;
    }
    //iterative!
    public ArrayList<Integer> preorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (root == null) {
            return result;
        }
        Stack<treenode> stack = new Stack<treenode>();
        stack.push(root);
        while (!stack.isEmpty()){
            TreeNode node = stack.pop();
            result.add(node.val);
            //push right node first, which comes out later
            if (node.right != null) stack.push(node.right);
            if (node.left != null) stack.push(node.left);
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        stack, ret = [root], []
        while stack:
            curr = stack.pop()
            ret.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return ret
```
