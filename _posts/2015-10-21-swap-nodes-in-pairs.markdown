---
layout: post
title: Swap Nodes in Pairs
date: 2015-10-21 14:44:57.000000000 -04:00
type: post
published: true
status: publish
categories:
- LinkedList
tags: []
meta:
  _wpas_done_all: '1'
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1449407435;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:592;}i:1;a:1:{s:2:"id";i:244;}i:2;a:1:{s:2:"id";i:246;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a linked list, swap every two adjacent nodes and return its head.</em></strong></p>
<p>[expand title = "iterative"]</p>
<pre>
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while (prev.next != null && prev.next.next != null) {
            ListNode last = prev.next;
            ListNode curr = last.next;
            last.next = curr.next;
            curr.next = prev.next;
            prev.next = curr;
            prev = last;
        }
        return dummy.next;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title = "recursive"]</p>
<pre>
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode n1 = head, n2 = head.next;
        n1.next = n2.next;
        n2.next = n1;
        n1.next = swapPairs(n1.next);
        return n2;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public ListNode swapPairs(ListNode head) {
        // Write your code here
        if (head == null) return null;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        int i = 0;
        while (head != null) {
            i ++;
            if (i % 2 == 0) {
                prev = reverse(prev, head.next);
                head = prev.next;
            } else {
                head = head.next;
            }
        }
        return dummy.next;
    }
    public ListNode reverse(ListNode prev, ListNode next) {
        ListNode last = prev.next;
        ListNode curr = last.next;
        while (curr != next) {
            last.next = curr.next;
            curr.next = prev.next;
            prev.next = curr;
            curr = last.next;
        }
        return last;
    }
}
</pre>
<p>[/expand]</p>
