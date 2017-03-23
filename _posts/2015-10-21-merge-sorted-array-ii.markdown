---
layout: post
title: Merge Sorted Array II
date: 2015-10-21 02:25:04.000000000 -04:00
tags:
- Algorithm
categories:
- Sorting
author: Jason
---
<p><strong><em>Merge two given sorted integer array A and B into a new sorted integer array.</em></strong></p>


``` java
class Solution {
    /**
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    public ArrayList<integer> mergeSortedArray(ArrayList<integer> A, ArrayList<integer> B) {
        // write your code here
        ArrayList<integer> C = new ArrayList<integer>();
        while (!A.isEmpty() && !B.isEmpty()){
            if (A.get(0) <= B.get(0)) C.add(A.remove(0));
            else C.add(B.remove(0));
        }
        while (!A.isEmpty()){
            C.add(A.remove(0));
        }
        while (!B.isEmpty()){
            C.add(B.remove(0));
        }
        return C;
    }
}
```
