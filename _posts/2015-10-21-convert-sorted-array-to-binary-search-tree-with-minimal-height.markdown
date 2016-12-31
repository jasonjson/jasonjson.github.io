---
layout: post
title: Convert Sorted Array to Binary Search Tree With Minimal Height
date: 2015-10-21 02:59:05.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465832105;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:290;}i:1;a:1:{s:2:"id";i:47;}i:2;a:1:{s:2:"id";i:936;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a sorted (increasing order) array, Convert it to create a binary tree with minimal height.</em></strong><br />
[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
