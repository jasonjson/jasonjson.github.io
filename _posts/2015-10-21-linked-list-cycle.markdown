---
layout: post
title: Linked List Cycle
date: 2015-10-21 02:45:22.000000000 -04:00
categories:
- LinkedList
author: Jason
---
<p><strong><em>Given a linked list, determine if it has a cycle in it. Follow up:<br />

Can you solve it without using extra space?</em></strong><br />

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
