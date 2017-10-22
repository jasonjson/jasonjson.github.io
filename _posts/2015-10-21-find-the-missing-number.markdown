---
layout: post
title: 268 - Find the Missing Number
date: 2015-10-21 13:02:42.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.**


``` java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int findMissing(int[] nums) {
        int x1 = 0;
        for (int n : nums) {
            x1 ^= n;
        }
        int x2 = 0;
        for (int i = 0; i <= nums.length; i++) {
            x2 ^= i;
        }
        return x1 ^ x2;
    }
    public int findMissing(int[] nums) {
        // write your code here
        bucketSort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        return nums.length;
    }
    //bucket sort
    public void bucketSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] != i) {
                if (nums[i] == nums.length) {
                    break;
                } //nums[nums.length] out of bounds
                int nextNum = nums[nums[i]];
                nums[nums[i]] = nums[i];
                nums[i] = nextNum;
            }
        }
    }
}
```

``` python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        xor = 0
        for num in nums:
            xor ^= num
        for i in xrange(len(nums) + 1):
            xor ^= i
        return xor
```
