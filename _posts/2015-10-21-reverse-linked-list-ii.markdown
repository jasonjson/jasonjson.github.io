---
layout: post
title: Reverse Linked List II
date: 2015-10-21 02:46:31.000000000 -04:00
type: post
published: true
status: publish
categories:
- LinkedList
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467949298;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:592;}i:1;a:1:{s:2:"id";i:601;}i:2;a:1:{s:2:"id";i:246;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Reverse a linked list from position m to n.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int index = 1;
        ListNode prev = dummy;
        while (index < m) {
            index ++;
            prev = prev.next;
        }
        ListNode last = prev.next, curr = last.next;
        while (index < n) {
            index ++;
            last.next = curr.next;
            curr.next = prev.next;
            prev.next = curr;
            curr = last.next;
        }
        return dummy.next;
    }
}
</pre>
<p>[/expand]</p>
