---
layout: post
title: Add and Search Word - Data structure design
date: 2015-11-04 11:39:30.000000000 -05:00
tags:
- Algorithm
categories:
- Data Structure
author: Jason
---
<p><strong><em>Design a data structure that supports the following two operations:</p>

void addWord(word)</p>
bool search(word)</p>
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.</em></strong></p>
``` java
public class WordDictionary {
    class TrieNode {
        boolean storeWord = false;
        TrieNode[] children = new TrieNode[26];
    }
    
    class Trie {
        TrieNode root = new TrieNode();
        public void insert(String word) {
            TrieNode curr = root;
            for (char c : word.toCharArray()) {
                if (curr.children[c - 'a'] == null) {
                    curr.children[c - 'a'] = new TrieNode();
                }
                curr = curr.children[c - 'a'];
            }
            curr.storeWord = true;
        }
        public boolean search(String word, TrieNode curr) {
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (c == '.') {
                    for (TrieNode temp : curr.children) {
                        if (temp != null && search(word.substring(i+1), temp)) {
                            return true;//search the rest chars, do not start from beginning
                        }
                    }
                    return false;
                } else {
                    if (curr.children[c - 'a'] == null) {
                        return false;
                    }
                    curr = curr.children[c - 'a'];
                }                
            }
            return curr.storeWord;
        }
    }
    Trie trie = new Trie();
    // Adds a word into the data structure.
    public void addWord(String word) {
        trie.insert(word);
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        return trie.search(word, trie.root);
    }
}
```
