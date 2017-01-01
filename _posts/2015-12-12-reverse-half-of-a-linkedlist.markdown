---
layout: post
title: Reverse half of a Linkedlist
date: 2015-12-12 11:38:04.000000000 -05:00
type: post
published: true
status: publish
categories:
- Data Structure
- LinkedList
- 面经
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468600764;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:218;}i:1;a:1:{s:2:"id";i:246;}i:2;a:1:{s:2:"id";i:238;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Reverse the latter half of a linkedlist.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
class Solution {
    public static void main(String[] args) {
        ListNode l1 = new ListNode(1);
        ListNode l2 = new ListNode(2);
        ListNode l3 = new ListNode(3);
        ListNode l4 = new ListNode(4);
        ListNode l5 = new ListNode(5);
        l1.next = l2; l2.next = l3; l3.next = l4; l4.next = l5;
        ListNode l6 = reverseHalf(l1);
        while (l6 != null) {
            System.out.println(l6.val);
            l6 = l6.next;
        }

    }
    public static ListNode reverseHalf(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode fast = head, slow = head, prev = slow;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = reverse(slow);
        return head;
    }
    public static ListNode reverse(ListNode head) {
        if (head == null || head.next == null) return head;
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
