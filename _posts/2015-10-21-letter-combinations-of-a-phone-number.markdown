---
layout: post
title: Letter Combinations of a Phone Number
date: 2015-10-21 14:43:14.000000000 -04:00
tags:
- Algorithm
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
    public ArrayList<string> letterCombinations(String digits) {
        ArrayList<string> result = new ArrayList<string>();
        if (digits == null || digits.length() == 0) return result;
        String[] letters = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        StringBuilder str = new StringBuilder();
        helper(digits, letters, str, result);
        return result;
    }

    public void helper(String digits, String[] letters, StringBuilder str, ArrayList<string> result) {
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
        self.helper(0, digits, letters, [], ret)
        return ret

    def helper(self, index, digits, letters, curr, ret):
        if index == len(digits):
            ret.append("".join(curr))
            return
        for char in letters[int(digits[index])]:
            curr.append(char)
            self.helper(index + 1, digits, letters, curr, ret)
            curr.pop()
```
