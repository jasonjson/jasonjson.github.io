class SegmentNode(object):

    def __init__(self, lo, hi, sums):
        this.lo = lo
        this.hi = hi
        this.sums = sums
        this.left = None
        this.right = None

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self.build(0, len(nums) - 1, nums)


    def build(self, lo, hi, nums):
        if lo > hi:
            return
        elif lo == hi:
            return SegmentNode(lo, hi, nums[lo])
        else:
            mid = (lo + hi) / 2
            root = SegmentNode(lo, hi, 0)
            root.left = self.build(lo, mid, nums)
            root.right = self.build(mid + 1, hi, nums)
            root.sums = root.left.sums + root.right.sums
            return root

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.update_node(self.root, i, val)

    def update_node(self, node, i, val):
        if node.lo == i and node.hi == i:
            node.sums = val
        else:
            mid = (node.lo + node.hi) / 2
            if i <= mid:
                update_node(node.left, i, val)
            else:
                update_node(node.right, i, val)
            node.sums = node.left.sums + node.right.sums


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sumRange(self.root, i, j)

    def sum_node(self, node, i, j):
        if node.lo == i and node.hi == j:
            return node.sums
        mid = (node.lo + node.hi) / 2
        if j <= mid:
            return self.sum_node(node.left, i, j)
        elif i > mid:
            return self.sum_node(node.right, i, j)
        else:
            return self.sum_node(node.left, i, mid) + self.sum_node(node.right, mid + 1, j)
