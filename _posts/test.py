#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        ret = sum(nums[:3])
        nums.sort()
        for i, num in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                if lo > i + 1 and nums[lo] == nums[lo - 1]:
                    lo += 1
                    continue
                if hi < len(nums) - 1 and nums[hi] == nums[hi + 1]:
                    hi -= 1
                    continue
                total = num + nums[lo] + nums[hi]
                print(num, nums[lo], nums[hi], total)
                if total == target:
                    return total
                elif total > target:
                    hi -= 1
                else:
                    lo += 1
                if abs(total - target) < abs(ret - target):
                    ret = total
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.threeSumClosest([-3,-2,-5,3,-4], -1))
