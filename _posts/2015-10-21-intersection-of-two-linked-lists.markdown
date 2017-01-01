---
layout: post
title: Intersection of Two Linked Lists
date: 2015-10-21 14:46:15.000000000 -04:00
type: post
published: true
status: publish
categories:
- LinkedList
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"b52187fdc06e97354ec0d5271cfb5b8f";a:2:{s:7:"expires";i:1468233363;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1848;}i:1;a:1:{s:2:"id";i:216;}i:2;a:1:{s:2:"id";i:222;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Write a program to find the node at which the intersection of two singly linked lists begins.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        ListNode A = headA, B = headB;//must create two new node, can't change headA headB
        while (A != B) {
            A = A != null ? A.next : headB;// A = A.next = null ?....wrong!!
            B = B != null ? B.next : headA;
            //必须走到null不然就在headA前加上了node形成无限循环
            //if there is no intersection, the loop stops when both A and B gets to null
            //the length of two list should be the same now!
        }
        return A;
    }
}
</pre>
<p>[/expand]</p>
