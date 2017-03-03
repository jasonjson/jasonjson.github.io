---
layout: post
title: Permutations
date: 2015-10-21 03:37:39.000000000 -04:00
tags: algorithm
categories:
- DFS Backtracking
- Permutation
author: Jason
---
<p><strong><em>Given a list of numbers, return all possible permutations.</em></strong></p>


``` java
class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public ArrayList<ArrayList<integer>> permute(ArrayList<integer> nums) {
        // write your code here
        ArrayList<ArrayList<integer>> result = new ArrayList<ArrayList<integer>>();
        if (nums == null || nums.size() == 0) return result;
        
        ArrayList<integer> list = new ArrayList<integer>();
        dfs(nums, list, result);
        return result;
    }
    
    public void dfs(ArrayList<integer> nums, ArrayList<integer> list, ArrayList<ArrayList<integer>> result) {
        if (list.size() == nums.size()) {
            result.add(new ArrayList<integer> (list));
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (list.contains(nums.get(i))) {
                continue;//if this number is already in the list, we continue
            }//assumes no duplicates in nums
            //对这种order matters的问题，不能increment start来处理问题
            list.add(nums.get(i));
            dfs(nums, list, result);
            list.remove(list.size() - 1);
        }
    }
}
```
