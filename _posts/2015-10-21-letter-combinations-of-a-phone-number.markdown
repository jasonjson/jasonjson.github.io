---
layout: post
title: 17 - Letter Combinations of a Phone Number
date: 2015-10-21 14:43:14.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given a digit string, return all possible letter combinations that the number could represent.**


``` java
public class Solution {
    /**
     * @param digits A digital string
     * @return all posible letter combinations
     */
    public ArrayList<String> letterCombinations(String digits) {
        ArrayList<String> result = new ArrayList<String>();
        if (digits == null || digits.length() == 0) return result;
        String[] letters = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        StringBuilder str = new StringBuilder();
        helper(digits, letters, str, result);
        return result;
    }

    public void helper(String digits, String[] letters, StringBuilder str, ArrayList<String> result) {
        if (digits.length() == 0) {
            result.add(str.toString());
            return;
        }
        String toPick = letters[digits.charAt(0) - '0'];
        for (char c : toPick.toCharArray()) {
            str.append(c);
            helper(digits.substring(1), letters, str, result);
            str.deleteCharAt(str.length() - 1);
        }
    }
}
```

``` python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ret = []
        self.helper(digits, letters, "", ret)
        return ret

    def helper(self, digits, letters, curr, ret):
        if len(digits) == 0:
            ret.append(curr)
            return
        for char in letters[int(digits[0])]:
            self.helper(digits[1:], letters, curr + char, ret)
```
