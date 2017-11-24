---
layout: post
title: 315 - Count of Smaller Numbers After Self
date: 2015-12-07 18:21:09.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].**


``` java
public class Solution {
    public List<Integer> countSmaller(int[] nums) {
        List<Integer> result = new ArrayList<Integer>();
        if (nums == null || nums.length == 0) return result;

        List<Integer> sorted = new ArrayList<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            int index = find(sorted, nums[i]);
            result.add(index);
            sorted.add(index,nums[i]);
        }
        Collections.reverse(result);//!!don't forget to reverse
        return result;
    }

    public int find(List<Integer> sorted, int val) {
        //if (sorted.size() == 0) return 0; no need
        int lo = 0, hi = sorted.size() - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (sorted.get(mid) == val) {
                while (mid - 1 >= 0 && sorted.get(mid - 1) == val) {
                    mid--;
                }
                return mid;
            } else if (sorted.get(mid) < val) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}
```

``` python
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort, ret = [], []
        for num in reversed(nums):
            index = self.query(sort, num)
            sort.insert(index, num)
            ret.append(index)
        return list(reversed(ret))

    def query(self, sort, num):
        lo, hi = 0, len(sort) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if sort[mid] == num:
                while mid - 1 >= 0 and sort[mid - 1] == num:
                    mid -= 1
                return mid
            elif sort[mid] < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
```
