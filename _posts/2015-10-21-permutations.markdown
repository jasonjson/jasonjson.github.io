---
layout: post
title: 46 - Permutations
date: 2015-10-21 03:37:39.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given a list of numbers, return all possible permutations.**


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

``` python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        ret = []
        self.helper(nums, [], ret)
        return ret

    def helper(self, nums, curr, ret):
        if len(curr) == len(nums):
            ret.append(copy.deepcopy(curr))
            return

        for i, num in enumerate(nums):
            if num not in curr:
                curr.append(num)
                self.helper(nums, curr, ret)
                curr.pop()
```
