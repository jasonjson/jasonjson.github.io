---
layout: post
title: 47 - Permutations II
date: 2015-10-21 03:38:30.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given a list of numbers with duplicate number in it. Find all unique permutations.**


``` java
class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of unique permutations.
     */
    public ArrayList<ArrayList<Integer>> permuteUnique(ArrayList<Integer> nums) {
        // write your code here
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (nums == null || nums.size() == 0) return result;

        Collections.sort(nums);
        ArrayList<Integer> list = new ArrayList<Integer>();
        boolean[] visited = new boolean [nums.size()];
        dfs(nums, visited, list, result);
        return result;
    }

    public void dfs(ArrayList<Integer> nums, boolean[] visited, ArrayList<Integer> list, ArrayList<ArrayList<Integer>> result) {
        if (list.size() == nums.size()) {
            result.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            //when visit the same number, or the previous number has not been used, we continue
            //only recursively call on the first duplicate number that has not been used
            if (visited[i] || (i > 0 && nums.get(i) == nums.get(i-1) && !visited[i-1])) {
                continue;
            }//可以先判断前面的一个数是否和自己相等，相等的时候则前面的数必须使用了，自己才能使用，这样就不会产生重复的排列了
             // visited[i-1]==0 is correct to skip the duplicate digit in recursion. What this code tries to do is to make sure all duplicate digits are used in transaction batch. either they are all used, or none of them is used.﻿
            //根据代码想了一阵倒是有另一个角度解释：假设有两个1，排序后位置不同，我们规定这两个1在排序中出现的顺序必须和数组中位置顺序一样，也就是第一个1只能出现在前面，第二个1只能出现在后面，这样就消除了重复解。对应到代码中，要排除的情况就是在前面的位置选择第二个1，这时检查发现第一个1还没用过就是这种情况，于是可以跳过了。
            visited[i] = true;
            //回溯有两种,一种是用visited来记录用过的数据,结束后要返回原值
            //另一种是在删减原始数据,比如substring或者increment起点或者decrement重点(remain)
            list.add(nums.get(i));
            dfs(nums, visited, list, result);
            list.remove(list.size() - 1);
            visited[i] = false;
        }
    }
}
```

``` python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        nums.sort()
        visited = [False] * len(nums)
        ret = []
        self.helper(nums, visited, [], ret)
        return ret

    def helper(self, nums, visited, curr, ret):
        if len(curr) == len(nums):
            ret.append(curr[:])
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            if not visited[i]:
                visited[i] = True
                self.helper(nums, visited, curr + [nums[i]], ret)
                visited[i] = False
```
