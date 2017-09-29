#!/usr/bin/python
# -*- coding: utf-8 -*-

from listnode import ListNode
class Solution(object):
    def reverse(self, head):
        if not head:
            return

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        last, curr = prev.next, prev.next.next
        while curr:
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
        return dummy.next

if __name__ == "__main__":
    solution = Solution()
    head = ListNode([1,2,3,4, 5, 6])
    import pprint
    pprint.pprint(solution.reverse(head))
