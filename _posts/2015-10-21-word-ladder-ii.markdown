---
layout: post
title: Word Ladder II
date: 2015-10-21 12:58:31.000000000 -04:00
type: post
published: true
status: publish
categories:
- BFS
- DFS Backtracking
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467839066;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:433;}i:1;a:1:{s:2:"id";i:1357;}i:2;a:1:{s:2:"id";i:1735;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public static List<List<string>> findLadders(String beginWord, String endWord, Set<string> wordList) {
        List<List<string>> result = new ArrayList<List<string>>();

        wordList.add(beginWord);
        wordList.add(endWord);
        HashMap<String, Integer> dist = new HashMap<String, Integer>();
        bfs(beginWord, dist, wordList);
        List<string> path = new ArrayList<>();
        path.add(endWord);
        dfs(endWord, beginWord, dist, wordList, path, result);
        return result;
    }
    public static void bfs(String start, HashMap<String, Integer> dist, Set<string> wordList) {
        Queue<string> q = new LinkedList<string>();
        q.offer(start);
        dist.put(start, 0);
        while (!q.isEmpty()) {
            String curr = q.poll();
            for (String s : getWord(curr, wordList)) {
                if (!dist.containsKey(s)) {
                    q.offer(s);
                    dist.put(s, dist.get(curr) + 1);
                }
            }
        }
    }
    public static void dfs(String end, String start, HashMap<String, Integer> dist, Set<string> wordList, List<string> path, List<List<string>> result) {
        if (end.equals(start)) {
            Collections.reverse(path);
            result.add(new ArrayList<string>(path));
            Collections.reverse(path);
            return;
        }
        for (String s : getWord(end, wordList)) {
            if (dist.containsKey(s) && dist.get(s) + 1 == dist.get(end)) {
                path.add(s);
                dfs(s, start, dist, wordList, path, result);
                path.remove(path.size() - 1);
            }
        }
    }
    public static Set<string> getWord(String s, Set<string> wordList) {
        Set<string> result = new HashSet<string>();
        for (int i = 0; i < s.length(); i++) {
            char[] chars = s.toCharArray();
            for (char c = 'a'; c <= 'z'; c++) {
                if (chars[i] == c) continue;
                chars[i] = c;
                String newS = String.valueOf(chars);
                if (wordList.contains(newS)) {
                    result.add(newS);
                }
            }
        }
        return result;
    }
}
</string></string></string></string></string></string></string></string></string></string></string></string></string></string></string></string></pre>
<p>[/expand]</p>
