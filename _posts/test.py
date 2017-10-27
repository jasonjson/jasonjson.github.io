class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        seq = [0] * len(nums)
        seq[0] = nums[0]
        size = 1
        for i in xrange(1, len(nums)):
            if nums[i] <= seq[0]:
                seq[0] = nums[i]
            elif nums[i] > seq[size - 1]:
                seq[size] = nums[i]
                size += 1
            else:
                seq[self.helper(nums, 0, size - 1, nums[i])] = nums[i]
            print seq
        return size
    def helper(self, nums, lo, hi, target):
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return hi

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.lengthOfLIS([4,10,4,3,8,9]))
