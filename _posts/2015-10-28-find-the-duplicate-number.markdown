---
layout: post
title: 287 - Find the Duplicate Number
date: 2015-10-28 14:16:38.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.**


[Read more](http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number)
二分枚举答案范围，使用鸽笼原理进行检验
* 根据鸽笼原理，给定n + 1个范围[1, n]的整数，其中一定存在数字出现至少两次。
* 假设枚举的数字为 n / 2, 遍历数组，若数组中不大于n / 2的数字个数超过n / 2，则可以确定[1, n /2]范围内一定有解. 否则可以确定解落在(n / 2, n]范围内。

```java
public class Solution {
    public int findDuplicate(int[] nums) {
        if (nums == null || nums.length == 0) return -1;

        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2, count = 0;
            for (int n : nums) {
                if (n <= mid) {
                    count ++;
                }
            }
            if (count > mid) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
```

``` python
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid, count = (lo + hi) / 2, 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
```
