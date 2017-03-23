---
layout: post
title: Output a sorted array from an equation
date: 2016-01-20 18:05:25.000000000 -05:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an equation y = ax^2 + bx + c, and sorted array X, output sorted Y</em></strong></p>


``` java

public class Solution {
    public static void main(String[] args) {
        int[] nums = {-4,-3,-2,-1,0,1,2,3,4};
        int[] result = getSorted(nums, 1, 2, 3);
        for (int n : result) {
            System.out.print(n + ",");
        }
    }
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
            double mid = -b / 2.0 * a;//以中轴为分界线
            List<integer> left = new ArrayList<>(), right = new ArrayList<>();
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
