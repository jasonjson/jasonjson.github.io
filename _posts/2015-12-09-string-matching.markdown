---
layout: post
title: String matching
date: 2015-12-09 18:17:30.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
- Data Structure
author: Jason
---
<p><strong><em>给一个字典，里面全是string，字典很大，可能有几百万个string。然后写一个方法判断输入是否有一个typo，否则返回false。比如，字典有google，facebook，amazon等。输入google返回false，因为没有typo。输入geogle，返回true，因为有一个typo。输入geogla，返回false，因为有多于一个的typo。</em></strong></p>


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
