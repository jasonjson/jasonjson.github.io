---
layout: post
title: Letter Combinations of a Phone Number
date: 2015-10-21 14:43:14.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465960641;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1119;}i:1;a:1:{s:2:"id";i:1208;}i:2;a:1:{s:2:"id";i:1424;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a digit string, return all possible letter combinations that the number could represent.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param digits A digital string
     * @return all posible letter combinations
     */
    public ArrayList<string> letterCombinations(String digits) {
        ArrayList<string> result = new ArrayList<string>();
        if (digits == null || digits.length() == 0) return result;
        String[] letters = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        StringBuilder str = new StringBuilder();
        helper(digits, letters, str, result);
        return result;
    }
    
    public void helper(String digits, String[] letters, StringBuilder str, ArrayList<string> result) {
        if (digits.length() == 0) {
            result.add(str.toString());
            return;
        }
        String toPick = letters[digits.charAt(0) - '0'];
        for (char c : toPick.toCharArray()) {
            str.append(c);
            helper(digits.substring(1), letters, str, result);
            str.deleteCharAt(str.length() - 1);
        }
    }
}
</string></string></string></string></pre>
<p>[/expand]</p>
