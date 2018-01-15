---
layout: post
title: 30 - Substring with Concatenation of All Words
date: 2015-11-15 11:38:30.000000000 -05:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.**


``` java
public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<Integer>();
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

``` python
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_map = defaultdict(int)
        for word in words:
            word_map[word] += 1

        ret = []
        length, number = len(words[0]), len(words)
        seen_map = defaultdict(int)
        for i in xrange(len(s) - length * number + 1):
            if s[i : i + length] in word_map:
                seen_map = defaultdict(int)
                j = 0
                while j < number:
                    new_s = s[i + j * length: i + (j + 1) * length]
                    if new_s in word_map:
                        seen_map[new_s] += 1
                        if seen_map[new_s] > word_map[new_s]:
                            break
                    else:
                        break
                    j += 1
                if j == number:
                    ret.append(i)
        return ret
```
