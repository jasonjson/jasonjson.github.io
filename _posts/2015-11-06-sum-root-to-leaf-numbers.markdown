---
layout: post
title: 129 - Sum Root to Leaf Numbers
date: 2015-11-06 22:04:46.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number. An example is the root-to-leaf path 1->2->3 which represents the number 123. Find the total sum of all root-to-leaf numbers.**


``` java
public class Solution {
    public int sumNumbers(TreeNode root) {
        if (root == null) return 0;

        List<String> result = new ArrayList<String>();
        helper(root, "", result);
        int sum = 0;
        for (String s : result) {
            sum += Integer.parseInt(s);
        }
        return sum;
    }

    public void helper(TreeNode root, String path, List<String> result) {
        if (root == null) {
            return;
        }
        if (root.left == null && root.right == null) {
            result.add(new String(path + String.valueOf(root.val)));
        }
        helper(root.left, path + String.valueOf(root.val), result);
        helper(root.right, path + String.valueOf(root.val), result);
    }
}
```

``` python
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        ret = []
        self.helper(root, [], ret)
        return sum([int(n) for n in ret])

    def helper(self, root, curr, ret):
        curr += [str(root.val)]
        if not root.left and not root.right:
            ret.append("".join(curr))
            return
        if root.left:
            self.helper(root.left, curr, ret)
            curr.pop()
        if root.right:
            self.helper(root.right, curr, ret)
            curr.pop()
```
