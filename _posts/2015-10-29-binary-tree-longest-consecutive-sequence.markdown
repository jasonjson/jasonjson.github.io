---
layout: post
title: 298 - Binary Tree Longest Consecutive Sequence
date: 2015-10-29 10:37:39.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, find the length of the longest consecutive sequence path. The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).**


``` java
public class Solution {
    int result = 0;
    public int longestConsecutive(TreeNode root) {
        if (root == null) return 0;
        helper(root);
        return result;
    }
    public int helper(TreeNode root) {
        if (root == null) return 0;
        int left = helper(root.left);
        int right = helper(root.right);
        int max_left = (root.left != null && root.val + 1 == root.left.val) ? left + 1 : 1;
        int max_right = (root.right != null && root.val + 1 == root.right.val) ? right + 1: 1;
        int local = Math.max(max_left, max_right);
        result = Math.max(result, local);//global max
        return local;
    }
}
```

``` python
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ret = [0]
        self.helper(root, ret)
        return ret[0]

    def helper(self, root, ret):
        if not root:
            return 0
        left_max = self.helper(root.left, ret)
        right_max = self.helper(root.right, ret)
        if root.left and root.left.val == root.val + 1:
            left_max += 1
        else:
            left_max = 1
        if root.right and root.right.val == root.val + 1:
            right_max += 1
        else:
            right_max = 1
        local_max = max(left_max, right_max)
        ret[0] = max(ret[0], local_max)
        return local_max
```
