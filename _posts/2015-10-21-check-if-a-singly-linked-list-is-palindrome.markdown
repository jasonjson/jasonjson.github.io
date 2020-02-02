---
layout: post
title: 234 - Palindrome Linked List
date: 2015-10-21 02:48:25.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
Given a singly linked list of integers, write a function that returns true if the given list is palindrome, else false.

``` python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(node):
            curr = None
            while node:
                next_node = node.next
                node.next = curr
                curr = node
                node = next_node
            return curr

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        rev_slow = reverse(slow)
        while rev_slow:
            if head.val != rev_slow.val:
                return False
            head = head.next
            rev_slow = rev_slow.next
        return True
```
