---
layout: post
title: Permutations II
date: 2015-10-21 03:38:30.000000000 -04:00
categories:
- DFS Backtracking
- Permutation
author: Jason
---
<p><strong><em>Given a list of numbers with duplicate number in it. Find all unique permutations.</em></strong><br />


``` java
class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of unique permutations.
     */
    public ArrayList<ArrayList<integer>> permuteUnique(ArrayList<integer> nums) {
        // write your code here
        ArrayList<ArrayList<integer>> result = new ArrayList<ArrayList<integer>>();
        if (nums == null || nums.size() == 0) return result;
        
        Collections.sort(nums);
        ArrayList<integer> list = new ArrayList<integer>();
        boolean[] visited = new boolean [nums.size()];
        dfs(nums, visited, list, result);
        return result;
    }
    
    public void dfs(ArrayList<integer> nums, boolean[] visited, ArrayList<integer> list, ArrayList<ArrayList<integer>> result) {
        if (list.size() == nums.size()) {
            result.add(new ArrayList<integer>(list));
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
