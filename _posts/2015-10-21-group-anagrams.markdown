---
layout: post
title: 49 - Group Anagrams
date: 2015-10-21 02:11:51.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given an array of strings, return all groups of strings that are anagrams.**


``` java
public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> lists = new ArrayList<List<String>>();
        if(strs == null) return lists;

        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        for(String str : strs){
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);
            String sorted = String.valueOf(charArr);
            List<String> list = new ArrayList<String>();
            if(map.containsKey(sorted)){
                list = map.get(sorted);
            }
            list.add(str);
            map.put(sorted,list);
        }

        for(String key : map.keySet()){
            List<String> list = map.get(key);
            Collections.sort(list);
            //the problem requests this
            lists.add(list);
        }
        return lists;
    }
}
```

``` python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        str_dict = defaultdict(int)
        for s in strs:
            str_list["".join(sorted(s))].append(s)
        return list(str_dict.values())
```
