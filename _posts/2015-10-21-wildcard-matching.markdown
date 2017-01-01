---
layout: post
title: Wildcard Matching
date: 2015-10-21 02:15:18.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465849227;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1056;}i:1;a:1:{s:2:"id";i:1050;}i:2;a:1:{s:2:"id";i:1510;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement wildcard pattern matching with support for '?' and '</em>'.<br />
'?' Matches any single character.<br />
'<em>' Matches any sequence of characters (including the empty sequence).<br />
The matching should cover the entire input string (not partial).</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public static boolean isMatch(String s, String p) {
        int lenS = s.length(), lenP = p.length();
        boolean[][] d = new boolean[lenS+1][lenP+1];
        //d[i][j] is true, means s.substring(0,i) match p.substring(0,j)
        d[0][0] = true;
        //update the first row
        for(int i = 1; i <= lenP; i++){
            if(p.charAt(i-1) == '*') d[0][i] = d[0][i-1];
        }
        
        for(int i = 1; i<= lenS; i++){
            for(int j = 1; j <= lenP; j++){
                if(s.charAt(i-1) == p.charAt(j-1) || p.charAt(j-1) == '?'){
                    d[i][j] = d[i-1][j-1];
                }else if(p.charAt(j-1) == '*'){
                //find if there is a s[0, k - 1] that 
                //matches p[0, j - 1] for (k : 0 to i)
                    for(int k = 0; k <= i; k++){
                        if(d[k][j-1]) {
                            d[i][j] = true;
                            break;
                        }
                    }
                }
            }
        }
        return d[lenS][lenP];
        //check if s.substring(0,lenS-1) match p.substring(0,lenP-1)
    }
}
</pre>
<p>[/expand]</p>
