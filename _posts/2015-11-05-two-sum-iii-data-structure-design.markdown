---
layout: post
title: Two Sum III - Data structure design
date: 2015-11-05 12:06:13.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Design and implement a TwoSum class. It should support the following operations: add and find.<br />

add - Add the number to an internal data structure.<br />
find - Find if there exists any pair of numbers which sum is equal to the value.</em></strong></p>
``` java
public class TwoSum {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    // Add the number to an internal data structure.
    public void add(int number) {
        if (!map.containsKey(number)) {
            map.put(number, 1);
        } else {
            map.put(number, map.get(number) + 1);
        }
    }

    // Find if there exists any pair of numbers which sum is equal to the value.
    public boolean find(int value) {
        for (int key : map.keySet()) {
            int other = value - key;
            if ((other == key && map.get(key) >= 2) || (other != key && map.containsKey(other))) {
                return true;
            }
        }
        return false;
    }
}
```
