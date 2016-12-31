---
layout: post
title: Reorder String
date: 2016-01-21 21:26:55.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1462783102;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1201;}i:1;a:1:{s:2:"id";i:2049;}i:2;a:1:{s:2:"id";i:1005;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>BACCBBAAA -> ABABACABC，就是输出相邻字母不能相同的string</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</character></character></pre>
<p>[/expand]</p>
