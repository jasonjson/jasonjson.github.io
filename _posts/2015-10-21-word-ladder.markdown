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
import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if not wordList:
            return 0

        dict_words = self.construct_dict(wordList)
        word_queue = collections.deque([(beginWord, 1)])
        visited = set()
        while word_queue:
            curr_word, step = word_queue.popleft()
            if curr_word not in visited:
                visited.add(curr_word)
                if curr_word == endWord:
                    return step
                for i in xrange(len(curr_word)):
                    s = curr_word[:i] + "_" + curr_word[i+1:]
                    neigh_words = dict_words.get(s, [])
                    for new_word in neigh_words:
                        if new_word not in visited:
                            word_queue.append((new_word, step + 1))
        return 0

    def construct_dict(self, word_list):
        #find all possible tranformation words
        d = {}
        for word in word_list:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                d[s] = d.get(s, []) + [word]
        return d
```
