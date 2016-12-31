---
layout: post
title: Compare Version Numbers
date: 2015-11-05 14:31:17.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466041353;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1050;}i:1;a:1:{s:2:"id";i:1501;}i:2;a:1:{s:2:"id";i:398;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Compare two version numbers version1 and version2.<br />
If version1 > version2 return 1, if version1 &lt; version2 return -1, otherwise return 0.<br />
You may assume that the version strings are non-empty and contain only digits and the . character.<br />
The . character does not represent a decimal point and is used to separate number sequences.<br />
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int compareVersion(String version1, String version2) {
        int i = 0, j = 0;
        while (i < version1.length() || j < version2.length()) {
            int temp1 = 0, temp2 = 0;
            while (i < version1.length() && version1.charAt(i) != '.') {
                temp1 = temp1 * 10 + (version1.charAt(i++) - '0');
            }
            while (j < version2.length() && version2.charAt(j) != '.') {
                temp2 = temp2 * 10 + (version2.charAt(j++) - '0');
            }
            if (temp1 > temp2) {
                return 1;
            } else if (temp1 < temp2) {
                return -1;
            } else {
                i ++;
                j ++;
            }
        }
        return 0;
    }
}
</pre>
<p>[/expand]</p>
