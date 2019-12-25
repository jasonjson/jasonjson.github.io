---
layout: post
title: 332 - Reconstruct Itinerary
date: 2016-02-22 22:26:53.000000000 -05:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.**


``` java
public class Solution {
        public static List<String> findItinerary(String[][] tickets) {
        List<String> result = new ArrayList<>();
        if (tickets == null || tickets.length == 0) return result;

        Map<String, List<String>> map = new HashMap<>();
        for (String[] ticket : tickets) {
            List<String> arrival = map.containsKey(ticket[0]) ? map.get(ticket[0]) : new ArrayList<>();
            arrival.add(ticket[1]);
            map.put(ticket[0], arrival);
        }
        for (List<String> arrivals : map.values()) {
            Collections.sort(arrivals);
        }
        result.add("JFK");
        helper(map, result, "JFK", tickets.length + 1);
        return result;
    }

    public static boolean helper(Map<String, List<String>> map, List<String> path, String last, int stops) {
        if (path.size() == stops) {
            return true;
        }
        if (!map.containsKey(last) || map.get(last).size() == 0) return false;
        List<String> arrivals = map.get(last);
        for (int i = 0; i < arrivals.size(); i++) {
            String next = map.get(last).remove(i);
            path.add(next);
            if (helper(map, path, next, stops)) {
                return true;
            }
            path.remove(path.size() - 1);
            arrivals.add(i, next);//be aware of concurrency problem
        }
        return false;
    }
}
```

``` python
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []

        iter_map = defaultdict(list)
        for a, b in tickets:
            iter_map[a].append(b)
        [iter_map[k].sort() for k in iter_map]
        ret = ["JFK"]
        self.helper(iter_map, ret, len(tickets) + 1)
        return ret

    def helper(self, iter_map, ret, total_stops):
        if len(ret) == total_stops:
            return True

        next_stops = iter_map[ret[-1]]
        for i in range(len(next_stops)):
            ret.append(next_stops.pop(i))
            if self.helper(iter_map, ret, total_stops):
                return True
            next_stops.insert(i, ret.pop())
        return False
```
