---
layout: post
title: 369 - Plus One Linked List
date: 2018-02-27
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer. You may assume the integer do not contain any leading zero, except the number 0 itself. The digits are stored such that the most significant digit is at the head of the list.**


```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not head:
            return
        dummy = last_node = ListNode(0)
        dummy.next = head
        while head:
            if head.val < 9:
                last_node = head
            head = head.next

        last_node.val += 1
        while last_node.next:
            last_node.next.val = 0
            last_node = last_node.next
        return dummy if dummy.val == 1 else dummy.next

```
