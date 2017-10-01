---
layout: post
title: 113 - Path Sum II
date: 2015-11-11 09:05:32.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.**


``` java
public class Solution {
    public List<List<integer>> pathSum(TreeNode root, int sum) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (root == null) return result;
        helper(root, new ArrayList<integer>(), sum, result);
        return result;
    }

    public void helper(TreeNode root, List<integer> path, int remain, List<List<integer>> result) {
        if (root == null) return;
        path.add(root.val);
        if (root.left == null && root.right == null && root.val == remain) {
            result.add(new ArrayList<integer>(path));//加进result的条件比较特殊,必须到了leaf且leaf的值等于remain
        }
        helper(root.left, path, remain - root.val, result);
        helper(root.right, path, remain - root.val, result);
        path.remove(path.size() - 1);
    }
}
```

``` python
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if not root:
            return []

        ret = []
        self.helper(root, sum, [], ret)
        return ret

    def helper(self, root, sum, curr, ret):
        if not root:
            return
        if not root.left and not root.right and root.val == sum:
            ret.append(curr + [root.val])
            return
        self.helper(root.left, sum - root.val, curr + [root.val], ret)
        self.helper(root.right, sum - root.val, curr + [root.val], ret)
```
