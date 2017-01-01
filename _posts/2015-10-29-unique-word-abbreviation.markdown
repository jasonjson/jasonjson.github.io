---
layout: post
title: Unique Word Abbreviation
date: 2015-10-29 13:02:33.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465999487;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1208;}i:1;a:1:{s:2:"id";i:1510;}i:2;a:1:{s:2:"id";i:1414;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations: Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.</last></number></first></em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class ValidWordAbbr {
    private HashMap<String, String> map = new HashMap<String, String>();
    public ValidWordAbbr(String[] dictionary) {
        if (dictionary == null || dictionary.length == 0) return;
        for (String s : dictionary) {
            if (s.length() <= 2) continue; //for the case of "ab" there are no abbr
            String newS = s.charAt(0) + String.valueOf(s.length() - 2) + s.charAt(s.length() - 1);
            if (map.containsKey(newS)) {
                map.put(newS, "");
            } else {
                map.put(newS, s);
            }
        }
    }

    public boolean isUnique(String word) {
        if (word == null || word.length() <= 2) return true;
        String newS = word.charAt(0) + String.valueOf(word.length() - 2) + word.charAt(word.length() - 1);
        return !map.containsKey(newS) || map.get(newS).equals(word);
        //["apple"] "apple" is true, since there are no other words than apple in the dictionary that have the same abbr
        //["dog"] "dig" is false, since dog and dig has same abbr
    }
}
</pre>
<p>[/expand]</p>
