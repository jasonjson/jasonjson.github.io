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
    public List<List<string>> groupAnagrams(String[] strs) {
        List<List<string>> lists = new ArrayList<List<string>>();
        if(strs == null) return lists;

        HashMap<String, List<string>> map = new HashMap<String, List<string>>();
        for(String str : strs){
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);
            String sorted = String.valueOf(charArr);
            List<string> list = new ArrayList<string>();
            if(map.containsKey(sorted)){
                list = map.get(sorted);
            }
            list.add(str);
            map.put(sorted,list);
        }

        for(String key : map.keySet()){
            List<string> list = map.get(key);
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

        str_dict = {}
        for s in strs:
            str_list= str_dict.setdefault("".join(sorted(s)), [])
            str_list.append(s)
        return str_dict.values()
```
