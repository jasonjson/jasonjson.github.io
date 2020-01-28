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
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0, 0
            left = helper(node.left)
            right = helper(node.right)
            return node.val + left[1] + right[1], max(left) + max(right)
        return max(helper(root))
```
