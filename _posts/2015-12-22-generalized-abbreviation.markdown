---
layout: post
title: Generalized Abbreviation
date: 2015-12-22 16:04:37.000000000 -05:00
categories:
- Brain teaser
- DFS Backtracking
author: Jason
---
<p><strong><em>Write a function to generate the generalized abbreviations of a word.<br />

Example:<br />
Given word = "word", return the following list (order does not matter):<br />
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]</em></strong></p>
``` java
public class Solution {
    public List<string> generateAbbreviations(String word) {
        List<string> result = new ArrayList<string>();
        //if (word == null || word.length() == 0) return result; empty string also has abbreviation
        helper(word, 0, "", result, true);//true indicates we can add abbreviation(numbers)
        return result;
    }
    
    public void helper(String word, int start, String path, List<string> result, boolean addAbbr) {
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
