---
layout: post
title: Maximum Depth of Binary Tree
date: 2015-10-21 02:51:31.000000000 -04:00
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.**

``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: An integer.
     */
    public int maxDepth(TreeNode root) {
        // write your code here
        if(root == null) return 0;
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
```

``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: An integer.
     */
    public int maxDepth(TreeNode root) {
        // write your code here
        if (root == null) return 0;
        if (root.left == null) {
            return maxDepth(root.right) + 1;
        } else if (root.right == null) {
            return maxDepth(root.left) + 1;
        } else {
            return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
        }
    }
}
```

```python
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        left_dep = self.maxDepth(root.left)
        right_dep = self.maxDepth(root.right)
        return max(left_dep, right_dep) + 1
```
