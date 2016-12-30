---
layout: post
title: String matching
date: 2015-12-09 18:17:30.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468925278;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:531;}i:1;a:1:{s:2:"id";i:1320;}i:2;a:1:{s:2:"id";i:583;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>给一个字典，里面全是string，字典很大，可能有几百万个string。然后写一个方法判断输入是否有一个typo，否则返回false。比如，字典有google，facebook，amazon等。输入google返回false，因为没有typo。输入geogle，返回true，因为有一个typo。输入geogla，返回false，因为有多于一个的typo。</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
