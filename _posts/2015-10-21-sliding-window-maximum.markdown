---
layout: post
title: 239 - Sliding Window Maximum
date: 2015-10-21 13:01:03.000000000 -04:00
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
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dq = collections.deque()
        ret = []
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            if i + 1 >= k:
                ret.append(nums[dq[0]])
        return ret
```
