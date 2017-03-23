---
layout: post
title: Friend circles
date: 2015-10-25 19:51:28.000000000 -04:00
tags:
- Algorithm
categories:
- BFS
- Brain teaser
- Two sigma OA
author: Jason
---
<p><strong><em>There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature, i.e., if A is friend of B and B is friend of C, then A is also friend of C. A friend circle is a group of students who are directly or indirectly friends. You are given a N×N−matrix M which consists of characters Y or N. If M[i][j]=Y, then ith and jth students are friends with each other, otherwise not. You have to print the total number of friend circles in the class.</em></strong></p>


``` java
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
```
