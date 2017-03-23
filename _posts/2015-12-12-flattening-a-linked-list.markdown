---
layout: post
title: Flattening a Linked List
date: 2015-12-12 10:28:11.000000000 -05:00
tags:
- Algorithm
categories:
- Brain teaser
- LinkedList
author: Jason
---
<p><strong><em>Given a linked list where every node represents a linked list and contains two pointers of its type:</p>

(i) Pointer to next node in the main list (we call it ‘right’ pointer in below code)</p>
(ii) Pointer to a linked list where this node is head (we call it ‘down’ pointer in below code).</p>
All linked lists are sorted.Write a function flatten() to flatten the lists into a single linked list.</em></strong></p>
``` java
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
```
