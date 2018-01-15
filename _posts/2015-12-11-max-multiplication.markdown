---
layout: post
title: OA - Max multiplication
date: 2015-12-11 11:44:45.000000000 -05:00
tags:
- OA
categories:
- Sorting
author: Jason
---
**Given two integer arrays, find the kth smallest multiplication by picking one element from each array.**


``` java
class Solution {
    public static void main(String[] args) {
        int[] num1 = {2,5,10,8,7};
        int[] num2 = {10, 9, 8, 6, 5};
        System.out.print(multiply(num1, num2, 5));
    }
    static class point {
        int i, j, val;
        public point(int i, int j, int val) {
            this.i = i;
            this.j = j;
            this.val = val;
        }
    }
    public static int multiply(int[] num1, int[] num2, int k) {
        if (num1.length == 0 || num2.length == 0) return 0;

        Arrays.sort(num1);
        Arrays.sort(num2);
        PriorityQueue<point> pq = new PriorityQueue<point>(k, new Comparator<point>() {
           public int compare(point a, point b) {
               return a.val - b.val;
           }
        });
        pq.offer(new point(0, 0, num1[0] * num2[0]));
        int result = 0;
        for (int i = 0; i < k; i++) {
            point curr = pq.poll();
            result = curr.val;
            set(pq, curr.i + 1, curr.j, num1, num2);
            set(pq, curr.i, curr.j + 1, num1, num2);
        }
        return result;
    }
    public static void set(PriorityQueue<point> pq, int i, int j, int[] num1, int[] num2) {
        if (i >= num1.length || j >= num2.length) return;
        pq.offer(new point(i, j, num1[i] * num2[j]));
    }
}
```

``` python
import heapq
class Solution(object):
    def find_k_th_smallest(self, arr1, arr2, k):
        if not arr1 or not arr2:
            return -1

        arr1.sort()
        arr2.sort()
        path = []
        heapq.heappush(path, (arr1[0] * arr2[0], 0, 0))
        ret = None
        for _ in xrange(k):
            ret, i, j = heapq.heappop(path)
            if i + 1 < len(arr1):
                heapq.heappush(path, (arr1[i + 1] * arr2[j], i + 1, j))
            if j + 1 < len(arr2):
                heapq.heappush(path, (arr1[i] * arr2[j + 1], i, j + 1))
        return ret
```
