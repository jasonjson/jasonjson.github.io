#!/usr/bin/python
from listnode import ListNode

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if not head:
            return

        prev, right, fast = None, head, head
        while fast and fast.next:
            prev = right
            right = right.next
            fast = fast.next.next

        root = ListNode(right.val)
        if prev:
            prev.next = None
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(right.next)
            print root, root.left, root.right
        return root

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.sortedListToBST(ListNode([1,3])))
