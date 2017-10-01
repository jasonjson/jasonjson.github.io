---
layout: post
title: 61 - Rotate List
date: 2015-10-21 14:35:50.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Given a list, rotate the list to the right by k places, where k is non-negative.**


``` java
public class Solution {
    /**
     * @param head: the List
     * @param k: rotate to the right k places
     * @return: the list after rotation
     */
    public ListNode rotateRight(ListNode head, int k) {
        // write your code here
        if (head == null) return null;
        int len = getSize(head);
        k %= len;
        ListNode prev = head, right = head;
        for (int i = 0; i < len - k; i++) {//we can find the nth node from the end use len directly, since we already calculate it
            prev = right;
            right = right.next;
        }
        if (right == null) { //!!important corner case
            return head;
        }
        prev.next = null;
        ListNode tail = right;
        while (tail.next != null) {
            tail = tail.next;
        }
        tail.next = head;
        return right;
    }
    public int getSize(ListNode head) {
        int count = 0;
        while (head != null) {
            head = head.next;
            count ++;
        }
        return count;
    }
}
```

``` python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return

        slow, fast = head, head
        for i in xrange(k):
            fast = fast.next
                if not fast:
                    fast = head

        while fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None
        return head
```
