---
layout: post
title: 328 - Odd Even Linked List
date: 2016-01-18 12:00:49.000000000 -05:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes. You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.


``` java
public class Solution {
    public static ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;
        int index = 1;
        ListNode prev = head, curr = prev.next;
        while (curr.next != null) {
            index++;
            if (index % 2 == 0) {
                ListNode front = curr.next;
                curr.next = front.next;
                front.next = prev.next;
                prev.next = front;
                prev = front;
            } else {
                curr = curr.next;
            }
        }
        return head;
    }
}
```

``` python
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        prev, curr = head, head.next
        index = 1
        while curr.next:
            index += 1
            if index % 2 == 0:
                front = curr.next
                curr.next = front.next
                front.next = prev.next
                prev.next = front
                prev = front
            else:
                curr = curr.next
        return head
```

```cpp
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        ListNode* prev = head;
        ListNode* curr = head->next;
        int index = 1;
        while (curr->next) {
            index += 1;
            if (index % 2 == 0) {
                ListNode* tmp = curr->next;
                curr->next = tmp->next;
                tmp->next = prev->next;
                prev->next = tmp;
                prev = tmp;
            } else {
                curr = curr->next;
            }
        }
        return head;
    }
    };
```
