---
layout: post
title: Palindrome Linked List
date: 2015-10-21 14:45:44.000000000 -04:00
type: post
published: true
status: publish
categories:
- LinkedList
- Palindrome
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468137798;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:238;}i:1;a:1:{s:2:"id";i:1850;}i:2;a:1:{s:2:"id";i:242;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement a function to check if a linked list is a palindrome.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;
        
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        if (fast != null) {
            slow = slow.next;
        }
        slow = reverse(slow);
        while (slow != null) {
            if (head.val != slow.val) {
                return false;
            }
            slow = slow.next;
            head = head.next;
        }
        return true;
    }    
    public ListNode reverse(ListNode head) {
        ListNode rev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = rev;
            rev = head;
            head = next;
        }
        return rev;
    }
}
</pre>
<p>[/expand]</p>
