---
layout: post
title: 141 - Linked List Cycle
date: 2015-10-21 02:45:22.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Given a linked list, determine if it has a cycle in it.**


``` java
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        ListNode curr = head;
        ListNode runner = head;
        while(runner != null && runner.next != null) {
            head = head.next;
            runner = runner.next.next;
            if (runner == head) return true;
            //if there is cycle, this can end the while loop
            //if there is no cycle, the loop will ends automatically
            //since runner will gets to null
        }
        return false;
    }
}
```

``` python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```
