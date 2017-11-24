---
layout: post
title: 547 - Friend circles
date: 2015-10-25 19:51:28.000000000 -04:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends. Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.**


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
        Queue<Integer> q = new LinkedList<Integer>();
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
                        break;
                    }
                }
            }
        }
        return circles;
    }
}
```

``` python
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        if not M:
            return 0

        num = len(M)
        visited = [False] * num
        queue = collections.deque()

        visited[0] = True
        queue.append(0)
        ret = 0
        while queue:
            i = queue.popleft()
            for j in xrange(num):
                if M[i][j] == 1 and not visited[j] and i != j:
                    queue.append(j)
                    visited[j] = True
            if not queue:
                ret += 1
                for i in xrange(num):
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True
                        break
        return ret
```
