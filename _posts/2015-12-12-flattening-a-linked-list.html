---
layout: post
title: Flattening a Linked List
date: 2015-12-12 10:28:11.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- LinkedList
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467606797;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:246;}i:1;a:1:{s:2:"id";i:222;}i:2;a:1:{s:2:"id";i:43;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a linked list where every node represents a linked list and contains two pointers of its type:<br />
(i) Pointer to next node in the main list (we call it ‘right’ pointer in below code)<br />
(ii) Pointer to a linked list where this node is head (we call it ‘down’ pointer in below code).<br />
All linked lists are sorted.Write a function flatten() to flatten the lists into a single linked list.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
class Solution {
    class ListNode {
        ListNode next, right;
        int val;
        public ListNode(int val) {
            this.val = val;
            next = null;
            right = null;
        }
    }
    public ListNode flatten(ListNode head) {
        if (head == null || head.right == null) return head;
        /*while (head.right != null) {
            ListNode next = head.right.right;
            head = merge(head, head.right);
            head.right = next;
        }*/
        return merge(head, flatten(head.right));
    }

    public ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        curr.next = l1 == null ? l2 : l1;
        return dummy.next;
    }
}
</pre>
<p>[/expand]</p>
