---
layout: post
title: 239 - Sliding Window Maximum
date: 2020-01-15
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving**

``` java
public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: The maximum number inside the window at each moving.
     */
    public ArrayList<Integer> maxSlidingWindow(int[] nums, int k) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (nums == null || nums.length == 0) return result;

        PriorityQueue<Integer> max = new PriorityQueue<Integer>(10, Collections.reverseOrder());
        int start = 0;
        for (int i = 0; i < nums.length; i++) {
            max.offer(nums[i]);
            if (i + 1 >= k) {
                result.add(max.peek());
                max.remove(nums[start++]);
            }
        }
        return result;
    }
}
```

``` python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        queue = []
        ret = []
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if i - queue[0] == k:
                queue.pop(0)
            if i + 1 >= k:
                ret.append(nums[queue[0]])
        return ret
```
