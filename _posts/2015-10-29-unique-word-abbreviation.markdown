---
layout: post
title: 288 - Unique Word Abbreviation
date: 2015-10-29 13:02:33.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations: Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.**


``` java
public class ValidWordAbbr {
    private HashMap<String, String> map = new HashMap<String, String>();
    public ValidWordAbbr(String[] dictionary) {
        if (dictionary == null || dictionary.length == 0) return;
        for (String s : dictionary) {
            if (s.length() <= 2) continue;
            String newS = s.charAt(0) + String.valueOf(s.length() - 2) + s.charAt(s.length() - 1);
            if (map.containsKey(newS)) {
                map.put(newS, "");
            } else {
                map.put(newS, s);
            }
        }
    }

    public boolean isUnique(String word) {
        if (word == null || word.length() <= 2) return true;
        String newS = word.charAt(0) + String.valueOf(word.length() - 2) + word.charAt(word.length() - 1);
        return !map.containsKey(newS) || map.get(newS).equals(word);
    }
}
```

``` python
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.word_map = {}
        for s in dictionary:
            if len(s) <= 2:
                continue

            abbr = s[0] + str(len(s) - 2) + s[-1]
            if abbr in self.word_map:
                self.word_map[abbr] = ""
            else:
                self.word_map[abbr] = s

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if len(word) <= 2:
            return True

        abbr = word[0] + str(len(word) - 2) + word[-1]
        return  word == self.word_map.get(abbr, word)
```
