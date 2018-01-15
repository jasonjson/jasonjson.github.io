---
layout: post
title: OA - String matching
date: 2015-12-09 18:17:30.000000000 -05:00
tags:
- OA
categories:
- Data Structure
author: Jason
---
**给一个字典，里面全是string，字典很大，可能有几百万个string。然后写一个方法判断输入是否有一个typo，否则返回false。比如，字典有google，facebook，amazon等。输入google返回false，因为没有typo。输入geogle，返回true，因为有一个typo。输入geogla，返回false，因为有多于一个的typo**


``` java
class Solution {
    static class TrieNode {
        boolean isWord = false;
        TrieNode[] children = new TrieNode[26];
    }
    static class Trie {
        TrieNode root = new TrieNode();

        public void insert(String word) {
            TrieNode curr = root;
            for (char c : word.toCharArray()) {
                if (curr.children[c - 'a'] == null) {
                    curr.children[c - 'a'] = new TrieNode();
                }
                curr = curr.children[c - 'a'];
            }
            curr.isWord = true;
        }
        public boolean search(String word, TrieNode curr, Boolean typo) {
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (curr.children[c - 'a'] == null) {
                    if (!typo) {
                        typo = true;
                        if (search(word.substring(i+1), curr, typo)) {
                            return true;
                        }//one more char, googgle
                        for (TrieNode temp : curr.children) {
                            if (temp != null && search(word.substring(i+1), temp, typo)) {
                                return true;
                            }
                        }//wrong char gooble
                        for (TrieNode temp : curr.children) {
                            if (temp != null && search(word.substring(i), temp, typo)) {
                                return true;
                            }
                        }//missing a char gogle
                    } else {
                        return false;
                    }
                } else {
                    curr = curr.children[c - 'a'];
                }
            }
            return typo && curr.isWord;
        }
    }

    public static void main(String[] args) {
        String[] words = {"google","facebook","amazon"};
        Trie trie = new Trie();
        for (String word : words) {
            trie.insert(word);
        }
        System.out.println(trie.search("gogfgle", trie.root, false));
    }
}
```

``` python
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children.get(char)
        curr.is_word = True

    def search(self, word, curr, is_typo):
        for i, char in enumerate(word):
            if char in curr.children:
                curr = curr.children[char]
            else:
                if not is_typo:
                    is_typo = True
                    if self.search(word[i+1:], curr, is_typo):
                        return True
                    for tmp in curr.children.values():
                        if self.search(word[i+1:], tmp, is_typo) or self.search(word[i:], tmp, is_typo):
                            return True
        return is_typo and curr.is_word
```
