---
layout: post
title: 68 - Text Justification
date: 2015-11-13 09:05:29.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.**
**Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text, it should be left justified and no extra space is inserted between words.**

``` java
public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<String>();
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
```

``` python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr = []
        ret = []
        num_letters = 0
        for word in words:
            if num_letters + len(word) + len(curr) > maxWidth:
                for i in range(maxWidth - num_letters):
                    index = 0 if len(curr) == 1 else i % (len(curr) - 1)
                    curr[index] += " "
                ret.append("".join(curr))
                num_letters = 0
                curr = []
            curr.append(word)
            num_letters += len(word)
        ret.append(" ".join(curr).ljust(maxWidth))
        return ret
```
