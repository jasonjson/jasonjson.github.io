---
layout: post
title: 215 - Kth Largest Element in an Array
date: 2015-10-21 02:26:27.000000000 -04:00
tags:
- Leetcode
categories:
- Sorting
author: Jason
---
**Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element. For example, given [3,2,1,5,6,4] and k = 2, return 5.**


``` java
class Solution {
    //param k : description of k
    //param numbers : array of numbers
    //return: description of return
    public int kthLargestElement(int k, ArrayList<Integer> numbers) {
        // write your code here
        if (numbers == null || numbers.size() == 0) return 0;

        return helper(k, numbers, 0, numbers.size() - 1);
    }

    public int helper(int k, ArrayList<Integer> numbers, int start, int end) {
        int lo = start, hi = end, pivot = end;
        while (lo <= hi) {
            while (lo <= hi && numbers.get(lo) < numbers.get(pivot)) {
                lo ++;
            }
            while (lo <= hi && numbers.get(hi) >= numbers.get(pivot)) {
                hi --;
            }
            if (lo <= hi) {
                Collections.swap(numbers, lo, hi);
            }
        }
        Collections.swap(numbers, lo, pivot);
        if (lo == numbers.size() - k) {
            return numbers.get(lo);
        } else if (lo > numbers.size() - k) {
            return helper(k, numbers, start, lo - 1);
        } else {
            return helper(k, numbers, lo + 1, end);
        }
    }
};
```

``` python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        return self.helper(nums, k, 0, len(nums) - 1)

    def helper(self, nums, k, start, end):
        lo, hi, pivot = start, end, end
        while lo < hi:
            if nums[lo] < nums[pivot]:
                lo += 1
                continue
            if nums[hi] >= nums[pivot]:
                hi -= 1
                continue
            nums[lo], nums[hi] = nums[hi], nums[lo]
        nums[lo], nums[pivot] = nums[pivot], nums[lo]
        if lo == len(nums) - k:
            return nums[lo]
        elif lo > len(nums) - k:
            return self.helper(nums, k, start, lo - 1)
        else:
            return self.helper(nums, k, lo + 1, end)
```
