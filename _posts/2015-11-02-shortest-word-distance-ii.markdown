---
layout: post
title: Shortest Word Distance II
date: 2015-11-02 13:36:55.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?</p>

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.</em></strong></p>
``` java
public class WordDistance {
    HashMap<String, List<Integer>> map = new HashMap<String, List<Integer>>();
    public WordDistance(String[] words) {
        for (int i = 0; i < words.length; i++) {
            if (!map.containsKey(words[i])) {
                map.put(words[i], new ArrayList<Integer>());
            }
            map.get(words[i]).add(i);
        }
    }

    public int shortest(String word1, String word2) {
        List<Integer> l1 = map.get(word1);
        List<Integer> l2 = map.get(word2);
        int min = Integer.MAX_VALUE;
        int i = 0, j = 0;
        while (i < l1.size() && j < l2.size()) {
            int index1 = l1.get(i), index2 = l2.get(j);
            min = Math.min(min, Math.abs(index1 - index2));
            if (index1 < index2) {
                i ++;
            } else {
                j ++;
            }
        }//no need to consider the rest elements
        return min;
    }
}
```
