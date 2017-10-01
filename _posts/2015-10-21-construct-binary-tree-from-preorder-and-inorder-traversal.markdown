---
layout: post
title: Construct Binary Tree from Preorder and Inorder Traversal
date: 2015-10-21 02:55:10.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Construct a binary tree from preorder and inorder traversal.**


``` java
//basic idea: the first element in preorder is the root
//the root int inorder divides the inorder into left subtree and right subtree, which are also subtrees in preorder
//we find the index of root in inorder and get the length of left subtree, recursively get root.left
public class Solution {
    /**
     *@param preorder : A list of integers that preorder traversal of a tree
     *@param inorder : A list of integers that inorder traversal of a tree
     *@return : Root of a tree
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null || preorder.length == 0 || inorder.length == 0 || preorder.length != inorder.length) return null;

        return buildTreeUtil(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
    }
    public int findIndex(int[] nums, int start, int end, int target) {
        for (int i = start; i <= end; i ++) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }
    public TreeNode buildTreeUtil(int[] preorder, int pre_start, int pre_end, int[] inorder, int in_start, int in_end) {
        if (pre_start > pre_end || in_start > in_end) return null;
        int root_val = preorder[pre_start];//not preorder[0] !!!
        TreeNode root = new TreeNode(root_val);
        int index = findIndex(inorder, in_start, in_end, root_val);
        root.left = buildTreeUtil(preorder, pre_start + 1, pre_start + index - in_start, inorder, in_start, index - 1);
        root.right = buildTreeUtil(preorder, pre_start + index - in_start + 1, pre_end, inorder, index + 1, in_end);
        return root;
    }
}
```

``` python
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder or not inorder:
            return

        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def helper(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return
        root = TreeNode(preorder[pre_start])
        index = inorder.index(root.val)
        root.left = self.helper(preorder, pre_start + 1, pre_start + index - in_start, inorder, in_start, index - 1)
        root.right = self.helper(preorder, pre_start + index - in_start + 1, pre_end, inorder, index + 1, in_end)
        return root
```
