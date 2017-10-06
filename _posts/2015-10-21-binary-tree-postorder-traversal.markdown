---
layout: post
title: 145 - Binary Tree Postorder Traversal
date: 2015-10-21 02:50:25.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, return the postorder traversal of its nodes' values.**


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: Postorder in ArrayList which contains node values.
     */
    public ArrayList<Integer> postorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (root == null) return result;

        Stack<treenode> stack = new Stack<treenode>();
        TreeNode prev = null;
        stack.push(root);
        while (!stack.isEmpty()) {
            root = stack.peek();
            boolean nochildren = false;
            if (root.left == null && root.right == null) {
                nochildren = true;
            }
            boolean childrenvisited = false;
            if (prev != null && (root.left == prev || root.right == prev)) {
                childrenvisited = true;
            }
            if (nochildren || childrenvisited) {
                prev = stack.pop();
                result.add(root.val);
            } else {
                if (root.right != null) {
                    stack.push(root.right);
                }
                if (root.left != null) {
                    stack.push(root.left);
                }
            }
        }
        return result;
    }
}
```
``` java
public class Solution {
    public ArrayList<Integer> postorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (root != null) {
            ArrayList<Integer> left = postorderTraversal(root.left);
            ArrayList<Integer> right = postorderTraversal(root.right);
            result.addAll(left);
            result.addAll(right);
            result.add(root.val);
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack, ret = [root], []
        prev = None
        while stack:
            curr = stack[-1]
            no_children = True if not curr.left and not curr.right else False
            visit_children = True if prev and (curr.left == prev or curr.right == prev) else False
            if no_children or visit_children:
                curr = stack.pop()
                ret.append(curr.val)
                prev = curr
            else:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
        return ret
```
