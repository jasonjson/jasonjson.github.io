---
layout: post
title: 320 - Generalized Abbreviation
date: 2015-12-22 16:04:37.000000000 -05:00
tags:
- Leetcode
categories:
- DFS
author: Jason
---
**Write a function to generate the generalized abbreviations of a word. Example: Given word = "word", return the following list (order does not matter): ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]**


``` java
public class Solution {
    public List<String> generateAbbreviations(String word) {
        List<String> result = new ArrayList<String>();
        //true indicates we can add abbreviation(numbers)
        helper(word, 0, "", result, true);
        return result;
    }

    public void helper(String word, int start, String path, List<String> result, boolean addAbbr) {
        if (start == word.length()) {
            result.add(new String(path));
            return;
        }
        if (addAbbr) {
            for (int i = start + 1; i <= word.length(); i++) {
                helper(word, i, path + (i - start), result, false);
            }
        }
        helper(word, start + 1, path + word.charAt(start), result, true);
    }
}
```

```python
class Solution():
    def generateAbbreviations(self, word):
        result = []
        self.helper(word, 0, "", result, False)
        return result

    def helper(self, word, start, path, result, num_added):
        if start == len(word):
            result.append(path)
            return
        if not num_added:
            for i in range(start + 1, len(word) + 1):
                self.helper(word, i, path + str(i - start), result, True)
        self.helper(word, start + 1, path + word[start], result, False)
```
