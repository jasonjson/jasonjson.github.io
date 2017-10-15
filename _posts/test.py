#!/usr/bin/python

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return self.helper(nums, 0, len(nums) - 1, k)

    def helper(self, nums, lo, hi, k):
        left, right, pivot = lo, hi, hi
        while left <= right:
            while left <= right and nums[left] < nums[pivot]:
                left += 1
            while left <= right and  nums[right] >= nums[pivot]:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[left], nums[pivot] = nums[pivot], nums[left]
        if left ==  len(nums) - k:
            return nums[lo]
        elif left > len(nums) - k:
            return self.helper(nums, lo, left - 1, k)
        else:
            return self.helper(nums, left + 1, hi, k)
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.findKthLargest([2, 1], 1))
