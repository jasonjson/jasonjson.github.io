---
layout: post
title: 333 - Largest BST Subtree
date: 2016-02-23 22:38:07.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.**


``` java
public class Solution {
    public int largestBSTSubtree(TreeNode root) {
        int[] result = helper(root);
        return result[1];
    }
    public int[] helper(TreeNode root) {
        int[] result = new int[5];
        //result[0]: is BST? result[2] : total number of nodes, result[3]: maximum value, result[4] minimum value
        result[0] = 1; result[3] = Integer.MIN_VALUE; result[4] = Integer.MAX_VALUE;
        if (root == null) return result;
        int[] result_left = helper(root.left);
        int[] result_right = helper(root.right);
        if (result_left[0] == 0 || result_right[0] == 0 || root.val >= result_right[4] || root.val <= result_left[3]) {
            result[0] = 0;
        }//root is larger than the biggest node in left subtree and smaller than smallest node in right subtree
        result[2] = result_left[2] + result_right[2] + 1;
        result[1] = result[0] == 1 ? result[2] : Math.max(result_left[1], result_right[1]);
        result[3] = Math.max(root.val, Math.max(result_left[3], result_right[3]));
        result[4] = Math.min(root.val, Math.min(result_left[4], result_right[4]));
        return result;
    }
}
```

``` python
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, 0, float('inf'), float('-inf')
            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)
            n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
            #N is the size of the largest BST in the tree.
            #If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
            return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
        return dfs(root)[0]
```
