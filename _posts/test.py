#!/usr/bin/python

from listnode import ListNode
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        fast = right = head
        prev = None
        while fast and fast.next:
            prev = right
            fast = fast.next.next
            right = right.next
        prev.next = None
        curr, right = head, self.reverse(right)
        print curr, right
        while curr:
            next_node = curr.next
            curr.next = right
            right = right.next
            right.next = next_node
            curr = next_node
        import pprint
        pprint.pprint(head)

    def reverse(self, head):
        rev = None
        while head:
            next_node = head.next
            head.next = rev
            rev = head
            head = next_node
        return rev

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.reorderList(ListNode([1,2,3,4])))
