---
layout: post
title: 250 - Count Univalue Subtrees
date: 2015-11-02 08:49:03.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, count the number of uni-value subtrees. A Uni-value subtree means all nodes of the subtree have the same value with the root.**


``` java
public class Solution {
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) return 0;
        //if (root.left == null && root.right == null) return 1;
        int result = countUnivalSubtrees(root.left) + countUnivalSubtrees(root.right);
        if (isUnival(root)) result += 1;
        return result;

    }

    public boolean isUnival(TreeNode root) {
        if (root == null) return true;
        //if (root.left == null && root.right == null) return true;
        if (root.left != null && root.left.val != root.val) return false;
        if (root.right != null && root.right.val != root.val) return false;
        return isUnival(root.left) && isUnival(root.right);
    }
}
```

``` python
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ret = self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right)
        return ret + 1 if self.is_uni(root) else ret

    def is_uni(self, root):
        if not root:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.is_uni(root.left) and self.is_uni(root.right)
```
