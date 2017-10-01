---
layout: post
title: Unique Binary Search Trees II
date: 2015-10-21 03:40:35.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.


``` java
public class Solution {
    /**
     * @paramn n: An integer
     * @return: A list of root
     */
    public List<treenode> generateTrees(int n) {
        // write your code here
        return generateTreesUtil(1, n);
    }

    public List<treenode> generateTreesUtil(int start, int end) {
        List<treenode> result = new ArrayList<treenode>();
        if (start > end) {
            result.add(null); //must deal with null TreeNode here, otherwise fail for n = 1
            return result;
        }
        for (int i = start; i <= end; i++) {//use i as root to construct BST
        //create all possible left subtree roots and right subtree roots
            List<treenode> leftTree = generateTreesUtil(start, i - 1);
            List<treenode> rightTree = generateTreesUtil(i + 1, end);
            for (TreeNode leftroot : leftTree) {
                for (TreeNode rightroot : rightTree) {
                //connect root to all possible subtree roots
                    TreeNode root = new TreeNode(i);
                    root.left = leftroot;
                    root.right = rightroot;
                    result.add(root);
                }
            }
        }
        return result;
    }
}
```

``` python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if not n:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]
        ret = []
        for i in xrange(start, end + 1):
            left_tree = self.helper(start, i - 1)
            right_tree = self.helper(i + 1, end)
            for r1 in left_tree:
                for r2 in right_tree:
                    root = TreeNode(i)
                    root.left = r1
                    root.right = r2
                    ret.append(root)
        return ret
```
