"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class SegmentTreeNode:
    def __init__(self, start, end, sums):
        self.start = start
        self.end = end
        self.sums = sums
        self.left = None
        self.right = None

class Solution:
    """
    @param: A: An integer array
    """
    def __init__(self, A):
        # do intialization if necessary
        self.root = self.build(A, 0, len(A) - 1)

    def build(self, A, start, end):
        root = SegmentTreeNode(start, end, 0)
        if start == end:
            root.sums = A[start]
        else:
            mid = (start + end) / 2
            root.left = self.build(A, start, mid)
            root.right = self.build(A, mid + 1, end)
            root.sums = root.left.sums + root.right.sums
        return root
    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        # write your code here
        return self.query_helper(self.root, start, end)

    def query_helper(self, root, start, end):
        if not root:
            return 0
        if root.start == start and root.end == end:
            return root.sums
        mid = (root.start + root.end) / 2
        if start > mid:
            return self.query_helper(root.right, start, end)
        elif end < mid:
            return self.query_helper(root.left, start, end)
        else:
            return self.query_helper(root.left, start, mid) + self.query_helper(root.right, mid + 1, end)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        # write your code here
        self.modify_helper(self.root, index, value)

    def modify_helper(self, root, index, value):
        if not root:
            return
        if root.start == index and root.end == index:
            root.sums = value
            return
        mid = (root.start + root.end) / 2
        if index <= mid:
            self.modify_helper(root.left, index, value)
        else:
            self.modify_helper(root.right, index, value)
        root.sums = root.left.sums + root.right.sums

if __name__ == "__main__":
    solution = Solution([1,2,7,8,5])
    solution.modify(0, 4)
    print solution.query(0, 1)
