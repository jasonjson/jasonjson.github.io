---
layout: post
title: Reorder String
date: 2016-01-21 21:26:55.000000000 -05:00
tags:
- OA
categories:
- String
author: Jason
---
**BACCBBAAA -> ABABACABC，就是输出相邻字母不能相同的string**


``` java
public class Solution {
    public static void main(String[] args) {
        System.out.println(reOrder("BACCBBAAAACBACBAD"));
    }
    public static String reOrder(String s) {
        if (s == null || s.length() == 0) return "";

        HashMap<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        PriorityQueue<character> pq = new PriorityQueue<>(10, new Comparator<character>() {
            @Override
            public int compare(Character o1, Character o2) {
                return map.get(o2) - map.get(o1);
            }
        });
        StringBuilder sb = new StringBuilder();
        for (char c : map.keySet()) {
            pq.offer(c);
        }
        while (!pq.isEmpty()) {//每次poll出频率最大的两个字符，如果还没用完就塞回去，如果频率相同，heap应该是按照入列顺序排序，这样就保证了如果剩余字符频率都一样的话，刚用过的字符肯定在最后
            char c1 = pq.poll();
            sb.append(c1);
            if (pq.isEmpty()) {
                break;
            }
            char c2 = pq.poll();
            sb.append(c2);
            map.put(c1, map.get(c1) - 1);
            map.put(c2, map.get(c2) - 1);
            if (map.get(c1) > 0) {
                pq.offer(c1);
            }
            if (map.get(c2) > 0) {
                pq.offer(c2);
            }
        }
        return sb.toString();
    }
}
```

``` python
class Solution(object):
    def reOrder(self, s):
        if not s:
            return ""
        counter = collections.Counter(s)
        pq = []
        ret = []
        for k, v in counter.iteritems():
            heapq.heappush(pq, (-v, k))
        while pq:
            count1, char1 = heapq.heappop(pq)
            ret.append(char1)
            if not pq:
                break
            count2, char2 = heapq.heappop(pq)
            ret.append(char2)
            count1 += 1
            count2 += 1
            if count1 < 0:
                heapq.heappush(pq, (count1, char1))
            if count2 < 0:
                heapq.heappush(pq, (count2, char2))
        return "".join(ret)
```
