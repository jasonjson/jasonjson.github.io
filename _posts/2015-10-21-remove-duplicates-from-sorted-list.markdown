---
layout: post
title: Remove Duplicates from Sorted List
date: 2015-10-21 02:42:57.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Given a sorted linked list, delete all duplicates such that each element appear only once.**


``` java
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        //if (head == null) return null; bug1 no need this, if head is null, we just return it.
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        ListNode curr = head;
        ListNode prev = null;
        while (curr != null) {
            if (!map.containsKey(curr.val)) {
                map.put(curr.val, 1);
                prev = curr;
            } else {
                prev.next = curr.next;
            }
            curr = curr.next;
        }
        return head;
    }

    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr = head;
        while (curr != null && curr.next != null) {
            if (curr.next.val == curr.val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return head;
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return

        prev = head
        while prev:
            curr = prev.next
            while curr and curr.val == prev.val:
                curr = curr.next
            prev.next = curr
            prev = curr
        return head

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
```
