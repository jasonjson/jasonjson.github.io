---
layout: post
title: Reconstruct Itinerary
date: 2016-02-22 22:26:53.000000000 -05:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468549969;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1208;}i:1;a:1:{s:2:"id";i:107;}i:2;a:1:{s:2:"id";i:1251;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
        public static List<string> findItinerary(String[][] tickets) {
        List<string> result = new ArrayList<>();
        if (tickets == null || tickets.length == 0) return result;

        Map<String, List<string>> map = new HashMap<>();
        for (String[] ticket : tickets) {
            List<string> arrival = map.containsKey(ticket[0]) ? map.get(ticket[0]) : new ArrayList<>();
            arrival.add(ticket[1]);
            map.put(ticket[0], arrival);
        }
        for (List<string> arrivals : map.values()) {
            Collections.sort(arrivals);
        }
        result.add("JFK");
        helper(map, result, "JFK", tickets.length + 1);
        return result;
    }

    public static boolean helper(Map<String, List<string>> map, List<string> path, String last, int stops) {
        if (path.size() == stops) {
            return true;
        }
        if (!map.containsKey(last) || map.get(last).size() == 0) return false;
        List<string> arrivals = map.get(last);
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
</string></string></string></string></string></string></string></string></pre>
<p>[/expand]</p>
