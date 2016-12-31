---
layout: post
title: Text Justification
date: 2015-11-13 09:05:29.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1462425355;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1510;}i:1;a:1:{s:2:"id";i:1890;}i:2;a:1:{s:2:"id";i:1201;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.<br />
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.<br />
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.<br />
For the last line of text, it should be left justified and no extra space is inserted between words.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<string> fullJustify(String[] words, int maxWidth) {
        List<string> result = new ArrayList<string>();
        if (words == null || words.length == 0) return result;
        
        int index = 0;
        while (index < words.length) {
            int len = words[index].length();//此处没有额外+1，相当于最后一个word不需要空格
            int last = index + 1;
            while (last < words.length && len + words[last].length() + 1 <= maxWidth) {
                len += words[last].length() + 1;
                last ++;
            }
            int diff = last - index - 1; //(number of words - 1) in this line
            StringBuilder sb = new StringBuilder();
            if (last == words.length || diff == 0) {
                for (int i = index; i < last; i++) {
                    sb.append(words[i] + " ");
                }
                sb.deleteCharAt(sb.length() - 1);
                for (int j = sb.length() + 1; j <= maxWidth; j++) {
                    sb.append(" ");
                }
            } else {
                int spaces = (maxWidth - len) / diff;
                int left = (maxWidth - len) % diff;
                for (int i = index; i < last; i++) {
                    sb.append(words[i] + " ");
                    if (i == last - 1) break;
                    for (int j = 0; j < spaces + (i - index < left ? 1 : 0); j ++) {
                        sb.append(" ");
                    }
                }
                sb.deleteCharAt(sb.length() - 1);
            }
            result.add(sb.toString());
            index = last;//!!!!
        }
        return result;
    }
}
</string></string></string></pre>
<p>[/expand]</p>
