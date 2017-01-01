---
layout: post
title: Maximum Product of Word Lengths
date: 2015-12-15 14:06:56.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- String
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468533369;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1510;}i:1;a:1:{s:2:"id";i:1484;}i:2;a:1:{s:2:"id";i:1201;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.</em></strong></p>
<p>[expand title = "bit"]</p>
<pre>
public class Solution {
    public int maxProduct(String[] words) {
        if (words == null || words.length == 0) return 0;
        
        int[] mask = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                mask[i] |= 1 << (words[i].charAt(j) - 'a');
            }
        }
        int result = 0;
        for (int i = 0; i < words.length; i ++) {
            for (int j = 1; j < words.length; j++) {
                if ((mask[i] & mask[j]) == 0) {
                    result = Math.max(result, words[i].length() * words[j].length());
                }
            }
        }
        return result;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int maxProduct(String[] words) {
        if (words == null || words.length == 0) return 0;
        
        int result = 0;
        for (int i = 0; i < words.length; i++) {
            int[] letters = new int[26];
            for (char c : words[i].toCharArray()) {
                letters[c - 'a'] ++;
            }
            for (int j = i + 1; j < words.length; j++) {
                int k = 0;
                for (; k < words[j].length(); k++) {
                    if (letters[words[j].charAt(k) - 'a'] != 0) {
                        break;
                    }
                }
                if (k == words[j].length()) {
                    result = Math.max(result, words[i].length() * words[j].length());
                }
            }
        }
        return result;
    }
}
</pre>
<p>[/expand]</p>
