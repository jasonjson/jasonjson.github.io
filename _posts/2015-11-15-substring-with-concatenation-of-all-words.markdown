---
layout: post
title: Substring with Concatenation of All Words
date: 2015-11-15 11:38:30.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.</em></strong></p>

``` java
public class Solution {
    public List<integer> findSubstring(String s, String[] words) {
        List<integer> result = new ArrayList<integer>();
        if(words.length == 0 || s.length() == 0) return result;
        
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for (String word : words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        int len = words[0].length(), num = words.length;
        for (int k = 0; k < len; k++) {//len of a word
            HashMap<String,Integer> toFind = new HashMap<String, Integer>(map);
            for (int i = k, j = 0; i + j + len - 1 < s.length();){
            //i is the start point of the matching string 
            //j is the length of the matching string
                String temp = s.substring(i + j, i + j + len);
                if (toFind.containsKey(temp)) {
                    toFind.put(temp, toFind.get(temp) - 1);
                    if (toFind.get(temp) == 0) {
                        toFind.remove(temp);
                    }
                    if (toFind.isEmpty()) {
                        result.add(i);
                    }
                    j += len;
                } else {
                    if (j == 0) {
                        i += len;
                    } else {
                        String newS = s.substring(i, i + len);
                        toFind.put(newS, toFind.getOrDefault(newS, 0) + 1);
                        i += len;
                        j -= len;
                    }
                }
            }
        }
        return result;
    }
}
```
``` java
public class Solution {
    public List<integer> findSubstring(String s, String[] words) {
        List<integer> result = new ArrayList<integer>();
        if (s.length() == 0 || words.length == 0) return result;
        
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for (String word : words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        
        int len = words[0].length(), num = words.length;
        HashMap<String, Integer> seen = new HashMap<String, Integer>();
        for (int i = 0; i < s.length() - len * num + 1; i++) {
            if (map.containsKey(s.substring(i, i + len))) {
                seen.clear();
                int j = 0;
                for (; j < num; j++) {
                    String word = s.substring(i + j * len, i + j * len + len);
                    if (map.containsKey(word)) {
                        seen.put(word, seen.getOrDefault(word, 0) + 1);
                        if (seen.get(word) > map.get(word)) {
                            break;
                        }
                    } else {
                        break;
                    }
                }
                if (j == num) {
                    result.add(i);
                }
            }
        }
        return result;
    }
}
```
