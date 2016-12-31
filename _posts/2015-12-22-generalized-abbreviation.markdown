---
layout: post
title: Generalized Abbreviation
date: 2015-12-22 16:04:37.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- DFS Backtracking
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468618013;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:583;}i:1;a:1:{s:2:"id";i:1414;}i:2;a:1:{s:2:"id";i:1208;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Write a function to generate the generalized abbreviations of a word.<br />
Example:<br />
Given word = "word", return the following list (order does not matter):<br />
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<string> generateAbbreviations(String word) {
        List<string> result = new ArrayList<string>();
        //if (word == null || word.length() == 0) return result; empty string also has abbreviation
        helper(word, 0, "", result, true);//true indicates we can add abbreviation(numbers)
        return result;
    }
    
    public void helper(String word, int start, String path, List<string> result, boolean addAbbr) {
        if (start == word.length()) {
            result.add(new String(path));
            return;
        }
        if (addAbbr) {
            for (int i = start + 1; i <= word.length(); i++) {
                helper(word, i, path + (i - start), result, false);
            }
        }
        helper(word, start + 1, path + word.charAt(start), result, true);
    }
}
</string></string></string></string></pre>
<p>[/expand]</p>
