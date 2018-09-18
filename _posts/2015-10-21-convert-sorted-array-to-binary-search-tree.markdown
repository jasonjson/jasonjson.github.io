---
layout: post
title: 108 - Convert Sorted Array to Binary Search Tree
date: 2015-10-21 02:59:05.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given an array where elements are sorted in ascending order, convert it to a height balanced BST.**


``` java
public class Solution {
    /**
     * @param A: an integer array
     * @return: a tree node
     */
    public TreeNode sortedArrayToBST(int[] A) {
        if (A == null || A.length == 0) return null;
        return sortedArrayToBSTUtil(A, 0, A.length - 1);
    }

    public TreeNode sortedArrayToBSTUtil(int[] A, int start, int end) {
        if (start > end) return null;
        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(A[mid]);
        root.left = sortedArrayToBSTUtil(A, start, mid - 1);
        root.right = sortedArrayToBSTUtil(A, mid + 1, end);
        return root;
    }
}
```

``` python
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return

        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right):
        if left > right:
            return

        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, left, mid - 1)
        root.right = self.helper(nums, mid + 1, right)
        return root
```
