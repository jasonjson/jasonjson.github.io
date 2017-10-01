---
layout: post
title: Construct Binary Tree from Inorder and Postorder Traversal
date: 2015-10-21 02:55:48.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Construct a binary tree from inorder and postorder traversal.**


``` java
//same ideas as above, except the last element in postorder is the root
//be careful about the length of subtrees, run some examples on paper
public class Solution {
    /**
     *@param inorder : A list of integers that inorder traversal of a tree
     *@param postorder : A list of integers that postorder traversal of a tree
     *@return : Root of a tree
     */
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        // write your code here
        if (inorder == null || postorder == null || inorder.length == 0 || postorder.length == 0 || inorder.length != postorder.length) {
            return null;
        }
        return buildTreeUtil(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
    }
    public int findIndex(int[] nums, int start, int end, int target) {
        for (int i = start; i <= end; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }
    public TreeNode buildTreeUtil(int[] inorder, int in_start, int in_end, int[] postorder, int post_start, int post_end) {
        if (in_start > in_end || post_start > post_end) return null;
        int root_val = postorder[post_end];
        TreeNode root = new TreeNode(root_val);
        int index = findIndex(inorder, in_start, in_end, root_val);
        // inorder not nums
        root.left = buildTreeUtil(inorder, in_start, index - 1, postorder, post_start, post_start + index - in_start - 1);
        root.right = buildTreeUtil(inorder, index + 1, in_end, postorder, post_start + index - in_start, post_end - 1);
        return root;
    }
}
```

``` python
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not inorder or not postorder:
            return

        return self.helper(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)

    def helper(self, postorder, post_start, post_end, inorder, in_start, in_end):
        if post_start > post_end or in_start > in_end:
            return
        root = TreeNode(postorder[post_end])
        index = inorder.index(root.val)
        root.left = self.helper(postorder, post_start, index - in_start + post_start - 1, inorder, in_start, index - 1)
        root.right = self.helper(postorder, index - in_start + post_start, post_end - 1, inorder, index + 1, in_end)
        return root
```
