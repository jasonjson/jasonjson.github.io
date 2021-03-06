---
layout: post
title: 90 - Subsets II
date: 2015-10-21 03:37:09.000000000 -04:00
tags:
- Leetcode
categories:
- DFS
author: Jason
---
**Given a list of numbers that may has duplicate numbers, return all possible subsets.**


``` java
class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public ArrayList<ArrayList<Integer>> subsetsWithDup(ArrayList<Integer> S) {
        // write your code here
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (S == null || S.size() == 0) return result;

        Collections.sort(S);//remember to sort!!
        ArrayList<Integer> list = new ArrayList<Integer>();
        dfs(S, 0, list, result);
        return result;
    }

    public void dfs(ArrayList<Integer> S, int start, ArrayList<Integer> list, ArrayList<ArrayList<Integer>> result) {
        result.add(new ArrayList<Integer>(list));
        for (int i = start; i < S.size(); i++) {
            if (i > start && S.get(i) == S.get(i-1)) {
                continue;
                //jump i if it is the same with previous
                //i > start not i > 0, important!! same mistakes as in permutations problems
            }
            list.add(S.get(i));
            dfs(S, i + 1, list, result);
            list.remove(list.size() - 1);
        }
    }
}
```

``` python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        ret = []
        nums.sort()
        self.helper(nums, 0, [], ret)
        return ret

    def helper(self, nums, start, curr, ret):
        ret.append(curr[:])
        for i in xrange(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            self.helper(nums, i + 1, curr, ret)
            curr.pop()
```
