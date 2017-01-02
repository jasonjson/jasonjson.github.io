---
layout: post
title: Implement Trie
date: 2015-10-21 14:22:20.000000000 -04:00
categories:
- Data Structure
author: Jason
---
<p><strong><em>Implement a trie with insert, search, and startsWith methods.</em></strong></p>

``` java
class TrieNode {
    boolean storeWord = false;
    TrieNode[] children = new TrieNode[26];
}
public class Solution {
    TrieNode root = new TrieNode();
    
    public void insert (String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                curr.children[c - 'a'] = new TrieNode();
            }
            curr = curr.children[c - 'a'];
        }
        curr.storeWord = true;
    }
    
    public boolean search (String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                return false;
            }
            curr = curr.children[c - 'a'];
        }
        return curr.storeWord;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        for (char c : prefix.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                return false;
            }
            curr = curr.children[c - 'a'];
        }
        return true;
    }
}
```
