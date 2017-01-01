---
layout: post
title: Two Strings Are Anagrams
date: 2015-10-21 02:10:56.000000000 -04:00
type: post
published: true
status: publish
categories:
- String
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465536764;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1050;}i:1;a:1:{s:2:"id";i:411;}i:2;a:1:{s:2:"id";i:450;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Write a method anagram(s,t) to decide if two strings are anagrams or not.</em></strong><br />
[expand title="code"]</p>
<pre>
public class solution {
    public static void main(String[] args) {
        String s1 = "abcd";
        String s2 = "bcda";
        System.out.println(isAnagram(s1,s2));
        System.out.println(isAnagram2(s1,s2));
    }

    public static boolean isAnagram(String s1, String s2){
        if (s1.isEmpty() || s2.isEmpty()) return false;
        if (s1.length() != s2.length()) return false;
        //error check!!!
        char[] charArr1 = s1.toCharArray();
        char[] charArr2 = s2.toCharArray();
        Arrays.sort(charArr1);
        Arrays.sort(charArr2);
        return String.valueOf(charArr1).equals(String.valueOf(charArr2));
    }

    public static boolean isAnagram2(String s1, String s2){
        if (s1.isEmpty() || s2.isEmpty()) return false;
        if (s1.length() != s2.length()) return false;
        int[] counts = new int[256];
        for (int i = 0; i < s1.length(); i++){
            counts[s1.charAt(i)] ++;
        }
        for (int j = 0; j < s2.length(); j++){
            if (--counts[s2.charAt(j)] < 0) return false;
        }
        return true;
    }
}
</pre>
<p>[/expand]</p>
