---
layout: post
title: 93 - Restore IP Addresses
date: 2015-11-12 09:09:28.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a string containing only digits, restore it by returning all possible valid IP address combinations.**

```python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.helper(s, "", result, 0)
        return result

    def helper(self, s, temp, result, step):
        if step == 4:
            if len(s) == 0:
                result.append(temp[:-1])
            return

        for i in range(1, 4):
            if i > len(s):
                return
            sub_str = s[:i]
            if (self.is_valid(sub_str)):
                self.helper(s[i:], temp + sub_str + '.', result, step + 1)

    def is_valid(self, s):
        if s[0] == '0':
            return len(s) == 1
        return int(s) <= 255 and int(s) > 0
```
``` java
public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<String>();
        if (s == null || s.length() == 0) return result;

        helper(s, 0, "", result);
        return result;
    }

    public void helper(String s, int step, String path, List<String> result) {
        if (step == 4) {//这个负责控制多少段字符
            if (s.length() == 0) {
                result.add(path.substring(0, path.length() - 1));
            }
            return;
//不能合并上面的if，当step == 4就不必往下继续了, 也不能调换顺序，s可能很长，只要到了第四步就return
        }
        for (int i = 1; i <= 3; i++) {
           if (s.length() < i) return;
           int val = Integer.parseInt(s.substring(0, i));
           if (val <= 255 && String.valueOf(val).length() == i) {//去掉010这样的IP
               helper(s.substring(i), step + 1, path + val + ".", result);
           }
        }
    }
}
```

``` python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if not s:
            return []

        ret = []
        self.helper(0, s, [], ret)
        return ret

    def helper(self, step, s, curr, ret):
        if step == 4:
            if len(s) == 0:
                ret.append(".".join(curr))
            return
        for i in xrange(1, 4):
            if i > len(s):
                return
            val = int(s[:i])
            if val <= 255 and str(val) == s[:i]:
                self.helper(step + 1, s[i:], curr + [s[:i]], ret)
```
