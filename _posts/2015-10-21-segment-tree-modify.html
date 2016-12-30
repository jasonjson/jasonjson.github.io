---
layout: post
title: Segment Tree Modify
date: 2015-10-21 13:30:27.000000000 -04:00
type: post
published: true
status: publish
categories:
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465371211;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1030;}i:1;a:1:{s:2:"id";i:488;}i:2;a:1:{s:2:"id";i:936;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>For a Maximum Segment Tree, which each node has an extra value max to store the maximum value in this node's interval. Implement a modify function with three parameter root, index and value to change the node's value with [start, end] = [index, index] to the new given value. Make sure after this change, every node in segment tree still has the max attribute with the correct value.</em></strong></p>
<p>[expand title = "code1"]</p>
<pre>
public class Solution {
    /**
     *@param root, index, value: The root of segment tree and 
     *@ change the node's value with [index, index] to the new given value
     *@return: void
     */
    public void modify(SegmentTreeNode root, int index, int value) {
        if (root == null) return;
        if (root.start == index && root.end == index) {
            root.max = value;
            return;
        }
        int mid = (root.start + root.end) / 2;
        if (root.start <= index && index <= mid) {
            modify(root.left, index, value);
        } else if (mid < index && index <= root.end) {
            modify(root.right, index, value);
        }
        root.max = Math.max(root.left.max, root.right.max);
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="code2"]</p>
<pre>
public class Solution {
    /**
     *@param root, index, value: The root of segment tree and 
     *@ change the node's value with [index, index] to the new given value
     *@return: void
     */
    public void modify(SegmentTreeNode root, int index, int value) {
        // write your code here
        if (root == null) return;
        
        if(root.start == index && root.end == index) {
            root.max = value;
        }
        
        int mid = (root.start + root.end) / 2;
        if (index <= mid) {//modify left subtree, The left child of node A has start=A.left, end=(A.left + A.right) / 2.
            modify(root.left, index, value);
        } else {//modify right subtree, The right child of node A has start=(A.left + A.right) / 2 + 1, end=A.right
            modify(root.right, index, value);
        }
        if (root.left != root.right) {
            //bug, missing if, nullpointer, no need to update the leaf node 
            root.max = Math.max(root.left.max, root.right.max);
        }
    }
}
</pre>
<p>[/expand]</p>
