---
layout: post
title: Segmemt Tree Build II
date: 2015-10-21 13:29:13.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1455435895;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:499;}i:1;a:1:{s:2:"id";i:936;}i:2;a:1:{s:2:"id";i:485;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement a build method with a given array, so that we can create a corresponding segment tree with every node value represent the corresponding interval max value in the array, return the root of this segment tree.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     *@param A: a list of integer
     *@return: The root of Segment Tree
     */
    public SegmentTreeNode build(int[] A) {
        return build(0, A.length - 1, A);
    }
    
    public SegmentTreeNode build(int start, int end, int[]array) {//start and end are indexes of the array
        if(start > end) {
            return null;
        }
        SegmentTreeNode root = new SegmentTreeNode(start, end);
        if (start == end) {
            root.max = array[start];
        } else {
            int mid = (start + end) / 2;
            root.left = build(start, mid , array);
            root.right = build(mid + 1, end, array);
            root.max = Math.max(root.left.max, root.right.max);
        }
        return root;
    }
}
</pre>
<p>[/expand]</p>
