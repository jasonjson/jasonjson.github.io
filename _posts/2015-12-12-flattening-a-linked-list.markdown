---
layout: post
title: OA - Flattening a Linked List
date: 2015-12-12 10:28:11.000000000 -05:00
tags:
- OA
categories:
- LinkedList
author: Jason
---
**Given a linked list where every node represents a linked list and contains two pointers of its type:**
* Pointer to next node in the main list (we call it ‘right’ pointer in below code)
* Pointer to a linked list where this node is head (we call it ‘down’ pointer in below code).
**All linked lists are sorted. Write a function to flatten the lists into a single sorted linked list.**


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

``` python
class Solution(object):
    def flatten(self, head):
        if not head or not head.right:
            return head

        return self.merge(head, self.flatten(head.right))

    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
```
