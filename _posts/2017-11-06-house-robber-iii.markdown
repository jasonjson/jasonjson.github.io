---
layout: post
title: 337 - House Robber III
date: 2017-11-06
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night. Determine the maximum amount of money the thief can rob tonight without alerting the police.**


```python
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

    return self.helper(root)[1]

    def helper(self, node):
        #[0] maximum profit without robbing node
        #[1] maxmimum profit with or without robbing node
        #if node is robbed, then node.left and node.right can not be robbed
        if not node:
            return [0, 0]
        left = self.helper(node.left)
        right = self.helper(node.right)
        return left[1] + right[1], max(left[1] + right[1], left[0] + right[0] + node.val)
```
