---
layout: post
title: Unique Word Abbreviation
date: 2015-10-29 13:02:33.000000000 -04:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations: Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.</last></number></first></em></strong></p>


``` java
public class ValidWordAbbr {
    private HashMap<String, String> map = new HashMap<String, String>();
    public ValidWordAbbr(String[] dictionary) {
        if (dictionary == null || dictionary.length == 0) return;
        for (String s : dictionary) {
            if (s.length() <= 2) continue; //for the case of "ab" there are no abbr
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
        //["apple"] "apple" is true, since there are no other words than apple in the dictionary that have the same abbr
        //["dog"] "dig" is false, since dog and dig has same abbr
    }
}
```
