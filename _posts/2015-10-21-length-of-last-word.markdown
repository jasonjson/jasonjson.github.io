---
layout: post
title: Length of Last Word
date: 2015-10-21 02:15:44.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465989315;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:75;}i:1;a:1:{s:2:"id";i:89;}i:2;a:1:{s:2:"id";i:393;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string s consists of upper/lower-case alphabets and empty space characters ' ',<br />
return the length of last word in the string.If the last word does not exist, return 0.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public static int lengthOfLastWord(String s) {
        if (s ==  null || s == " ") return 0;
        String[] arr = s.split(" ");
        int n = arr.length;
        if (n > 0) { 
            return (arr[n-1].length());
        } else {
            return 0;
        }
    }
    
    public static int lengthOfLastWord(String s) {
        if(s == null || s.length() == 0) return 0;
        
        int start = 0, end = s.length() - 1;
        while (end > 0 && s.charAt(end) == ' ') { 
            end --;
        }
        for (int i = 0; i <= end; i++) {
            if (s.charAt(i) == ' ') {
                start = i + 1;
            }
        }
        return end - start + 1;
    }
}
</pre>
<p>[/expand]</p>
