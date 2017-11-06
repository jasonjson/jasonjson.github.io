class SegmentNode(object):
    def __init__(self, lo, hi, sums):
        self.lo = lo
        self.hi = hi
        self.sums = sums
        self.left = None
        self.right = None
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        ret = [0]
        root = self.build_tree(nums, 0, len(nums) - 1, lower, upper, ret)
        return ret[0]

    def build_tree(self, nums, lo, hi, lower, upper, ret):
        if lo == hi:
            if nums[lo] >= lower and nums[lo] <= upper:
                ret[0] += 1
            return SegmentNode(lo, hi, nums[lo])
        elif lo > hi:
            return
        else:
            root = SegmentNode(lo, hi, 0)
            mid = (lo + hi) / 2
            root.left = self.build_tree(nums, lo, mid, lower, upper, ret)
            root.right = self.build_tree(nums, mid + 1, hi, lower, upper, ret)
            root.sums = root.left.sums + root.right.sums
            if root.sums >= lower and root.sums <= upper:
                ret[0] += 1
            return root
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.countRangeSum([0,-3,-3,1,1,2], 3, 5))
