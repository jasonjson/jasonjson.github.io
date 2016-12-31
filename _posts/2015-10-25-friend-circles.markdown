---
layout: post
title: Friend circles
date: 2015-10-25 19:51:28.000000000 -04:00
type: post
published: true
status: publish
categories:
- BFS
- Brain teaser
tags:
- Two sigma OA
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469242877;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:589;}i:1;a:1:{s:2:"id";i:393;}i:2;a:1:{s:2:"id";i:2059;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature, i.e., if A is friend of B and B is friend of C, then A is also friend of C. A friend circle is a group of students who are directly or indirectly friends. You are given a N×N−matrix M which consists of characters Y or N. If M[i][j]=Y, then ith and jth students are friends with each other, otherwise not. You have to print the total number of friend circles in the class.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public static void main(String[] args) {
        String[] friends = {"YYNN","YYYN","NYYN","NNNY"};
        System.out.println(friendCircles(friends));
    }
    public static int friendCircles (String[] friends) {
        if (friends == null || friends.length == 0) return 0;

        int circles = 0, n = friends.length;
        boolean[] visited = new boolean[n];
        Queue<integer> q = new LinkedList<integer>();
        q.offer(0);//0 is the index of first person in friends
        visited[0] = true;
        while (!q.isEmpty()) {
            int curr = q.poll();
            char[] currFriends = friends[curr].toCharArray();
            for (int i = 0; i < currFriends.length; i++) {
                if (currFriends[i] == 'Y' && i != curr && !visited[i]) {
                    q.offer(i);//i belongs the the circle with curr
                    visited[i] = true;
                }
            }
            if (q.isEmpty()) {//find another component/circle
                circles++;
                for (int i = 0; i < n; i++) {//offer next unvisited friend to the queue
                    if (!visited[i]) {
                        q.offer(i);//create a new component
                        visited[i] = true;
                    }
                }
            }
        }
        return circles;
    }
}
</integer></integer></pre>
<p>[/expand]</p>
