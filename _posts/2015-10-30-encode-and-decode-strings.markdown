---
layout: post
title: 271 - Encode and Decode Strings
date: 2015-10-30 11:43:26.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.**


``` java
public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        if (strs == null || strs.size() == 0) return "";

        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length() + "/" + s);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        if (s == null || s.length() == 0) return result;

        for (int i = 0; i < s.length();) {
            int slash = s.indexOf("/", i);
            int len = Integer.parseInt(s.substring(i, slash));
            result.add(s.substring(slash + 1, slash + len + 1));
            i = slash + len + 1;
        }
        return result;
    }
}
```

``` python
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        return "".join([str(len(s)) + "/" + s for s in strs])


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """

        ret = []
        index = 0
        while index < len(s):
            slash = s.index("/", index)
            size = int(s[index : slash])
            ret.append(s[slash + 1 : slash + size + 1])
            index = slash + size + 1
        return ret
```
