---
layout: post
title: 143 - Reorder List
date: 2015-10-21 02:47:42.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Given a singly linked list L: L0 - L1 - ...  - Ln-1 - Ln, reorder it to: L0 - Ln - L1 - Ln-1 - L2 - Ln-2 - ... You must do this in-place without altering the nodes' values.**

``` java
public class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) return;
        //bug1 forget to check head.next
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        //find the mid node
        //for 1 2 3 4 5 6, slow = 4; reverse 5 6
        //left = 1 2 3 4 right = 6 5; merge: 1 6 2 5 3 4; 3 4 is already in correct positions
        //for 1 2 3 4 5 6 7, slow = 4, reverse 5 6 7
        //left = 1 2 3 4 right 7 6 5, merge 1 7 2 6 3 5 4; 4 is already in correct position
        right = reverse(slow.next);
        slow.next = null;//clear the tail nodes in left part
        ListNode curr = head;
        //insert right nodes to left nodes, do this in place
        while (right != null) {
            ListNode curr_next = curr.next;
            ListNode right_next = right.next;
            right.next = curr.next;
            curr.next = right;
            right = right_next;
            curr = curr_next;
        }
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
```

``` python
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        left, right = head, self.reverse(slow.next)
        slow.next = None
        while right:
            left_next = left.next
            right_next = right.next
            right.next = left.next
            left.next = right
            left = left_next
            right = right_next

    def reverse(self, head):
        ret = None
        while head:
            next_node = head.next
            head.next = rev
            rev = head
            head = next_node
        return ret
```
