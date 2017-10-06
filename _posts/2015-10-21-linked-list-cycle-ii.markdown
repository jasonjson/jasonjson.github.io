---
layout: post
title: 142 - Linked List Cycle II
date: 2015-10-21 02:45:45.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Given a linked list, return the node where the cycle begins. If there is no cycle, return null.**


``` java
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @return: The node where the cycle begins.
     *           if there is no cycle, return null
     */
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) return null;

        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
        }
        return null;
    }
}
```

``` python
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #distance between the head location and entry location is equal to the distance
        #between the meeting location and the entry location
        if not head:
            return

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return
```
