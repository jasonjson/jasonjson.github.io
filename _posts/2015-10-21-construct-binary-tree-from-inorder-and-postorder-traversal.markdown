---
layout: post
title: Construct Binary Tree from Inorder and Postorder Traversal
date: 2015-10-21 02:55:48.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1462551527;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:272;}i:1;a:1:{s:2:"id";i:47;}i:2;a:1:{s:2:"id";i:258;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
