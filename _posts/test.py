#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        curr = self
        val_list = []
        while curr:
            val_list.append(str(curr.val))
            curr = curr.next
        return "->".join(val_list)

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

        import pdb
        pdb.set_trace()
        fast.next = head
        head = slow.next
        slow.next = None
        return head

if __name__ == "__main__":
    solution = Solution()
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h5 = ListNode(5)
    # h1.next = h2
    # h2.next = h3
    # h3.next = h4
    # h4.next = h5
    import pprint
    pprint.pprint(solution.rotateRight(h1, 0))
