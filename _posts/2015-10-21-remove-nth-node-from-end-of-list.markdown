---
layout: post
title: Remove Nth Node From End of List
date: 2015-10-21 02:44:57.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1458557292;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:246;}i:1;a:1:{s:2:"id";i:216;}i:2;a:1:{s:2:"id";i:592;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a linked list, remove the nth node from the end of list and return its head.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return null;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy, slow = dummy;
        for (int i = 0; i <= n; i++) {
            curr = curr.next;
        }
        while (curr != null) {
            slow = slow.next;
            curr = curr.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }
}
</pre>
<p>[/expand]</p>
