---
layout: post
title: 127 - Word Ladder
date: 2015-10-21 12:57:57.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that: Only one letter can be changed at a time. Each intermediate word must exist in the dictionary.**


``` java
public class Solution {
    public int ladderLength(String beginWord, String endWord, Set<String> wordList) {
        wordList.add(endWord);
        HashMap<String, Boolean> visited = new HashMap<String, Boolean>();
        for (String s : wordList) {
            visited.put(s, false);
        }
        int ladder = 0;
        Queue<String> q = new LinkedList<String>();
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

    public List<String> getNext(String s, Set<String> wordList) {
        List<String> result = new ArrayList<String>();
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

``` python
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words_map = self.helper(wordList)
        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            curr, step = queue.pop(0)
            if curr == endWord:
                return step
            visited.add(curr)
            step += 1
            for i in range(len(curr)):
                new_curr = curr[:i] + "_" + curr[i+1:]
                for candidate in words_map.get(new_curr, []):
                    if candidate not in visited:
                        queue.append((candidate, step))
        return 0

    def helper(self, wordList):
        words_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + "_" + word[i+1:]
                words_map[new_word].append(word)
        return words_map
```
