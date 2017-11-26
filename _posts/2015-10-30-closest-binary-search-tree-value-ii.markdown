---
layout: post
title: 272 - Closest Binary Search Tree Value II
date: 2015-10-30 11:29:11.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target. Given target value is a floating point. You may assume k is always valid, that is: k ≤ total nodes. You are guaranteed to have only one unique set of k values in the BST that are closest to the target.**


``` java
public class Solution {
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        List<Integer> result = new ArrayList<Integer>();
        if (root == null) return result;

        Stack<treenode> stack = new Stack<treenode>();
        while (!stack.isEmpty() || root != null) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (result.size() < k) {
                    result.add(root.val);
                } else if (Math.abs(root.val - target) < Math.abs(result.get(0) - target)) {
                    result.remove(0);
                    result.add(root.val);
                } else {//后面的数更大 不需要考虑 关键是找到中间k个数
                    break;
                }
                root = root.right;
            }
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []

        stack, ret = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if len(ret) < k:
                    ret.append(root.val)
                elif abs(root.val - target) < abs(ret[0] - target):
                    del ret[0]
                    ret.append(root.val)
                else:
                    break
                root = root.right
        return ret
```
