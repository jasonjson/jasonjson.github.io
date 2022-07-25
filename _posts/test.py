#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            print(lo, hi, mid)
            if nums[mid] == target:
                print(1)
                left = right = mid
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left + 1, right - 1]
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return []

s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
