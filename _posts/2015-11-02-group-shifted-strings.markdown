---
layout: post
title: 249 - Group Shifted Strings
date: 2015-11-02 09:26:18.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence: "abc" -> "bcd" -> ... -> "xyz" Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.**


``` java
public class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        List<List<String>> result = new ArrayList<List<String>>();
        if (strings == null || strings.length == 0) return result;

        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        Arrays.sort(strings);
        for (String s : strings) {
            String key = "";
            for (int i = 1; i < s.length(); i++) {
                key += (s.charAt(i) - s.charAt(i-1) + 26) % 26;
            }
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<String>());
            }
            map.get(key).add(s);
        }
        for (List<String> list : map.values()) {
            result.add(list);
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        if not strings:
            return []
        dist_map = collections.defaultdict(list)
        for s in strings:
            dist = []
            if len(s) == 0:
                dist_map["0"].append(s)
            else:
                for i in xrange(1, len(s)):
                    dist.append(str((ord(s[i]) - ord(s[i-1]) + 26) % 26))
                dist_map[''.join(dist)].append(s)
        return dist_map.values()
```
