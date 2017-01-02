---
layout: post
title: Wildcard Matching
date: 2015-10-21 02:15:18.000000000 -04:00
categories:
- String
author: Jason
---
<p><strong><em>Implement wildcard pattern matching with support for '?' and '</em>'.<br />

'?' Matches any single character.<br />
'<em>' Matches any sequence of characters (including the empty sequence).<br />
The matching should cover the entire input string (not partial).</em></strong><br />

``` java
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
```
