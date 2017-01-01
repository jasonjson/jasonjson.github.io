---
layout: post
title: Reverse Words in a String
date: 2015-10-21 02:13:20.000000000 -04:00
type: post
published: true
status: publish
categories:
- String
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465763305;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1407;}i:1;a:1:{s:2:"id";i:99;}i:2;a:1:{s:2:"id";i:393;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an input string, reverse the string word by word.</em></strong></p>
<p>[expand title = "code1"]</p>
<pre>
public class Solution {
    public void reverseWords(char[] s) {
        int start = 0;
        for (int i = 0; i < s.length; i ++) {
            if (s[i] == ' ') {
                reverse(s, start, i - 1);
                start = i + 1;
            }
        }
        reverse(s, start, s.length - 1);//reverse the last word!!! there is no space after!!
        reverse(s, 0, s.length - 1);
    }
    
    public void reverse(char[] s, int lo, int hi) {
        while (lo <= hi) {
            char temp = s[lo];
            s[lo] = s[hi];
            s[hi] = temp;
            lo ++;
            hi --;
        }
    }
}
</pre>
<p>[/expand]<br />
[expand title="code2"]</p>
<pre>
public class Solution {
    /**
     * @param s : A string
     * @return : A string
     */
    public String reverseWords(String s) {
        // write your code
        if(s == null || s.length() == 0) return s;
        String[] arr = s.split(" ");
        //split the original string to str array, use space as separator, there will be empty strings in the array
        StringBuilder str = new StringBuilder();
        for(int i = arr.length-1; i >= 0; i--){
            if(!arr[i].equals("")){
            //!!!important, use "" instead of " " to deal with empty strings, not space
                str.append(arr[i]).append(" ");
            }
        }
        return str.toString();
    }
}
</pre>
<p>[/expand]</p>
