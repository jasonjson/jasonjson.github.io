---
layout: post
title: Output a sorted array from an equation
date: 2016-01-20 18:05:25.000000000 -05:00
tags:
- OA
categories:
- Brain Teaser
author: Jason
---
**Given an equation y = ax^2 + bx + c, and sorted array X, output sorted Y.**


``` java

public class Solution {
    public static int[] getSorted(int[] nums, int a, int b, int c) {
        if (nums == null || nums.length == 0) return new int[]{};

        int n = nums.length;
        int[] result = new int[n];
        if (a == 0) {
            if (b > 0) {
                for (int i = 0; i < n; i++) {
                    result[i] = b * nums[i] + c;
                }
            } else {
                for (int i = 0, j = n - 1; i < n; i++) {
                    result[j--] = b * nums[i] + c;
                }
            }
        } else {
            double mid = - b / (2.0 * a);
            List<Integer> left = new ArrayList<>(), right = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                int val = a * nums[i] * nums[i] + b * nums[i] + c;
                if (nums[i] < mid) {
                    left.add(val);
                } else {
                    right.add(val);
                }
            }
            if (a > 0) {
                int k = 0, i = left.size() - 1, j = 0;
                while (i >= 0 && j < right.size()) {
                    result[k++] = left.get(i) < right.get(j) ? left.get(i--) : right.get(j++);
                }
                while (i >= 0) {
                    result[k++] = left.get(i--);
                }
                while (j < right.size()) {
                    result[k++] = right.get(j++);
                }
            } else {
                int k = 0, i = 0, j = right.size() - 1;
                while (i < left.size() && j >= 0) {
                    result[k++] = left.get(i) < right.get(j) ? left.get(i++) : right.get(j--);
                }
                while (i < left.size()) {
                    result[k++] = left.get(i++);
                }
                while (j >= 0) {
                    result[k++] = right.get(j--);
                }
            }
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def getSorted(self, nums, a, b, c):
        if not nums:
            return []

        if a == 0:
            ret = [b * num + c for num in nums]
            return ret if b > 0 else list(reversed(ret))

        mid = - b / (2.0 * a)
        left, right = [], []
        for num in nums:
            y = a * num * num + b * num + c
            if num < mid:
                left.append(y)
            else:
                right.append(y)
        ret = []
        if a > 0:
            i, j = len(left) - 1, 0
            while i >= 0 and j < len(right):
                if left[i] < right[j]:
                    ret.append(left[i])
                    i -= 1
                else:
                    ret.append(right[j])
                    j += 1
            while i >= 0:
                ret.append(left[i])
                i -= 1
            while j < len(right):
                ret.append(right[j])
                j += 1
        else:
            i, j = 0, len(right) - 1
            while i < len(left) and right >= 0:
                if left[i] < right[j]:
                    ret.append(left[i])
                    i += 1
                else:
                    ret.append(right[j])
                    j -= 1
            while i < len(left):
                ret.append(left[i])
                i += 1
            while j >= 0:
                ret.append(right[j])
                j -= 1
        return ret
```
