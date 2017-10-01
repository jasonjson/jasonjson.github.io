---
layout: post
title: Word Ladder
date: 2015-10-21 12:57:57.000000000 -04:00
tags:
- Leetcode
categories:
- BFS
author: Jason
---
<p><strong><em>Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that: Only one letter can be changed at a time. Each intermediate word must exist in the dictionary</em></strong></p>


``` java
public class Solution {
    public int ladderLength(String beginWord, String endWord, Set<string> wordList) {
        wordList.add(endWord);
        HashMap<String, Boolean> visited = new HashMap<String, Boolean>();
        for (String s : wordList) {
            visited.put(s, false);
        }
        int ladder = 0;
        Queue<string> q = new LinkedList<string>();
        q.offer(beginWord);
        while (!q.isEmpty()) {
            ladder ++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                String curr = q.poll();
                if (curr.equals(endWord)) {
                    return ladder;
                }
                for (String u : getNext(curr, wordList)) {
                    if (!visited.get(u)) {
                        q.offer(u);
                        visited.put(u, true);
                    }
                }
            }
        }
        return 0;
    }
    
    public List<string> getNext(String s, Set<string> wordList) {
        List<string> result = new ArrayList<string>();
        for (int i = 0; i < s.length(); i++) {
            char[] chars = s.toCharArray();
            for (char c = 'a'; c <= 'z'; c++) {
                chars[i] = c;
                String newS = String.valueOf(chars);
                if (wordList.contains(newS)) {
                    result.add(newS);
                }
            }
        }
        return result;
    }
}
```
