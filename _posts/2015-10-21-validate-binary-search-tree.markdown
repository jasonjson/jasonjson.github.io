---
layout: post
title: 98 - Validate Binary Search Tree
date: 2015-10-21 02:58:13.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, determine if it is a valid binary search tree (BST).**


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    public boolean isValidBST(TreeNode root) {
        // write your code here
        ArrayList<integer> array = new ArrayList<integer>();
        inorderTraversal(array, root);
        for(int i = 0; i < array.size() - 1; i++){
            if (array.get(i) >= array.get(i+1)) return false;
        }
        return true;
    }

    public void inorderTraversal(ArrayList<integer> array, TreeNode root){
        if(root == null) return;
        inorderTraversal(array, root.left);
        array.add(root.val);
        inorderTraversal(array, root.right);
    }
}
```

``` python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        stack = []
        prev = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                #prev might be 0, so cannot use if prev here
                if prev is not None and root.val <= prev:
                    return False
                prev = root.val
                root = root.right
        return True
```
