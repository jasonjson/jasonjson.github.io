#!/usr/bin/python

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        nums[:k-1] = reversed(nums[:k-1])
        nums[k:] = reversed(nums[k:])
        print nums
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.rotate([1,2,3,4,5,6,7],3))
