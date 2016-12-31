---
layout: post
title: Alien Dictionary
date: 2015-10-30 15:12:16.000000000 -04:00
type: post
published: true
status: publish
categories:
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466813548;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1510;}i:1;a:1:{s:2:"id";i:433;}i:2;a:1:{s:2:"id";i:1890;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public String alienOrder(String[] words) {
        if (words == null || words.length == 0) return "";
        
        StringBuilder rst = new StringBuilder();
        HashMap<Character, Integer> degree = new HashMap<Character, Integer>();
        HashMap<Character, Set<character>> map = new HashMap<Character, Set<character>>();
        for (String word : words) {
            for (char c : word.toCharArray()) {
                degree.put(c, 0);//初始化所有char的degree
            }
        }
        for (int i = 1; i < words.length; i++) {
            String s1 = words[i-1], s2 = words[i];
            int len = Math.min(s1.length(), s2.length());
            for (int j = 0; j < len; j++) {
                char c1 = s1.charAt(j), c2 = s2.charAt(j);
                if (c1 != c2) {
                    Set<character> set = new HashSet<character>();
                    if (map.containsKey(c1)) {
                        set = map.get(c1);
                    }
                    if (set.add(c2)) {//如果添加到set成功
                        map.put(c1, set);//有可能是新的set 所以必须加进map
                        degree.put(c2, degree.get(c2) + 1);
                    }
                    break;//don't forget to break!!
                }
            }
        }
        Queue<character> q = new LinkedList<character>();
        for (char c : degree.keySet()) {
            if (degree.get(c) == 0) {
                q.offer(c);
            }
        }
        while (!q.isEmpty()) {
            char curr = q.poll();
            rst.append(curr);
            if (map.containsKey(curr)) {//curr有可能不在map里，char可能没有child
                for (char child : map.get(curr)) {
                    degree.put(child, degree.get(child) - 1);
                    if (degree.get(child) == 0) {
                        q.offer(child);
                    }
                }
            }
        }
        if(rst.length() != degree.size()) return "";//!!important, there can be no suitable result
        return rst.toString();
    }
}
</character></character></character></character></character></character></pre>
<p>[/expand]</p>
